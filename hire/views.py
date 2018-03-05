from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,Service_category
from .forms import NewTopicForm

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


def add_service(request):
	ser = Services.objects.all()
	user = User.objects.first()
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			#new.name = name
            # new.category = category
			new.save()
            # topic.save()
			return render(request,'service.html',{'services':ser})  # TODO: redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'new_service.html', {'services':ser , 'form' : form})
	

