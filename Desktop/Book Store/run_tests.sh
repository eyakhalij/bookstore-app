#!/bin/bash

# Activate virtual environment (optional, if you're using one)
# source /full/path/to/venv/bin/activate

# Run Flask tests using Python's unittest with the full path to the tests directory
python -m unittest discover -s tests -p "test_flask_app.py"
