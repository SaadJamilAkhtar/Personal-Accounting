from django import forms
from .models import *


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
