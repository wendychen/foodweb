#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context	= {}
	context['food'] = 'Foodsharing!'
	return render(request, 'hello.html', context)

