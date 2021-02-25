from rest_framework import serializers
from .models import *

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topp
        fields = '__all__'