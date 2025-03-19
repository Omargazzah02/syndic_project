from django.urls import path
from .views import InterventionListCreateAPIView, ValidateInterventionAPIView

urlpatterns = [
    path("interventions/", InterventionListCreateAPIView.as_view(), name="intervention-list"),
    path("interventions/<int:pk>/validate/", ValidateInterventionAPIView.as_view(), name="validate-intervention"),
]
