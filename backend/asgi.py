import os
from django.core.asgi import get_asgi_application
from uvicorn import Server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()

if __name__ == '__main__':
    server = Server(application)
    server.run()