from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    license_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=20)
    latitude = models.CharField(max_length=10, null=True)
    longitude = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


