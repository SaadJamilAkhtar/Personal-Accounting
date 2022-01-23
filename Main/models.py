from django.contrib.auth.models import AbstractUser
from django.db import models


class AccuUser(AbstractUser):
    accounts = models.ManyToManyField('Account')
    entries = models.ManyToManyField("Entry")


class Account(models.Model):
    type_choices = [("Payable", "Payable"), ("Expense", "Expense"), ("Receivable", "Receivable"), ("Asset", "Asset")]
    name = models.CharField(null=False, blank=False, max_length=255, unique=True)
    credit = models.FloatField(default=0.0)
    debit = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    entries = models.ManyToManyField("Entry")
    type = models.CharField(max_length=25, choices=type_choices, default=type_choices[3][1])

    def __str__(self):
        return self.name


# class DebitAccount(Account):
#     def balanceAccount(self):
#         self.total = self.debit - self.credit
#         if self.total > 0:
#             self.debit = self.total
#         else:
#             self.total = abs(self.total)
#             self.credit = self.total
#
#
# class CreditAccount(Account):
#     def balanceAccount(self):
#         self.total = self.credit - self.debit
#         if self.total > 0:
#             self.credit = self.total
#         else:
#             self.total = abs(self.total)
#             self.debit = self.total


class Entry(models.Model):
    type_choices = [("C", "Credit"), ("D", "Debit")]
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=type_choices)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.date) + " | " + str(self.amount) + " | " + str(self.type)

    class Meta:
        verbose_name_plural = "Entries"
