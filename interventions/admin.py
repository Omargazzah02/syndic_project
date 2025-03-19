from django.contrib import admin
from .models import Intervention

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("user", "intervention_type", "is_validated", "created_at")
    list_filter = ("is_validated", "intervention_type")
    search_fields = ("user__username", "intervention_type")
