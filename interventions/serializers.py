from rest_framework import serializers
from .models import Intervention

class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ["id", "intervention_type", "user", "is_validated", "created_at"]
        read_only_fields = ["id", "user", "is_validated", "created_at"]
