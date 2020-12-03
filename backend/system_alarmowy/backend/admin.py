from django.contrib import admin
from .models import Measurement, Sensor
# Register your models here.

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'id', 'measured_value', 'time']
    ordering = ['sensor', 'time','id', 'measured_value']
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor_type', 'location']
    ordering = ['id', 'sensor_type', 'location']