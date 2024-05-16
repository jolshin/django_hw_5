# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

# Создать датчик (название и описание)
# POST {{baseUrl}}/sensors/

# Список датчиков (Ид, название, описнаие)
# GET {{baseUrl}}/sensors/

class SensorView(ListCreateAPIView):
    quaryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Изменить датчик (название и описание)
# PATCH {{baseUrl}}/sensors/1/

# Информация по конкретному датчику (Ид, название, описнаие, измерения)
# GET {{baseUrl}}/sensors/1/

class DetailSensorView(RetrieveUpdateAPIView):

    quaryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Добавить измерение (Ид датчика, температура)
# POST {{baseUrl}}/measurements/

class MeasurementView(CreateAPIView):
    
    quaryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
