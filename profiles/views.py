from django.shortcuts import render

# Create your views here.
# profiles/views.py

from rest_framework import viewsets
from .models import Profile, Link
from .serializers import ProfileSerializer, LinkSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        # Automatically set the owner to the current logged-in user
        serializer.save(owner=self.request.user)

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer