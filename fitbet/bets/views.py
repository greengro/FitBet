from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import CreateBet, CreateUserBet, UpdateBet
from .models import Bet, UserBet
from users.models import Profile
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
        profile = Profile.objects.filter(user=request.user).first()
        form.setPoints(profile.points)

        if form.is_valid():
            bet = form.save(commit=False)
            bet.user_id = request.user
            bet.bet_id = Bet.objects.get(pk=bet_id)
            profile = Profile.objects.filter(user=request.user).first()
            profile.points -= bet.amount_bet
            bet.save()
            print('bet is ', bet)
            profile.save()
            print('profile')
            return HttpResponseRedirect('/dashboard')
    else:
        form = CreateUserBet()

    return render(request, 'create_userbet.html', {'form': form, 'bet_id': bet_id})

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
            # Save information about bet
            bet = form.save(commit=False)
            bet.active = False
            bet.save()
            print('bet is updated')
            # Update steps on user's profile
            if(bet.achieved_goal):
                profile = Profile.objects.filter(user=request.user).first()
                profile.steps += bet.steps_wagered
                profile.save()
                print('profile is updated')
            # Update points for bet participants
            for userBet in UserBet.objects.filter(bet_id=bet_instance):
                payout = calculatePayout(userBet, bet)
                userBet.payout = payout
                userBet.save()
                profile = Profile.objects.get(user=userBet.user_id)
                profile.points += payout
                profile.save()

            return HttpResponseRedirect('/profile/' + str(request.user.id))
    else:
        form = UpdateBet(instance=bet_instance)

    bet = Bet.objects.get(pk=id)
    return render(request, 'update_bet.html', {'form': form, 'bet': bet})

def calculatePayout(userBet, bet_instance):
    potWon = 0
    potLost = 0
    for tempUserBet in UserBet.objects.filter(bet_id=bet_instance):
        if(bet_instance.achieved_goal != tempUserBet.betting_against):
            potWon += tempUserBet.amount_bet
        else: potLost += tempUserBet.amount_bet
    payoutRatio = potLost / potWon
    if(bet_instance.achieved_goal != userBet.betting_against):
    #   print(str(userBet.user_id) + " won the bet")
        return int(userBet.amount_bet * (1 + payoutRatio))
    else:
    #   print(str(userBet.user_id) + " lost the bet")
        return 0