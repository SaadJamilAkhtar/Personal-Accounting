from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model= Account
        fields = ["type", "name", "total"]
        labels = {"total": "balance"}

