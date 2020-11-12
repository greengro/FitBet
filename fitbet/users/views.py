from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from bets.models import Bet
from bets.forms import CreateUserBet

def home(request):
    return render(request, "users/home.html")


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
