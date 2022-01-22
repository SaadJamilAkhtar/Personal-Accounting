from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "credit", "debit", "total"]
        widgets = {}


class DebitAccountForm(forms.ModelForm):
    class Meta:
        model = DebitAccount
        fields = ["name", "credit", "debit", "total"]
        widgets = {}


class CreditAccountForm(forms.ModelForm):
    class Meta:
        model = CreditAccount
        fields = ["name", "credit", "debit", "total"]
        widgets = {}
