release: python manage.py collectstatic --no-input
web: gunicorn linkhub.wsgi --bind 0.0.0.0:$PORT