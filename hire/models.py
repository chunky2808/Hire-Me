from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from src import settings


class Services(models.Model):
	name = models.CharField(max_length = 40, unique =True)
	category = models.CharField(max_length = 40)
	last_updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Service_category(models.Model):
	namee = models.CharField(max_length = 100,unique=True)
	desc = models.CharField(max_length = 150)
	price = models.CharField(max_length = 10)
	Address = models.CharField(max_length = 200,default = '')
	location = models.CharField(max_length = 50)
	service = models.ForeignKey(Services,related_name = 'serces')
	last_updated = models.DateTimeField(auto_now_add=True)
	position = GeopositionField(null=True)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default =0)
	
	def __str__(self):
		return self.namee


class Page(models.Model):
	Review = models.TextField(max_length = 4000)
	service_cat = models.ForeignKey(Service_category,related_name = 'ser_cat',default = False)
	service_main = models.ForeignKey(Services,related_name = 'ser_main',default = False)
	started_by = models.ForeignKey(settings.AUTH_USER_MODEL)
	last_updated = models.DateTimeField(auto_now_add=True)
	helpful = models.IntegerField(default = 0)
	unhelpful = models.IntegerField(default = 0)

	def __str__(self):
		return self.Review

class verify(models.Model):
	user = 	models.ForeignKey(settings.AUTH_USER_MODEL)
	print(user.name)
	aadhar = models.FileField(upload_to='Details/%s/' % user.name)
	uploaded_at = models.DateTimeField(auto_now_add=True)
