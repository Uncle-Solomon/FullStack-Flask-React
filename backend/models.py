from exts import db

class Recipe(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    title=db.Column(db.String(), nullable=False)
    description=db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.title} >"

    
    def save_recipe(self):
        db.session.add(self)
        db.session.commit()

    def delete_recipe(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_recipe(self, title, description):
        self.title=title
        self.description=description
        db.session.commit()



class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(25), unique=True, nullable=False)
    email=db.Column(db.String(85), unique=True, nullable=False)
    password=db.Column(db.Text(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username} >"
    
    