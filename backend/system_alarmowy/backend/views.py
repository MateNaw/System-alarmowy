from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from .models import Measurement, Alarm
from .serializers import MeasurementSerializer, CustomUserSerializer, AlarmSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Avg, Max, Min, Sum
from os import system
from datetime import datetime
import socket
from rest_framework import generics


# Create your views here.

class CustomUserCreate(APIView):

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=request.data["email"]).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            if user:
                json = serializer.data
                token, created = Token.objects.get_or_create(user=user)
                json["token"] = token
                return Response(data={
            'token': token.key,
            'user_id': user.pk,
            'email': user.email}
        ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(pk=token.user_id)
        return Response({'token': token.key, 'id': token.user_id, 'is_admin': user.is_superuser})

@api_view(['GET', 'POST'])
def measurement_list(request):
    if request.method == 'GET':
        data = Measurement.objects.all()
        serializer = MeasurementSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MeasurementSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'DELETE'])
def measurement_details(request, pk):
    try:
        data = Measurement.objects.filter(pk=pk)
    except Measurement.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = MeasurementSerializer(data)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'DELETE'])
def recent_measurement(request, location):
    try:
        data = Measurement.objects.filter(location=location)
        try:
            data = sorted(data, key= lambda x : x.time, reverse=True)
            data = data[0]
        except IndexError:
            data = []
    except Measurement.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = MeasurementSerializer(data)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)

@api_view(['GET',])
def measurement_dates(request, start_time, end_time):
    if request.method == 'GET':
        data = Measurement.objects.all().filter(time__gte=start_time).filter(time__lte=end_time)
        serializer = MeasurementSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def alarm_list(request):
    if request.method == 'GET':
        data = Alarm.objects.all()
        serializer =AlarmSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlarmSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET',])
def alarm_details(request, location):
    if request.method == 'GET':
        data = Alarm.objects.filter(location=location)
        serializer = AlarmSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)