from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morris_unlocker.settings')
application = get_wsgi_application()

def handler(request):
    # Route requests to Django's WSGI application
    response = application(request)
    return HttpResponse(response.content, status=response.status_code)
