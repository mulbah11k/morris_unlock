from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.email} - ${self.balance}"

class WalletTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type.upper()} - ${self.amount} for {self.wallet.user.email}"
