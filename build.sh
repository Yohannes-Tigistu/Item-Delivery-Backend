#!/bin/bash

# Install Pipenv if not already installed
/usr/bin/python3 -m pip install pipenv

# Create a virtual environment and install dependencies
/usr/bin/python3 -m pipenv install --deploy --ignore-pipfile

# Activate the virtual environment
source $(/usr/bin/python3 -m pipenv --venv)/bin/activate

# Run Django collectstatic (if needed)
python manage.py collectstatic --no-input

# Deactivate the virtual environment
deactivate
