# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, AddMeasurementSerializer, MeasurementSerializer, \
    SensorDetailSerializer, AllSensorSerializer


class CreationSensorView(APIView):

    def get(self, request):  # список всех сенсоров
        sensors = Sensor.objects.all()
        serializer = AllSensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):  # добавление сенсора
        serializer = SensorSerializer(data=request.data)
        serializer.save()
        return Response(serializer.data)


class CreationMeasurementView(APIView):
    def post(self, request):  # добавление измерения
        serializer = AddMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class SensorDetail(APIView):
    def get(self, request, pk):  # подробная ин-фа по датчикам
        sensor = Sensor.objects.get(pk=pk)
        measurement = Measurement.objects.filter(sensor=pk)
        serializer = SensorDetailSerializer(sensor).data
        serializer['measurements'] = MeasurementSerializer(measurement, many=True).data
        return Response(serializer)

    def patch(self, request, pk):  # изменение датчика
        obj = Sensor.objects.get(pk=pk)
        serializer = SensorSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

