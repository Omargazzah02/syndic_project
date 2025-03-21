from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('owner', 'Propriétaire'),
        ('manager', 'Gestionnaire'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')
    def save(self, *args, **kwargs):
      if self.pk is None or not self.password.startswith('pbkdf2_sha256$'):
        self.set_password(self.password)  # Hash automatiquement le mot de passe
        super().save(*args, **kwargs)



class OwnerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=255) 
    


class ManagerProfile(OwnerProfile):
    department = models.CharField(max_length=100)  
    


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    can_manage_users = models.BooleanField(default=True)
