from django import forms
from .models import *


class AccountForm(forms.Form):
    type_choices = [("Payable", "Payable"), ("Expense", "Expense"), ("Receivable", "Receivable"), ("Asset", "Asset")]
    name = forms.CharField(max_length=25, required=True)
    type = forms.ChoiceField(choices=type_choices)
    balance = forms.FloatField(min_value=0.0, initial=0.0, required=True)

