from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
	#if not request.user.is_authenticated:
	return render(request, "auction/index.html")

def login_view(request):
	#if submitting the form
	if request.method == 'POST':
		#get username submited
		username = request.POST["username"]
		#ger pass submited
		password = request.POST["password"]
		#authenticate it with django bult-in feature
		user_ok = authenticate(request, username=username, password=password)
		#if user is ok
		if user_ok:
			#login
			login(request, user_ok)
			#if redirect to index
			return HttpResponseRedirect(reverse('index'))
		else:
			#else keep it in login and display error 
			return render(request, "auction/login.html", {
				message: "Credenciales Invalidas"
				})	
	return render(request, "auction/login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register(request):
	pass