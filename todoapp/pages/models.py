from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import  get_user_model
from django.urls import reverse
# Create your models here.

class TodoApp(models.Model):
    text=models.CharField(max_length=100)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    # image=models.ImageField(blank=True,upload_to='images')
    select='select one'
    one='Highpriority'
    two='Normal'
    three='Not sure'
    selection_choices=[(one,'Highpriority'),(two,'Normal'),(three,'Not sure'),( select,'select one')]
   
    selection=models.CharField(max_length=100,choices=selection_choices,default=select)

    


    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('todolist')

# class UserImage(models.Model):
#     image=models.ImageField(blank=True,upload_to='images')
#     def get_absolute_url(self):
#         return reverse('todolist')



class Profile(models.Model):
    get_user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True)
    bio=models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.get_user.username