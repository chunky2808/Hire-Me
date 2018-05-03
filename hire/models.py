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
	Address = models.CharField(max_length = 200)
	location = models.CharField(max_length = 50)
	service = models.ForeignKey(Services,related_name = 'serces')
	last_updated = models.DateTimeField(auto_now_add=True)
	position = GeopositionField(null=True)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default =0)
	distance = models.DecimalField(default=0.0,max_digits=25, decimal_places=3)
	pref_time =  models.CharField(max_length = 50,null=True)
	handle = models.CharField(max_length = 50,default='',null=True,unique=True)
	
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

