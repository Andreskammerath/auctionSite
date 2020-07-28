from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Bienvenido a subastas Kammerath")

def login_view(request):
	pass

def logout_view(request):
	pass

def register(request):
	pass