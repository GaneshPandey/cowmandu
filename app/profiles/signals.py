from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import CustomerProfile, ManagerProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'customer':
            customer_profile = CustomerProfile(user=instance)
            customer_profile.save()
        elif instance.role == 'manager':
            manager_profile = ManagerProfile(user=instance)
            manager_profile.save()
