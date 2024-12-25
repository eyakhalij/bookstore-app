from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__, static_folder="static")

# ---------------------------
# MongoDB Connection
# ---------------------------
try:
    # Get the MongoDB URI and database name from environment variables
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    db_name = os.getenv('DB_NAME', 'bookstore')
    client = MongoClient(mongo_uri)
    db = client[db_name]
    books_collection = db["books"]

    # Ensure sample data is loaded (only for initial setup)
    if books_collection.count_documents({}) == 0:
        books_collection.insert_many([
            {
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "price": 10.99,
                "description": "A novel about teenage rebellion and alienation.",
                "image": "static/images/61NAx5pd6XL.jpg"
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "price": 14.99,
                "description": "A dystopian novel about totalitarianism.",
                "image": "static/images/8125BDk3l9L.jpg"
            },
            {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "price": 12.99,
                "description": "A story about racial injustice and moral growth.",
                "image": "static/images/images.png"
            }
        ])
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# ---------------------------
# Routes for MongoDB-Based Books
# ---------------------------

@app.route('/')
def db_index():
    """Home route: Displays all books from MongoDB."""
    books = list(books_collection.find())
    for book in books:
        book["_id"] = str(book["_id"])  # Convert ObjectId to string for rendering
    return render_template('index_db.html', books=books)

@app.route('/db/add', methods=['GET', 'POST'])
def db_add():
    """Route to add a new book to MongoDB."""
    if request.method == 'POST':
        try:
            new_book = {
                "title": request.form.get('title'),
                "author": request.form.get('author'),
                "price": float(request.form.get('price')),
                "description": request.form.get('description'),
                "image": request.form.get('image')
            }

            # Check if the book already exists in the collection
            existing_book = books_collection.find_one({
                "title": new_book["title"],
                "author": new_book["author"]
            })
            
            if (existing_book):
                return f"Book '{new_book['title']}' by {new_book['author']} already exists.", 400

            books_collection.insert_one(new_book)
        except Exception as e:
            return f"Error adding book: {e}", 500
        return redirect(url_for('db_index'))  # Redirect after adding
    
    return render_template('add_db.html')  # If GET request, render the add form

@app.route('/db/edit/<string:id>', methods=('GET', 'POST'))
def db_edit(id):
    """Route to edit an existing book in MongoDB."""
    book = books_collection.find_one({"_id": ObjectId(id)})

    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        updated_book = {
            "title": request.form.get('title'),
            "author": request.form.get('author'),
            "price": float(request.form.get('price')),
            "description": request.form.get('description'),
            "image": request.form.get('image'),
        }
        books_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_book})
        return redirect(url_for('db_index'))

    return render_template('edit_db.html', book=book)

@app.route('/db/delete/<string:id>', methods=('POST',))
def db_delete(id):
    """Route to delete a book from MongoDB."""
    try:
        books_collection.delete_one({"_id": ObjectId(id)})
    except Exception as e:
        return f"Error deleting book: {e}", 500
    return redirect(url_for('db_index'))

@app.route('/db/book/<string:id>')
def db_book_details(id):
    """Route to display book details from MongoDB."""
    try:
        # Retrieve the book by ObjectId
        book = books_collection.find_one({"_id": ObjectId(id)})
        if not book:
            return "Book not found", 404

        # Convert ObjectId to string for rendering
        book["_id"] = str(book["_id"])
    except Exception as e:
        return f"Error fetching book details: {e}", 500

    return render_template('book_db.html', book=book)

# ---------------------------
# Debugging Route
# ---------------------------
@app.route('/debug')
def debug():
    """Debug route for testing."""
    return app.send_static_file('images/8125BDk3l9L.jpg')

# ---------------------------
# Run the App
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))