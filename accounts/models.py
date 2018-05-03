from django.contrib.auth.models import AbstractUser
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    position = GeopositionField(null=True)
    aadhar_no = models.IntegerField(unique=True,null=True)
    aadhar_file = models.FileField(upload_to='Details/',null=True)
  
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	

class Service(models.Model):
	user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
