from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Recipe, User
from exts import db
from flask_migrate  import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required



app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app, db)
JWTManager(app)

api = Api(app, doc='/docs')


recipe_model = api.model(
    'Recipe',
    {
        'id': fields.Integer(),
        'title': fields.String(),
        'description': fields.String()
    }
)

signup_model = api.model(
    'Signup',
    {
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'password': fields.String(required=True)
    }
)

login_model = api.model(
    'Login',
    {
        'username': fields.String(required=True),
        'password': fields.String(required=True)
    }
)

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}

@api.route('/signup')
class SignUp(Resource):
    @api.expect(signup_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')

        db_user = User.query.filter_by(username=username).first()

        if db_user is not None:
            return jsonify({"message":f"User with {username} as username already exists"})
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))
        )
        new_user.save_user()

        return jsonify({"message":"User created successfully"})
        


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password') 

        db_user = User.query.filter_by(username=username).first()

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)

            return jsonify(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            )



@api.route('/recipes')
class RecipeResource(Resource):
    @api.marshal_list_with(recipe_model)
    def get(self):
        # Get all recipes
        recipes= Recipe.query.all()
        return recipes
    @api.marshal_with(recipe_model)
    @api.expect(recipe_model)
    @jwt_required()
    def post(self):
        # Create a new recipe
        data = request.get_json()
        new_recipe = Recipe(
            title=data.get('title'), 
            description=data.get('description'),
            )

        new_recipe.save_recipe()
        return new_recipe, 201
@api.route('/recipes/<int:id>')
class RecipeResource(Resource):
    @api.marshal_with(recipe_model)
    def get(self, id):
        # Get a recipe by id
        recipe = Recipe.query.get_or_404(id)

        return recipe
    @api.marshal_with(recipe_model)
    @jwt_required()
    def put(self, id):
        # Update a recipe by id
        recipe_to_update = Recipe.query.get_or_404(id)
        data = request.get_json()
        recipe_to_update.update_recipe(data.get('title'), data.get('description'))
        return recipe_to_update, 200
    @api.marshal_with(recipe_model)
    @jwt_required()
    def delete(self, id):
        # Delete a recipe by id
        recipe_to_delete = Recipe.query.get_or_404(id)
        recipe_to_delete.delete_recipe()
        return recipe_to_delete, 200


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Recipe': Recipe}



if __name__ == '__main__':
    app.run()