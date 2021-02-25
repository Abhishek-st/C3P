from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from django_mysql.models import ListTextField

from .models import *
from .myserializers import *
# Create your views here.

class GetPizzas(APIView):
    def get(self, request):
        try:
            data = Pizza.objects.all()
            ser = PizzaSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })
    

class CreatePizzas(APIView):
    def post(self,request):
        typ = request.data['types']
        if typ == 'Regular' or typ=='Square':
            serializer = PizzaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'type can be either Regular or Square, case sensitive'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrDelete(APIView):
    def patch(self, request, pk, format=None):
        id = pk
        piz = Pizza.objects.get(name=id)
        serializer = PizzaSerializer(piz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        piz = Pizza.objects.get(name=id)
        piz.delete()
        return Response({'msg':'Data Deleted'})

class FilterPizza(APIView):
    def post(self, request):
        data = request.data
        try:
            if 'size' in data.keys() and 'type' in data.keys():
                data = Pizza.objects.filter(size=data['size'], types=data['type'])
                ser = PizzaSerializer(data, many=True)
                return Response(ser.data)
            elif 'size' in data.keys():
                data = Pizza.objects.filter(size=data['size'])
                ser = PizzaSerializer(data, many=True)
                return Response(ser.data)
            elif 'type' in data.keys():
                data = Pizza.objects.filter(types=data['type'])
                ser = PizzaSerializer(data, many=True)
                return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })


class AddSize(APIView):
    def post(self,request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddTopping(APIView):
    def post(self,request):

        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSize(APIView):
    def get(self, request):
        try:
            data = Size.objects.all()
            ser = SizeSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })

class GetTopping(APIView):
    def get(self, request):
        try:
            data = Topp.objects.all()
            ser = ToppingSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })