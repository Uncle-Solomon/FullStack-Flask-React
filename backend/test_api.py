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
        hello_response = self.client.get('/recipe/hello_world')

        json = jsonify(hello_response)

        self.assertEqual(json, {"message":"Hello World"})


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()   


if __name__ == "__main__":
    unittest.main()

