from django.urls import path
from .views import UserLogin,SignUp,EditUser,DeleteUser
from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('login/', UserLogin.as_view() , name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:pk>/edit', EditUser.as_view(), name='edituser'),
    path('<int:pk>/delete', DeleteUser.as_view(), name='deleteuser'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name="password_change"),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/passwordchangedone.html'),name="password_change_done"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/passwordresetform.html'),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'),name="password_reset_complete"),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)