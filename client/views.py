from .models import ClientLogs
from rest_framework import viewsets, status
from .serializers import ClientLogsSerializers, UserSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class ClientViewsSet(viewsets.ModelViewSet):
    queryset=ClientLogs.objects.all()
    serializer_class=ClientLogsSerializers
    # permission_classes=[permissions.AllowAny]
    permission_classes=[IsAuthenticated]
    # automaticaly associate the record with the authenticated user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #  only return client records created by the authenticated user
    def get_queryset(self):
        return ClientLogs.objects.filter(user=self.request.user)

class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
