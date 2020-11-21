from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Bet, UserBet


class CreateBet(ModelForm):
    class Meta:
        model = Bet
        fields = ['title', 'description', 'steps_wagered']

    def clean_steps_wagered(self):
        steps = self.cleaned_data.get('steps_wagered', False)

        if steps <= 0:
            raise ValidationError("Non-positive number of steps")

        return steps

class CreateUserBet(ModelForm):
    class Meta:
        model = UserBet
        fields = ['amount_bet', 'betting_against']

    def clean_amount_bet(self):
        amount = self.cleaned_data.get('amount_bet', False)

        if amount <= 0:
            raise ValidationError("Non-positive number of steps")

        return amount

class UpdateBet(ModelForm):
    class Meta:
        model = Bet
        fields = ['achieved_goal']

