from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Residence(models.Model):
    name = models.CharField(max_length=25)  
    address = models.CharField(max_length=25)
    num_units = models.IntegerField()


class Property(models.Model):
    surface_area = models.IntegerField() 
    property_type = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    acquisition_date = models.DateTimeField()
    number_of_rooms = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_properties')
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='properties' )
