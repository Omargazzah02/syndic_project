from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsManager  


User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data["username"])
        response.data["role"] = user.role  # Ajouter le rôle dans la réponse
        return response


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Accès autorisé", "user": request.user.username})






class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]  # Seuls les managers ont accès

    def get(self, request):
        return Response({"message": "Bienvenue, Manager !"}, status=200)









    