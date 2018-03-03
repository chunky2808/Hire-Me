from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,Service_category

def home(request):
	ser = Services.objects.all()
	return render(request,'service.html',{'services':ser})

def list_services(request, pk):
	ser = get_object_or_404(Services,pk=pk)
	li = ser.serces.order_by('-last_updated')
	#li = get_object_or_404(Service_category,pk=pk)
	#print(pk)
	#print(li.name)
	return render(request,'list_service.html',{'list':li , 'service' :ser})
