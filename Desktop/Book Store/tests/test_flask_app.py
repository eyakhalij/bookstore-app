import unittest
import os
from app import app
from pymongo import MongoClient

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Use absolute path for testing purposes
        current_directory = os.path.abspath(os.path.dirname(__file__))
        
        # Set the MongoDB URI (you may need to adjust this if you're using a remote database)
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client["bookstore"]
        self.books_collection = self.db["books"]

        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    # Test index route
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
