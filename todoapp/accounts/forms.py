from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# from .models import UserImage


class AuthorCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model=User
        fields=['username','email','first_name', 'last_name']

      


class AuthorChange(UserChangeForm):
    class Meta:
        model=User
        fields=['username','email','first_name', 'last_name']