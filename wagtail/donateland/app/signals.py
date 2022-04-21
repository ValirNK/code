from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import Transaction


@receiver(post_save, sender=Transaction)
def post_save_user(sender, instance, **kwargs):
    print('Действие отменено')