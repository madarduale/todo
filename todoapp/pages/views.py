from django.contrib.auth.mixins import (
    LoginRequiredMixin,UserPassesTestMixin,
    )
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView
from django.views.generic.edit import CreateView ,DeleteView,UpdateView
# from .forms import AuthorCreation,LoginUser
from .models import TodoApp,Profile
# from .forms import UserImageForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "todoapp/home.html"





class TodoAppCreateView(LoginRequiredMixin,CreateView):
    model=TodoApp
    fields=['text','selection']
    # success_url=reverse_lazy('home')
    template_name='todoapp/todocreate.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class ViewTodo(LoginRequiredMixin,ListView):
    model=TodoApp
    template_name = "todoapp/viewtodo.html"
    ordering = ['-date']
    # paginate_by = 3
   
    def get_context_data(self,**kwargs):  # sourcery skip: use-named-expression
        context=super().get_context_data(**kwargs)
        context['object_list']=context['object_list'].filter(author=self.request.user)
        context['count']=context['object_list'].filter(author=False).count()
        

        search_input=self.request.GET.get('search_area') or ''
        if search_input:
            context['object_list']=context['object_list'].filter(text__icontains=search_input)
        return context
   

class TodoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=TodoApp
    fields=['text','complete','selection']
    success_url=reverse_lazy('todolist')
    template_name="todoapp/updatetodo.html"

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user




class TodoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=TodoApp
    success_url=reverse_lazy('todolist')
    template_name="todoapp/tododelete.html"
    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user



# class userimage(ListView):
#     model=Profile
#     template_name="todoapp/viewtodo.html"




class UserImageCreateView(LoginRequiredMixin,CreateView):
    model=Profile
    fields=['profile_image','bio']
    template_name='todoapp/userimage.html'
    success_url=reverse_lazy('todolist')

    def form_valid(self,form):
        form.instance.get_user=self.request.user
        return super().form_valid(form)

class UserImageListView(LoginRequiredMixin,ListView):
    model=Profile
    template_name='todoapp/userimageview.html'
    # context_object_name = 'userimages'
    # ordering = ['-id']
    # paginate_by = 1

class UserImageEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Profile
    fields=['profile_image','bio']
    template_name="todoapp/userimageedit.html"
    success_url=reverse_lazy('todolist')

    def test_func(self):
        obj=self.get_object()
        return obj.get_user==self.request.user

   