from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Services(models.Model):
	name = models.CharField(max_length = 40, unique =True)
	category = models.CharField(max_length = 40)
	last_updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Service_category(models.Model):
	namee = models.CharField(max_length = 100)
	desc = models.CharField(max_length = 500)
	price = models.CharField(max_length = 10)
	location = models.CharField(max_length = 50)
	service = models.ForeignKey(Services,related_name = 'serces')
	last_updated = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.namee
	

class Page(models.Model):
	Review = models.TextField(max_length = 4000)
	service = models.ForeignKey(Services,related_name = 'cer',default = False)
	service_cat = models.ForeignKey(Service_category,related_name = 'ser_cat',default = False)
	started_by = models.ForeignKey(User)

	def __str__(self):
		return self.Review

   