from django.db import models
from user.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)

class Stuff(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/stuff_image/', null= True)
    category = models.ForeignKey(Category, related_name='stuffs', on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

class UserStuff(models.Model):
    user = models.ForeignKey(User, related_name='stuffs', on_delete=models.CASCADE)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

