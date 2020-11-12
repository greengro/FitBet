from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateBet, CreateUserBet
from .models import Bet, UserBet

def create_bet(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CreateBet(request.POST)

        if form.is_valid():
            bet = form.save(commit=False)
            bet.bet_owner_user_id = request.user
            print('bet is ', bet)
            bet.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = CreateBet()

    return render(request, 'create_bet.html', {'form': form})


def create_userbet(request, bet_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CreateUserBet(request.POST)

        if form.is_valid():
            bet = form.save(commit=False)
            bet.user_id = request.user
            bet.bet_id = Bet.objects.get(pk=bet_id)
            print('bet is ', bet)
            bet.save()

            return HttpResponseRedirect('/dashboard')
    else:
        form = CreateUserBet()

    return render(request, 'create_userbet.html', {'form': form})
