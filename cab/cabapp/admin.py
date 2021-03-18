from django.contrib import admin
from .models import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['id', 'name', 'car_number', 'phone_number', 'license_number']


