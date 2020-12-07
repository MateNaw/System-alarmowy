from django.contrib import admin
from .models import Measurement, Alarm
# Register your models here.

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['time', 'location', 'temperature', 'gas', 'windows', 'alarm',  'id']
    ordering = ['time', 'location','id']
    
@admin.register(Alarm)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['time', 'location', 'id']
    ordering = ['time', 'location', 'id']
    