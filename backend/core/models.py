from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# USER MODEL (Extending Django's Built-in User)
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# AUTHOR, NARRATOR & PUBLISHER MODELS
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Narrator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# AUDIOBOOK MODEL
class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    total_time = models.CharField(max_length=50, blank=True, null=True)
    total_number_of_listening = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# BOOK CHAPTER MODEL
class Chapter(models.Model):
    audiobook = models.ForeignKey(Audiobook, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='chapters/')
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"Chapter {self.order}: {self.title}"

# FAVORITE MODEL (Combining previous Favorite relations into one)
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audiobook = models.ForeignKey(Audiobook, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, null=True, blank=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.audiobook.title if self.audiobook else self.author.name if self.author else self.narrator.name if self.narrator else self.publisher.name}"
