from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializers


# Create your views here.
@api_view(["GET"])
def getCars(request):
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCar(request, pk):
    cars = Car.objects.get(id=pk)
    serializer = CarSerializers(cars, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createCar():
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def updateCar():
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteCar():
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def contact():
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)
