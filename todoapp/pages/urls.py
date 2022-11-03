from django.urls import path
from .views import HomeView,TodoAppCreateView,ViewTodo,TodoUpdateView,TodoDeleteView,UserImageCreateView,UserImageListView,UserImageEdit
from django.contrib.auth import  views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('<int:pk>/edit', TodoUpdateView.as_view(), name='todoupdate'),
    path('<int:pk>/delete', TodoDeleteView.as_view(), name='tododelete'),
    path('', HomeView.as_view(), name='home'),
    path('todolist/', ViewTodo.as_view(), name='todolist'),
    path('todocreate/', TodoAppCreateView.as_view(), name='todocreation'),
    path('userimageupload/', UserImageCreateView.as_view(), name='userimageupload'),
    path('userimageview/', UserImageListView.as_view(), name='userimageview'),
    path('userimage/<int:pk>/edit', UserImageEdit.as_view(), name='userimageedit'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)