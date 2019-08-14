
from rest_framework import viewsets, generics, permissions
from .models import User
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from stuff.serializer import UserStuffSerializer

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class MyStuffView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserStuffSerializer(request.user.stuffs.all(), many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

