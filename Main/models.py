from django.contrib.auth.models import AbstractUser
from django.db import models


class AccuUser(AbstractUser):
    accounts = models.ManyToManyField('Account')
    entries = models.ManyToManyField("Entry")


class Account(models.Model):
    type_choices = [("Payable", "Payable"), ("Expense", "Expense"), ("Receivable", "Receivable"), ("Asset", "Asset")]
    name = models.CharField(null=False, blank=False, max_length=255, unique=False)
    total = models.FloatField(default=0.0)
    entries = models.ManyToManyField("Entry")
    type = models.CharField(max_length=25, choices=type_choices, default=type_choices[3][1])

    def updateBalance(self, balance: float, update: str):
        if self.type in ["Receivable", "Asset", "Expense"]:
            if update == "db":
                self.total += balance
            else:
                self.total -= balance
        else:
            if update == 'db':
                self.total -= balance
            else:
                self.credit += balance

    def __str__(self):
        return self.name


class Entry(models.Model):
    date = models.DateField(auto_now_add=True)
    details = models.CharField(max_length=255)
    credit = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True, related_name="credit_acc")
    debit = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True, related_name="debit_acc")
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.date) + " | " + str(self.amount) + " | " + str(self.details)

    class Meta:
        verbose_name_plural = "Entries"
