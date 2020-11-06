from django.contrib import admin
from .models import Bet, UserBet

# Register your models here.
admin.site.register(Bet)
admin.site.register(UserBet)
