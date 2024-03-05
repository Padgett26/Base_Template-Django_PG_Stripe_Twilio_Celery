from django.db import models

from account.models import Account


class Transaction(models.Model):
    payer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="new")
    order_id = models.CharField(max_length=40, blank=True, null=True)
    price_id = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.payer

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
