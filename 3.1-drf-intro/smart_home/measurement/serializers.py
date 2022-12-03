from rest_framework import serializers

from measurement.models import Measurement, Sensor


# TODO: опишите необходимые сериализат  оры
class SensorSerializer(serializers.ModelSerializer):  # создание и изменение датчика
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class AllSensorSerializer(serializers.ModelSerializer):  # вывод списка всех датчиков
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class AddMeasurementSerializer(serializers.ModelSerializer):  # Добавление измерения
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):  # подробное описание датчика
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']