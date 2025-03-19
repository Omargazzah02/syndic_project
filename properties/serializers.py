from rest_framework import serializers
from .models import Property

class PropretySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "surface_area", "property_type", "status", "address" ,"acquisition_date" , "number_of_rooms" , "owner"]
        read_only_fields = ["id", "surface_area", "property_type", "status", "address" ,"acquisition_date" , "number_of_rooms" , "owner"]
