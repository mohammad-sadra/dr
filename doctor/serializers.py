from rest_framework import serializers
from .models import doctor, reserve


class doctoradd(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('name', 'type', 'day')


class reserveadd(serializers.ModelSerializer):
    class Meta:
        model = reserve
        fields = ('reserve_date', 'reserve_time')


class doctorget(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('name')


class reserveget(serializers.ModelSerializer):
    class Meta:
        model = reserve
        fields = ('name', 'phone', 'price', 'pay', 'info')
