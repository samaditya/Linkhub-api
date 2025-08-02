# profiles/serializers.py

from rest_framework import serializers
from .models import Profile, Link
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'url']

class ProfileSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'name', 'bio', 'links']