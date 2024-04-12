#!/bin/bash

# Activate virtual environment if present
if [ -d "/vercel/path0/.venv" ]; then
    source /vercel/path0/.venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input
