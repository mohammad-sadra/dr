from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import doctor, reserve
from .serializers import doctoradd, reserveadd, reserveget
# from .time import *
from datetime import date


@api_view(['GET'])
def get_doctor(request):
    doctors = doctor.objects.all()
    serializer = doctoradd(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_reserve_1(request):
    reserves = reserve.objects.filter(reserve_date=date.today(), doctor_reserve=1)
    serializers = reserveget(reserves, many=True)
    return Response(serializers.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_reserve_2(request):
    reserves = reserve.objects.filter(reserve_date=date.today(), doctor_reserve=2)
    serializers = reserveget(reserves, many=True)
    return Response(serializers.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def addreserve(request):
    serializer = reserveadd(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


