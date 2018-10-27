''' URL configuration for users app'''
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name = 'login'), # login page
    path('logout/', LogoutView.as_view(next_page = 'learning_notes:index'), name = 'logout'), # logout page
    path('register/', views.register, name = 'register'), # registering a new user
]