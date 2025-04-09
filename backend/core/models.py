from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Author(models.Model):
    name = models.CharField(max_length=100)

class Narrator(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Chapter(models.Model):
    audiobook = models.ForeignKey(Audiobook, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='chapters/')
    order = models.PositiveIntegerField()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audiobook = models.ForeignKey(Audiobook, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, null=True, blank=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.CASCADE)