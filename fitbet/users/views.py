from django.contrib.auth import login
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from bets.models import Bet
from bets.forms import CreateUserBet
from bets.models import UserBet

def home(request):
    return render(request, "users/home.html")

def profile(request):
    owned_bets = Bet.objects.filter(bet_owner_user_id=1)
    placed_bets = UserBet.objects.filter(user_id=1)
    queryset = Bet.objects.prefetch_related(Prefetch('bet_owner_user_id', queryset=UserBet.objects.filter(user_id=1)))
    return render(request, "users/profile.html", {'bets': owned_bets, 'placed': placed_bets, 'placed_desc': queryset})


def dashboard(request):
    all_bets = Bet.objects.all()
    form = CreateUserBet()
    return render(request, "users/dashboard.html", {'bets': all_bets, 'form': form})


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
