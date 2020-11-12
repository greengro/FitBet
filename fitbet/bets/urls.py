from .views import create_bet, create_userbet
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("createBet/", create_bet, name="createBet"),
    path("createUserBet/<str:bet_id>", create_userbet, name="createUserBet"),
]