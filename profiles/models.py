from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
    
class Link(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='links')
    title=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return f'{self.title} | {self.url}'