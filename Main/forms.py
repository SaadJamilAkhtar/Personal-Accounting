from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "credit", "debit", "total"]
        widgets = {}


class ExpenseAccountForm(forms.ModelForm):
    class Meta:
        model = ExpenseAndAssetAccount
        fields = ["name", "credit", "debit", "total"]
        widgets = {}


class RevenueAccountForm(forms.ModelForm):
    class Meta:
        model = RevenueAccount
        fields = ["name", "credit", "debit", "total"]
        widgets = {}
