from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import doctor, reserve
from .serializers import doctoradd, reserveget
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
    name = request.data.get('name')
    phone = request.data.get('phone')
    dr = request.data.get('dr')
    rd = request.data.get('rd')
    rt = request.data.get('rt')
    price = request.data.get('price')
    pay = request.data.get('pay')
    info = request.data.get('info')
    try :
        check = reserve.objects.get(phone=phone, doctor_reserve=dr, reserve_date=rd)
        return HttpResponse('user is found', status=status.HTTP_406_NOT_ACCEPTABLE)

    except:
        reserve.objects.create(name=name, phone=phone, reserve_date=rd, doctor_reserve=dr, reserve_time=rt, price=price,
                               pay=pay, info=info)
        return HttpResponse('ok', status=status.HTTP_201_CREATED)






