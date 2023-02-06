import unittest
from config import TestConfig
from exts import db
from main import create_app
from flask import jsonify


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def test_hello_world(self):
        hello_response = self.client.get('/recipe/hello')

        json = hello_response.json

        self.assertEqual(json, {'message': 'Hello World'})
        # print(json)

    def test_signup(self):
        signup_response = self.client.post(
            '/auth/signup', 
            json = {
                "username": "testuser", 
                "email": "testuser@tst.com", 
                "password": "password"
                }, 
            content_type='application/json')

        status_code = signup_response.status_code

        self.assertEqual(status_code,201)
    
    def test_login(self):
        signup_response = self.client.post(
            '/auth/signup', 
            json = {
                "username": "testuser", 
                "email": "testuser@tst.com", 
                "password": "password"
                }, 
            content_type='application/json')

        login_response = self.client.post(
            '/auth/login', 
            json = {
                "username": "testuser", 
                "password": "password"
                }, 
            content_type='application/json')

        status_code = login_response.status_code

        self.assertEqual(status_code,200)


    def test_get_all_recipes(self):
        response = self.client.get('/recipe/recipes')

        json = response.json

        status_code = response.status_code

        self.assertEqual(status_code,200)

    def test_get_one_recipe(self):
        id=1
        response = self.client.get('/recipe/recipes/{}'.format(id))

        status_code = response.status_code

        self.assertEqual(status_code, 404)


    def test_create_recipe(self):
        signup_response = self.client.post(
            '/auth/signup', 
            json = {
                "username": "testuser", 
                "email": "testuser@tst.com", 
                "password": "password"
                }, 
            content_type='application/json')

        login_response = self.client.post(
            '/auth/login', 
            json = {
                "username": "testuser", 
                "password": "password"
                }, 
            content_type='application/json')

        access_token = login_response.json['access_token']


        create_recipe_response = self.client.post(
            '/recipe/recipes',
            json={
                "title": "Test Cookie",
                "description": "test description",
            },
            headers={
                'Authorization': 'Bearer {}'.format(access_token)
            }
        )

        status_code = create_recipe_response.status_code

        print(create_recipe_response.json)

        self.assertEqual(status_code,201)

    def test_update_recipe(self):
        signup_response = self.client.post(
            '/auth/signup', 
            json = {
                "username": "testuser", 
                "email": "testuser@tst.com", 
                "password": "password"
                }, 
            content_type='application/json')

        login_response = self.client.post(
            '/auth/login', 
            json = {
                "username": "testuser", 
                "password": "password"
                }, 
            content_type='application/json')

        access_token = login_response.json['access_token']


        create_recipe_response = self.client.post(
            '/recipe/recipes',
            json={
                "title": "Test Cookie",
                "description": "test description",
            },
            headers={
                'Authorization': 'Bearer {}'.format(access_token)
            }
        )

        id = 1

        update_recipe_response = self.client.put(
            f'/recipe/recipes/{id}',
            json={
            "title": "Updated Test Cookie",
            "description": "Updated description",
            },
            headers={
                "Authorization": 'Bearer {}'.format(access_token)
            }
        )

        #print(update_recipe_response.json)
        status_code = update_recipe_response.status_code
        self.assertEqual(status_code,200)

    def test_delete_recipe(self):
        signup_response = self.client.post(
            '/auth/signup', 
            json = {
                "username": "testuser", 
                "email": "testuser@tst.com", 
                "password": "password"
                }, 
            content_type='application/json')

        login_response = self.client.post(
            '/auth/login', 
            json = {
                "username": "testuser", 
                "password": "password"
                }, 
            content_type='application/json')

        access_token = login_response.json['access_token']


        create_recipe_response = self.client.post(
            '/recipe/recipes',
            json={
                "title": "Test Cookie",
                "description": "test description",
            },
            headers={
                'Authorization': 'Bearer {}'.format(access_token)
            }
        )

        id = 1
        delete_recipe_response = self.client.delete(
            f'/recipe/recipes/{id}',
            headers={
                "Authorization": 'Bearer {}'.format(access_token)
            }
        )

        status_code = delete_recipe_response.status_code
        self.assertEqual(status_code,200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()   


if __name__ == "__main__":
    unittest.main()

