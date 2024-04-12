#!/bin/bash

# Specify Python version
PYTHON_VERSION="python3.9"

# Install dependencies
${PYTHON_VERSION} -m pip install -r requirements.txt

# Collect static files
${PYTHON_VERSION} manage.py collectstatic
