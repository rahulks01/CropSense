from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

# @login_required(login_url='/login/') 
def home(request):
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request) 
    return redirect('login')  

def register_user(request) :
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "You Have Successfully Registered")
            return redirect('home')
    else :
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form})

    return render(request, 'register.html', {'form' : form})