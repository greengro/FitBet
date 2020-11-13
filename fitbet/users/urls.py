from users.views import dashboard, register, home, profile
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("", home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile')
]