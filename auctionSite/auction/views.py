from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
	#if not request.user.is_authenticated:
	return render(request, "auction/index.html")

def login_view(request):
	pass

def logout_view(request):
	pass

def register(request):
	pass