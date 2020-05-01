from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html')

def password(request):

	charcters = ('abcdefghijklmnopqrstuvwxyz')
	upperchar = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	specialchar = ('@#$%&+*')
	num = ('123456789')

	if request.GET.get('uppercase'):
		charcters += upperchar

	if request.GET.get('special'):
		charcters += specialchar

	if request.GET.get('numbers'):
		charcters += num


	length = int(request.GET.get('length',6))

	password = ''
	for x in range(length):
		password += random.choice(charcters)

	return render(request,'generator/password.html', {'password':password})

def aboutpage(request):
	return render(request, 'generator/about.html')