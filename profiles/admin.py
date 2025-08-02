from django.contrib import admin

# Register your models here.
# profiles/admin.py
from .models import Profile, Link

admin.site.register(Profile)
admin.site.register(Link)