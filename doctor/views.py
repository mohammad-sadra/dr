from django.shortcuts import render
from rest_framework.views import APIView as api
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import doctor, reserve
from .serializers import doctoradd, doctorget, reserveadd, reserveget


class getdata(api):

    def get(self, request):
        doctors = doctor.objects.all()
        serializer = doctoradd(doctors, many=True)
        return Response(serializer.data)