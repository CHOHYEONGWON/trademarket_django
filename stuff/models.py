from django.db import models
from user.models import User
import random

class Category(models.Model):
    title = models.CharField(max_length=100)

def get_stuff_image_path(instance, filename):
    filename = str(random.randint(10000, 100000)) + filename
    path = 'stuff_images/%s' % (filename)
    return path

class Stuff(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=get_stuff_image_path, null=True)
    category = models.ForeignKey(Category, related_name='stuffs', on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

class UserStuff(models.Model):
    user = models.ForeignKey(User, related_name='stuffs', on_delete=models.CASCADE)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

