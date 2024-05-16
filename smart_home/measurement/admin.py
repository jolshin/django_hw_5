from django.contrib import admin

# Register your models here.

from .models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass