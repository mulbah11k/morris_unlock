from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wallet
from accounts.models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
