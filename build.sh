echo "Building Project packages..."
python3 -m pip install -r requirements.txt

python3 manage.py collectstatic -noinput