from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Intervention
from .serializers import InterventionSerializer
from .permissions import IsManager

class InterventionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all interventions (validated only)."""
        interventions = Intervention.objects.filter(is_validated=True)
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new intervention (User selects from predefined types)."""
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Attach the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ValidateInterventionAPIView(APIView):
    permission_classes = [IsAuthenticated ,IsManager]

    def patch(self, request, pk):
        """Special user validates an intervention."""
        try:
            intervention = Intervention.objects.get(pk=pk)
            if intervention.is_validated:
                return Response({"message": "Already validated"}, status=status.HTTP_400_BAD_REQUEST)

            intervention.is_validated = True
            intervention.save()
            return Response({"message": "Intervention validated successfully"}, status=status.HTTP_200_OK)

        except Intervention.DoesNotExist:
            return Response({"error": "Intervention not found"}, status=status.HTTP_404_NOT_FOUND)
