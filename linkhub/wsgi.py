# linkhub/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkhub.settings')

# Get the standard Django application
application = get_wsgi_application()

# Wrap it with WhiteNoise
application = WhiteNoise(application)