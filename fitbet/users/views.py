from django.contrib.auth import login
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from bets.models import Bet
from bets.forms import CreateUserBet
from bets.models import UserBet
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, "users/home.html")


def house(request):
    house_id = User.objects.filter(username='HouseBets').first()
    house_bets = Bet.objects.filter(bet_owner_user_id=house_id)
    form = CreateUserBet()
    return render(request, "users/houseBets.html", {'bets': house_bets, 'form': form})


def profile(request, id):
    profile = Profile.objects.filter(user=id).first()
    owner = User.objects.get(pk=id)
    if request.method == 'POST':
        if(profile.points < 500):
            profile.points = 500
            profile.save()
            messages.success(request, f'Your points have been topped off!')
        else:
            messages.warning(request, f'You cannot top off if you have 500 or more points')

    active_owned_bets = Bet.objects.filter(bet_owner_user_id=id).filter(active=True).order_by('-date_created')
    active_placed_bets = UserBet.objects.filter(user_id=id).filter(bet_id__active=True).order_by('-bet_id__date_created')
    finished_placed_bets = UserBet.objects.filter(user_id=id).filter(bet_id__active=False).order_by('-bet_id__date_created')
    return render(request, "users/profile.html", {'bets': active_owned_bets, 'placed': active_placed_bets,
                                                  'info': profile, 'old_placed': finished_placed_bets,
                                                  'user_id': request.user.id, 'owner': owner})

def dashboard(request):
    all_active_bets = Bet.objects.all().filter(active=True).order_by('-date_created')
    # Filter so you can't bet on the same bet twice
    if(request.user.is_authenticated):
        for userBet in UserBet.objects.all().filter(user_id=request.user).filter(bet_id__active=True):
            all_active_bets = all_active_bets.exclude(id=userBet.bet_id.id)
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


def search(request):
    username = request.GET['u']
    user = None
    try:
        user = User.objects.get(username=username)
        id = user.id
        return redirect('profile', id)
    except ObjectDoesNotExist:
        messages.error(request, "That user does not exist! Please try searching again.")
    return redirect('dashboard')
