from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Bet(models.Model):
    # id = models.CharField(max_length=30) this is automatically provided
    bet_owner_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    steps_wagered = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    achieved_goal = models.BooleanField(default=False)


class UserBet(models.Model):
    # id = models.CharField(max_length=30) this is automatically provided
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bet_id = models.ForeignKey(Bet, on_delete=models.CASCADE)
    amount_bet = models.IntegerField()
    betting_against = models.BooleanField()
