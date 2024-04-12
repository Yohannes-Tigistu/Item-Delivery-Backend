#!/usr/bin/env python

import os

# Install Pipenv if not already installed
os.system("pip install pipenv")

# Create a virtual environment and install dependencies
os.system("pipenv install --deploy --ignore-pipfile")

# Activate the virtual environment
os.system("pipenv shell")

# Run Django collectstatic (if needed)
os.system("python manage.py collectstatic --no-input")

# Deactivate the virtual environment
os.system("exit")
