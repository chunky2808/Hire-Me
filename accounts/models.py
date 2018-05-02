from django.contrib.auth.models import AbstractUser
from geoposition.fields import GeopositionField
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    position = GeopositionField(null=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	

class Service(models.Model):
	user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  
