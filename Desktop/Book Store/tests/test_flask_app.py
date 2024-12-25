import unittest
from app import app  # Assuming your Flask app is defined in `app.py`
from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

class FlaskTestCase(unittest.TestCase):
    # Ensure the app is set up correctly
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Set up MongoDB client and select test database
        os.environ['DB_NAME'] = 'test_bookstore'  # Use a test database
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client["test_bookstore"]
        self.books_collection = self.db["books"]

        # Insert a sample book for testing
        self.sample_book_id = self.books_collection.insert_one({
            "title": "Sample Book",
            "author": "Author Name",
            "published_date": "2023-01-01"
        }).inserted_id

    # Clean up after each test
    def tearDown(self):
        self.books_collection.delete_many({})

    # Test index route
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Test create book
    def test_create_book(self):
        response = self.app.post('/db/add', data={
            "title": "New Book",
            "author": "New Author",
            "price": 20.99,
            "description": "A new book description",
            "image": "static/images/new_book.jpg"
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code

    # Test read book
    def test_read_book(self):
        response = self.app.get(f'/db/book/{self.sample_book_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Book', response.get_data(as_text=True))

    # Test update book
    def test_update_book(self):
        response = self.app.post(f'/db/edit/{self.sample_book_id}', data={
            "title": "Updated Book",
            "author": "Updated Author",
            "price": 29.99,
            "description": "An updated book description",
            "image": "static/images/updated_book.jpg"
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code

    # Test delete book
    def test_delete_book(self):
        response = self.app.post(f'/db/delete/{self.sample_book_id}')
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertIsNone(self.books_collection.find_one({"_id": ObjectId(self.sample_book_id)}))

if __name__ == '__main__':
    unittest.main()