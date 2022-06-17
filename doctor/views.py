from django.shortcuts import render
from rest_framework.views import APIView as api
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import doctor, reserve
from .serializers import doctoradd, doctorget, reserveadd, reserveget
from datetime import date



class getdata(api):

    def get_doctor(self, request):
        doctors = doctor.objects.all(reserve_date=1)
        serializer = doctoradd(doctors, many=True)
        return Response(serializer.data)


    def get_reserve(self, request):
        reserves = reserve.object.filter()