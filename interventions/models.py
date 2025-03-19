from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Intervention(models.Model):
    INTERVENTION_CHOICES = [
        ("plumbing", "Plumbing"),
        ("electricity", "Electricity"),
        ("cleaning", "Cleaning"),
        ("security", "Security"),
    ]

    intervention_type = models.CharField(
        max_length=20, choices=INTERVENTION_CHOICES
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interventions"
    )
    is_validated = models.BooleanField(default=False)  # Special user validation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_intervention_type_display()}"
