from django.contrib.auth import login
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from bets.models import Bet
from bets.forms import CreateUserBet
from bets.models import UserBet
from .models import Profile


def home(request):
    return render(request, "users/home.html")


def house(request):
    house_bets = Bet.objects.filter(bet_owner_user_id=1)
    form = CreateUserBet()
    return render(request, "users/houseBets.html", {'bets': house_bets, 'form': form})


def profile(request):
    active_owned_bets = Bet.objects.filter(bet_owner_user_id=request.user.id).filter(active=True)
    active_placed_bets = UserBet.objects.filter(user_id=request.user.id).filter(bet_id__active=True)
    success_bets = Bet.objects.filter(bet_owner_user_id=request.user.id).filter(active=False).filter(achieved_goal=True)
    steps = 0
    for obj in success_bets:
        steps += obj.steps_wagered
    # Should probably order this from newest to oldest
    finished_placed_bets = UserBet.objects.filter(user_id=request.user.id).filter(bet_id__active=False)
    user_info = Profile.objects.filter(user_id=request.user.id)
    return render(request, "users/profile.html", {'bets': active_owned_bets, 'placed': active_placed_bets,
                                                  "info": user_info, 'old_placed': finished_placed_bets,
                                                  'steps': steps})


def dashboard(request):
    all_active_bets = Bet.objects.all().filter(active=True)
    form = CreateUserBet()
    return render(request, "users/dashboard.html", {'bets': all_active_bets, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Welcome, {username}, your account was created! Please login now')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
