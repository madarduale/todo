from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

# class UserImage(AbstractUser):
#     image=models.ImageField(default='media/owl.jpg',blank=True,upload_to='images')


# class Profile(models.Model):
#     user=models.OneToOneField(User,  on_delete=models.CASCADE)
#     profile_image = models.ImageField( blank=True, upload_to='static/images/profile/')
#     bio=models.CharField(max_length=225)

#     def __str__(self):
#         return self.user.username