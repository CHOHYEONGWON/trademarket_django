from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Stuff, UserStuff
from .serializer import CategorySerializer, StuffSerializer, UserStuffSerializer
from user.models import User


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StuffViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['POST'])
    def purchase(self, request, *args, **kwargs):
        stuff = self.get_object()
        user = request.user
        if stuff.price > user.point:
            return Response(status= status.HTTP_402_PAYMENT_REQUIRED)
        user.point -= stuff.price
        user.save()
        try:
            user_stuff = UserStuff.objects.get(user=user, stuff=stuff)
        except UserStuff.DoesNotExist:
            user_stuff = UserStuff(user=user, stuff=stuff)
        user_stuff.count += 1
        user_stuff.save()

        serializer = UserStuffSerializer(user.stuffs.all(), many=True)
        return Response(serializer.data)