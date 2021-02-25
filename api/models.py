from django.db import models
from django_mysql.models import ListTextField
# Create your models here.


class Topp(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Size(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Pizza(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    types = models.CharField(max_length=30)
    size =  models.ForeignKey(Size, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topp)

    

