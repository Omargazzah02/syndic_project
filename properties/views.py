# views.py
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Property
from .serializers import PropretySerializer

class UserPropretiesListAPIView(ListAPIView):
    serializer_class = PropretySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)
