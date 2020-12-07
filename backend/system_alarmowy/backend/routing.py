
from django.urls import re_path

from . import channel

websocket_urlpatterns = [
    re_path('socket/', channel.MeasurementConsumer.as_asgi()),
]