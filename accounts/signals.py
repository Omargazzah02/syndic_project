from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, AdminProfile, OwnerProfile, ManagerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            AdminProfile.objects.create(user=instance)
        elif instance.role == 'owner':
            OwnerProfile.objects.create(user=instance)
        elif instance.role == 'manager':
            ManagerProfile.objects.create(user=instance)
