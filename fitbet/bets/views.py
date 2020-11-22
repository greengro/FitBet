from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import CreateBet, CreateUserBet, UpdateBet
from .models import Bet, UserBet
from django.contrib.auth.decorators import login_required



@login_required
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

@login_required
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

@login_required
def delete_bet(request, id):
    bet = Bet.objects.get(pk=id)
    bet.delete()
    print('bet is deleted')
    return HttpResponseRedirect('/profile')

@login_required
def update_bet(request, id):
    # if this is a POST request we need to process the form data
    bet_instance = Bet.objects.get(pk=id)
    if request.method == 'POST':
        form = UpdateBet(request.POST,instance=bet_instance)

        if form.is_valid():
            bet = form.save(commit=False)
            bet.active = False
            print('bet is updated')
            bet.save()
            return HttpResponseRedirect('/profile/' + id)
    else:
        form = UpdateBet(instance=bet_instance)

    bet = Bet.objects.get(pk=id)
    return render(request, 'update_bet.html', {'form': form, 'bet': bet})