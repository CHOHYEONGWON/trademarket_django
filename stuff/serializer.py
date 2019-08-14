from rest_framework import serializers
from .models import Category, Stuff, UserStuff

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class StuffSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Stuff
        fields = ['id', 'name', 'description', 'category', 'category_id', 'image', 'price']

class UserStuffSerializer(serializers.ModelSerializer):
    stuff = StuffSerializer()

    class Meta:
        model = UserStuff
        fields = ['stuff', 'user', 'count']