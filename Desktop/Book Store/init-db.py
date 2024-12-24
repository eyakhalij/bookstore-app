import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create the 'books' table
conn.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    image TEXT
)
''')

# Insert sample data (optional)
books = [
    ('The Catcher in the Rye', 'J.D. Salinger', 10.99, 'A novel about teenage rebellion and alienation.', '/static/images/8125BDk3l9L.jpg'),
    ('1984', 'George Orwell', 14.99, 'A dystopian novel about totalitarianism.', '/static/images/61NAx5pd6XL.jpg'),
    ('To Kill a Mockingbird', 'Harper Lee', 12.99, 'A story about racial injustice and moral growth.', '/static/images/images.png')
]

conn.executemany('''
INSERT INTO books (title, author, price, description, image)
VALUES (?, ?, ?, ?, ?)
''', books)

# Commit and close the connection
conn.commit()
conn.close()

print("Database initialized and 'books' table created with sample data.")
