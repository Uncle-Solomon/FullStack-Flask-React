from flask_restx import Api, Resource, Namespace, fields
from flask import request, jsonify
from models import User
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_ns=Namespace('auth', description="A namespace for authentication")


signup_model = auth_ns.model(
    'Signup',
    {
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'password': fields.String(required=True)
    }
)

login_model = auth_ns.model(
    'Login',
    {
        'username': fields.String(required=True),
        'password': fields.String(required=True)
    }
)

@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(signup_model)
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
        

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
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


