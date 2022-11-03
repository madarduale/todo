from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,UserPassesTestMixin,
    )
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from .forms import AuthorCreation
# from .models import UserImage
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class UserLogin(LoginView):
 
    template_name='registration/login.html'
    fields=['username','password']
    success_url=reverse_lazy('todolist')
    redirect_authenticated_user = True
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('todolist')
        return super(UserLogin,self).get(*args, **kwargs)

class SignUp(CreateView):
    form_class =AuthorCreation
    template_name='registration/signup.html'
    success_url=reverse_lazy('todolist')
     
    # def form_valid(self, form):
    #     user=form.save()
    #     if user is not None :
    #         login(self.request,user)
    #     return super(SignUp,self).form_valid(form)

    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('todolist')
        return super(SignUp,self).get(*args, **kwargs)
   



class EditUser( LoginRequiredMixin,UpdateView):
    model=User
    fields=['email','username','first_name','last_name']
    success_url=reverse_lazy('login')
    template_name='registration/edituser.html'

class DeleteUser(LoginRequiredMixin,DeleteView):
    model=User
    success_url=reverse_lazy('home')
    template_name='registration/deleteuser.html'

