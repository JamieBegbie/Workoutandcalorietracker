from django.shortcuts import redirect,render
import webbrowser
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signup(request):	
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('login:home')
	else:
		form = UserCreationForm()
	return render(request, "nextcloudLogin/signup.html",{'form':form})

	permission = Permission.objects.get(
		codename='access_privilege'
	)
def signin(request):
	if request.method== 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			username = user.username
			password = user.password
			return redirect('access:home')

	else:
		form = AuthenticationForm()
	return render(request, "nextcloudLogin/signin.html", {'form':form})

def signout(request):
	if request.method=='POST':
		logout(request)
		messages.success(request, "Successfully logged out")
		return redirect('login:home')