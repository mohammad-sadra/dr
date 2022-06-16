from django.contrib import admin
from .models import doctor, reserve


@admin.register(doctor)
class doctor(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name']


@admin.register(reserve)
class reserve(admin.ModelAdmin):
    list_display = ['name', 'phone', 'doctor_reserve']
    search_fields = ['name']
