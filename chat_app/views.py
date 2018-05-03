from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def chat(request):	
	return render(request, 'index.html')

def chatbox(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse('index'))
	else:
		name = request.POST.get('name')
		return render(request, 'chat.html', {'name':name})