from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,Service_category,Page
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
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
	user = User.objects.first()
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


def review(request,pk,Service_category_pk):
	ser = get_object_or_404(Service_category,service__pk=pk,pk =Service_category_pk)
	er = Page.objects.filter(service_main=pk,service_cat=Service_category_pk)
	res = get_object_or_404(Services,pk=pk)
	print(er)
	return render(request,'review.html',{'service' : ser, 'revice' : res, 'review' : er,})

@login_required
def review_new(request,pk,Service_category_pk):
	ser = get_object_or_404(Service_category,service__pk=pk,pk =Service_category_pk)
	er = Page.objects.filter(service_main=pk,service_cat=Service_category_pk)
	res = get_object_or_404(Services,pk=pk)
	if request.method == 'POST':
		form = NewTopicForm3(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.started_by = request.user
			new.service_main = res
			new.service_cat = ser
			new.save()
			return render(request,'review.html',{'service' : ser, 'revice' : res, 'review' : er,})
	else:
		form = NewTopicForm3()
	return render(request, 'new_list_services.html', {'form' : form})



def mainee(request):
	return render(request,'main.html')


def worker_page(request,pk):
	ser = get_object_or_404(Service_category,pk=pk)
	return render(request,'worker_page.html',{'service':ser})
	




# def home(request):
# 	return render(request,'main.html')