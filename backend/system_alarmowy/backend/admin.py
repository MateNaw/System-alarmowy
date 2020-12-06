from django.contrib import admin
from .models import Measurement
# Register your models here.

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['time', 'localization', 'temperature', 'gas', 'windows', 'alarm',  'id']
    ordering = ['time', 'localization','id']
    