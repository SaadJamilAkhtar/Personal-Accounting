from django.db import models


class Account(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=True)
    credit = models.FloatField(default=0.0)
    debit = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ExpenseAndAssetAccount(Account):
    def balanceAccount(self):
        self.total = self.debit - self.credit
        if self.total > 0:
            self.debit = self.total
        else:
            self.total = abs(self.total)
            self.credit = self.total


class RevenueAccount(Account):
    def balanceAccount(self):
        self.total = self.credit - self.debit
        if self.total > 0:
            self.credit = self.total
        else:
            self.total = abs(self.total)
            self.debit = self.total
