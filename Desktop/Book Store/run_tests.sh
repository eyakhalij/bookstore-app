# filepath: /c:/Users/Eya/Desktop/Book Store/run_tests.sh
#!/bin/bash

# Set environment variables for the test database
export DB_NAME=test_bookstore

# Run the tests
python -m unittest discover -s tests -p "test*.py"