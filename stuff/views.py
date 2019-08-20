from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Stuff, UserStuff
from .serializer import CategorySerializer, StuffSerializer, UserStuffSerializer
from user.models import User
from django.contrib.auth.models import User
from django.db import transaction


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True)
    def stuffs(self, request, *ars, **kwargs):
        category = self.get_object()
        serializer = StuffSerializer(category.stuffs.all(), many=True)
        return Response(serializer.data)

class StuffViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # /stuffs/purchase/
    # /stuffs/1/purchase/
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

    @action(detail=False, method=['POST'], url_path='purchase')
    @transaction.atomic()
    def purchase_stuffs(self, request, *args, **kwargs):
        user = request.user
        stuffs = request.data['stuffs']

        sid = transaction.savepoint()
        for i in stuffs:
            stuff = stuff.objects.get(id=i['item_id'])
            count = int(i['count'])

            if stuff.price * count > user.point:
                transaction.savepoint_rollback(sid)
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
            user.point -= stuff.price * count
            user.save()
            try:
                user_stuff = UserStuff.objects.get(user=user, stuff=stuff)
            except UserStuff.DoesNotExist:
                user_stuff = UserStuff(user=user, stuff=stuff)
            user_stuff.count += count
        transaction.savepoint_commit(sid)
        serializer = UserStuffSerializer(user.stuffs.all(), many=True)
        return Response(serializer.data)