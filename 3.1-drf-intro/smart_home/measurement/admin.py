from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    pass