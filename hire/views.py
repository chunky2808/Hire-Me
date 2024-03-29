from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,Service_category,Page
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from accounts.decorators import service_required,customer_required
from django.contrib.auth import get_user_model
from math import cos, asin, sqrt

User = get_user_model()

def home(request):
	ser = Services.objects.all()
	query = request.GET.get('search_box')
	if query:
		ser = Services.objects.filter(Q(name__icontains=query)| Q(category__icontains=query) |Q(last_updated__icontains=query))
	return render(request,'service.html',{'services':ser})

@login_required
def list_services(request, pk):
	ser = get_object_or_404(Services,pk=pk)
	li = ser.serces.order_by('-last_updated').values()
	print(request.user)
	if(request.user=='NONE'):
		print(hi)
	for li in li:
		lat = li['position'].latitude
		lon = li['position'].longitude
		dist = distance(float(lat),float(lon),float(request.user.position.latitude),float(request.user.position.longitude))#Haversine formula)
		dist = "%.3f" % dist
		Service_category.objects.filter(namee=li['namee']).update(distance=dist)
		print(dist)
	li = ser.serces.order_by('distance')
	return render(request,'list_service.html',{'list':li , 'service' :ser})


@login_required
@service_required
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
@service_required
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


@login_required
@customer_required
def review(request,pk,Service_category_pk):
	ser = get_object_or_404(Service_category,service__pk=pk,pk =Service_category_pk)
	er = Page.objects.filter(service_main=pk,service_cat=Service_category_pk)
	res = get_object_or_404(Services,pk=pk)
	print(ser.position)
	lat = (ser.position).latitude
	lon = (ser.position).longitude
	print(request.user.position.latitude)
	print(request.user.position.longitude)
	dist = distance(float(lat),float(lon),float(request.user.position.latitude),float(request.user.position.longitude))#Haversine formula)
	dist = "%.3f" % dist
	print(dist)
	return render(request,'review.html',{'service' : ser, 'revice' : res, 'review' : er, 'latitude' : lat , 'longitude' : lon, 'distance' : dist})


@csrf_exempt
@login_required
@customer_required
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
	return render(request,'main2.html')


def worker_page(request,pk):
	ser = get_object_or_404(Service_category,pk=pk)
	return render(request,'worker_page.html',{'service':ser})
	
def increment(request,pk,Service_category_pk):
	print("hi")
	ser = get_object_or_404(Service_category,service__pk=pk,pk =Service_category_pk)
	er = Page.objects.filter(service_main=pk,service_cat=Service_category_pk)
	res = get_object_or_404(Services,pk=pk)
	par = ser.upvotes
	par = par +1
	Service_category.objects.filter(namee=ser).update(upvotes = par)
	return render(request,'review.html',{'service' : ser, 'revice' : res, 'review' : er,})


def decrement(request,pk,Service_category_pk):
	ser = get_object_or_404(Service_category,service__pk=pk,pk =Service_category_pk)
	er = Page.objects.filter(service_main=pk,service_cat=Service_category_pk)
	res = get_object_or_404(Services,pk=pk)
	par = ser.downvotes
	par = par -1
	Service_category.objects.filter(namee=ser).update(downvotes = par)
	return render(request,'review.html',{'service' : ser, 'revice' : res, 'review' : er,})

# @csrf_exempt
# @login_required
# def model_form_upload(request):
#     if request.method == 'POST':
#         form = verifyform(request.POST, request.FILES)
#         if form.is_valid():
#             new = form.save(commit=False)
#             new.user = request.user
#             form.save()
#             return redirect('maiee')
#     else:
#         form = verifyform()
#     return render(request, 'model_form_upload.html', {
#         'form': form
#     })

def hello(request):
	# print(image_to_string(Image.open('/home/paras/Desktop/coding/my-project/Hire-Me!/Hire-Me/media/Details/None/123.png')))
	# print(image_to_string(Image.open('/home/paras/Desktop/coding/my-project/Hire-Me!/Hire-Me/media/Details/None/123.png'), lang='eng'))
	print("hi")


#calculate distance between user and service provider
def distance(lat1, lon1, lat2, lon2):#Haversine formula)
    p = 0.017453292519943295     
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))	

#calculate distance between user and service provider





