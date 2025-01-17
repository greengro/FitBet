from users.views import dashboard, register, home, profile, house, search
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("", home, name="home"),
    path("house/", house, name="house"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/<str:id>', profile, name='profile'),
    path('search/', search, name='search')
]