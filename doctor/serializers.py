from rest_framework import serializers
from .models import doctor, reserve


class doctoradd(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('name', 'type', 'day')


class reserveadd(serializers.ModelSerializer):
    class Meta:
        model = reserve
        fields = ('name')
        #, 'phone', 'doctor_reserve', 'reserve_time', 'reserve_date', 'price', 'pay', 'info'


class doctor_check(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('name')


class reserveget(serializers.ModelSerializer):
    class Meta:
        model = reserve
        fields = ('name', 'phone', 'price', 'pay', 'info', 'reserve_time')
