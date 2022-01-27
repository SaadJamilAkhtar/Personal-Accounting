from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.contrib.auth.forms import UserCreationForm


# add image field in registration form

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    currency = forms.CharField(max_length=5)
    email = forms.EmailField()
    pass1 = forms.CharField(label="Password", widget=forms.PasswordInput(), required=False)
    pass2 = forms.CharField(label="Retype Password", widget=forms.PasswordInput(), required=False)
    profile = forms.ImageField(required=False)


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "type", "total"]
        labels = {"total": "balance"}


class EntryForm(forms.Form):
    def __init__(self, user: AccuUser, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        if user:
            accounts = user.accounts.all()
            self.acc_choices = [(acc.id, acc.name) for acc in accounts]
            self.fields["entry"] = forms.CharField(max_length=255, required=True)
            self.fields["credit"] = forms.ChoiceField(choices=self.acc_choices, required=True)
            self.fields["debit"] = forms.ChoiceField(choices=self.acc_choices, required=True)
            self.fields["amount"] = forms.FloatField(initial=0.0, required=True)
