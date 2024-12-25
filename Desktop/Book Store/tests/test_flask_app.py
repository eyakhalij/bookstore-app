import unittest
from app import app
from pymongo import MongoClient

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client["bookstore"]
        self.books_collection = self.db["books"]

    # Test index route
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
