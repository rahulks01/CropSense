from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.http import HttpResponse
from .weather_service import fetch_weather_data

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            print('Invalid username or password')
    
    return render(request, 'login.html')

@login_required(login_url='login/') 
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
        crop_record = Record.objects.get(id = pk)
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_record.html', {'form':form , 'crop_record' : crop_record})
    else :
        return redirect('login')

def weather(request) :
    if request.user.is_authenticated:
        return render(request, 'weather.html', {})
    else :
        return redirect('login')

def recommend(request) :
    if request.user.is_authenticated:
        return render(request, 'recommend_crops.html')
    else :
        return redirect('login')

def recommend_crops(request, location):
    try:
        weather = fetch_weather_data(location)
    except ValueError as e:
        return HttpResponse(f"Error: {str(e)}", status=400)

    recommended_crops = Record.objects.filter(
        ideal_temperature_min__lte=weather.temperature,
        ideal_temperature_max__gte=weather.temperature,
        ideal_humidity_min__lte=weather.humidity,
        ideal_humidity_max__gte=weather.humidity,
        ideal_rainfall_min__lte=weather.rainfall,
        ideal_rainfall_max__gte=weather.rainfall,
    )

    context = {
        'location': location,
        'weather': weather,
        'recommended_crops': recommended_crops,
    }

    return render(request, 'recommendation.html', context)
