from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "type", "total"]
        labels = {"total": "balance"}
