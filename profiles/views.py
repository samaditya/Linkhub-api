from django.shortcuts import render

# Create your views here.
# profiles/views.py

from rest_framework import viewsets
from .models import Profile, Link
from .serializers import ProfileSerializer, LinkSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer