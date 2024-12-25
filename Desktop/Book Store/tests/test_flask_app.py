import unittest
from app import app
from pymongo import MongoClient
from bson.objectid import ObjectId

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

    # Test add book functionality
def test_add_book(self):
    new_book = {
        'title': 'New Book',
        'author': 'Author Name',
        'price': 20.99,
        'description': 'A new book description.',
        'image': '/static/images/book.jpg'
    }

    # Make sure we are sending data correctly in the form format
    response = self.app.post('/db/add', data=new_book, follow_redirects=True)

    # Check if the status code is 200 (or 302 if redirect)
    self.assertEqual(response.status_code, 200)  # It might be 200 after redirect

    # Ensure the new book appears on the homepage
    response = self.app.get('/')
    self.assertIn(b'New Book', response.data)  # Ensure the new book is added

    def test_edit_book(self):
        # Create and add a book first
        book = {
            'title': 'Book to Edit',
            'author': 'Author to Edit',
            'price': 25.99,
            'description': 'A book to be edited.',
            'image': '/static/images/edit_book.jpg'
        }
        self.books_collection.insert_one(book)

        # Get the book's ObjectId
        book_id = str(self.books_collection.find_one({'title': book['title']})['_id'])

        updated_book = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'price': 29.99,
            'description': 'Updated description.',
            'image': '/static/images/updated_book.jpg'
        }

        # Send the edit request
        response = self.app.post(f'/db/edit/{book_id}', data=updated_book)

        # Check for redirect
        self.assertEqual(response.status_code, 302)

        # Ensure the updated data is reflected in the database
        updated_book_in_db = self.books_collection.find_one({"_id": ObjectId(book_id)})
        self.assertEqual(updated_book_in_db['title'], updated_book['title'])
        self.assertEqual(updated_book_in_db['author'], updated_book['author'])

    # Test delete book functionality
    def test_delete_book(self):
        # Add a book to delete
        book = {
            'title': 'Book to Delete',
            'author': 'Author to Delete',
            'price': 30.99,
            'description': 'A book to be deleted.',
            'image': '/static/images/delete_book.jpg'
        }
        self.books_collection.insert_one(book)

        # Get the book's ObjectId
        book_id = str(self.books_collection.find_one({'title': book['title']})['_id'])

        # Send the delete request
        response = self.app.post(f'/db/delete/{book_id}')

        # Check for redirect and successful deletion
        self.assertEqual(response.status_code, 302)

        # Ensure the book is no longer in the database
        deleted_book = self.books_collection.find_one({"_id": ObjectId(book_id)})
        self.assertIsNone(deleted_book)

if __name__ == '__main__':
    unittest.main()
