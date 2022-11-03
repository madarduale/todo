from django.contrib import admin
from .models import TodoApp,Profile
# Register your models here.
admin.site.register(TodoApp)
admin.site.register(Profile)

# admin.site.register(UserImage)