from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {}


class ExpenseAccountForm(forms.ModelForm):
    class Meta:
        model = ExpenseAndAssetAccount
        fields = '__all__'
        widgets = {}


class RevenueAccountForm(forms.ModelForm):
    class Meta:
        model = RevenueAccount
        fields = '__all__'
        widgets = {}
