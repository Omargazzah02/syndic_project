from django.db import models
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()





 

class Property(models.Model):
    surface_area = models.IntegerField() 
    property_type = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    acquisition_date  = models.DateTimeField()
    number_of_rooms   = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')







