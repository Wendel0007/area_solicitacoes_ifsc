import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_interno_ifsc.settings')
load_dotenv()
application = get_wsgi_application()
