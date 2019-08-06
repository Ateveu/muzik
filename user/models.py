from django.contrib.auth.models import AbstractUser
from django.db import models


class MuzikUser(AbstractUser):
    is_artist = models.BooleanField(default=False)
    is_orzanizer = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=False)
    bio = models.TextField(default="Hello")

class NormalUser(models.Model):
    user = models.OneToOneField(MuzikUser, on_delete=models.CASCADE, primary_key=True)
    attended_events = models.TextField(default='')


class ArstistUser(models.Model):
    user = models.OneToOneField(MuzikUser, on_delete=models.CASCADE, primary_key=True)
    genre = models.CharField(max_length = 30)

