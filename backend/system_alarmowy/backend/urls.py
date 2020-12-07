from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name="create_user"),
    path('login/', views.CustomObtainAuthToken.as_view()),
    path('alarmed_measurements', views.measurement_alarms),
    path('measurements', views.measurement_list),
    path('measurements/<int:pk>', views.measurement_details),
    path('recent/<int:location>', views.recent_measurement),
    path('dates/<str:start_time>/<str:end_time>', views.measurement_dates),
    path('alarms', views.alarm_list),
    path('alarms/<int:location>', views.alarm_details),
    # path('sensors', views.sensor_list),
    # path('sensors/<int:pk>', views.sensor_details),
]