#!/bin/bash

# Activate virtual environment (optional, if you're using one)
# source venv/bin/activate

# Run Flask tests using Python's unittest
python -m unittest discover -s tests -p "test_flask_app.py"