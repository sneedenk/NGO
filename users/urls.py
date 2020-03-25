from django.urls import path, include
from . import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', users_views.home, name='home-page'),
    path('register/', users_views.register, name='register-page'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    # format for adding admin exclusive views below
    path('check/', users_views.admin_view, name='checking'),
]
