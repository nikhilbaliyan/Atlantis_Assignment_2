from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'car_number', 'phone_number', 'license_number', 'email', 'latitude', 'longitude']
