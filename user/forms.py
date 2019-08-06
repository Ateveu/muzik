from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.db import transaction


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MuzikUser
        fields = ('username', 'email')


class ArstistCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MuzikUser
        fields = ('username', 'email')

    def save(self):
        user = super().save(commit=False)
        user.is_artist = True
        user.save()
        artist = ArstistUser.objects.create(user=user)
        return artist

class NormalCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MuzikUser
        fields = ('username', 'email')

    def save(self):
        user = super().save(commit=False)
        user.is_normal = True
        user.save()
        normal = NormalUser.objects.create(user=user)
        return normal


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MuzikUser
        fields = ('username', 'email')