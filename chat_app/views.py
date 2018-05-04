from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from hire.models import Service_category


def chat(request,stri_id):
	print(stri_id)	
	ser = Service_category.objects.filter(handle=stri_id)
	print(ser)
	for ser in ser:
		handle = ser.handle
	return render(request, 'index.html',{'handle':'handle'})

def chatbox(request,stri_id):
	ser = Service_category.objects.filter(handle=stri_id)
	for ser in ser:
		handle = ser.handle
	if request.method != 'POST':
		return render(request, 'index.html',{'handle':'handle'})
	else:
		name = request.POST.get('name')
		return render(request, 'chat.html', {'name':name})