from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,Service_category
from .forms import NewTopicForm,NewTopicForm2
from django.contrib.auth.decorators import login_required

def home(request):
	ser = Services.objects.all()
	return render(request,'service.html',{'services':ser})

def list_services(request, pk):
	ser = get_object_or_404(Services,pk=pk)
	li = ser.serces.order_by('-last_updated')
	return render(request,'list_service.html',{'list':li , 'service' :ser})

@login_required
def add_service(request):
	ser = Services.objects.all()
	user = User.objects.get()
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			return render(request,'service.html',{'services':ser}) 
	else:
		form = NewTopicForm()
	return render(request, 'new_service.html', {'services':ser , 'form' : form})


@login_required	
def list_services_new(request,pk):
	ser = get_object_or_404(Services,pk=pk)
	li = ser.serces.order_by('-last_updated')
	if request.method == 'POST':
		form = NewTopicForm2(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.service = ser
			new.save()
			return render(request,'list_service.html',{'list':li , 'service' :ser})
	else:
		form = NewTopicForm2()
	return render(request, 'new_list_services.html', {'form' : form})

def delete_main(request,pk):
	ser = get_object_or_404(Services,pk=pk)
	ser.delete()
	ser = Services.objects.all()
	return render(request,'service.html',{'services':ser})

