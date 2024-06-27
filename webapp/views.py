from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddRecordForm
from .models import Record


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
    records = Record.objects.all()
    return render(request, 'home.html', {'records' : records})

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

def crop_record(request, pk) :
    if request.user.is_authenticated :
        crop_record = Record.objects.get(id = pk)
        return render(request, 'record.html', {'crop_record' : crop_record})
    else :
        return redirect('login')

def delete_crop_record(request, pk) :
    if request.user.is_authenticated :
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        return redirect('home')
    else :
        return redirect('login')

def add_record(request) :
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                return redirect('home')
            
        return render(request, 'add_record.html', {'form':form})
    else :
        return redirect('login')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else :
        return redirect('login')

def weather(request) :
    if request.user.is_authenticated:
        return render(request, 'weather.html', {})
    else :
        return redirect('login')