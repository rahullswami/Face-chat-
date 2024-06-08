from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from fail_App.models import *


# Create your views here.S
def index(request):
    queryset = Usersearch.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset= queryset.filter(messages_box__icontains = search)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def follow(request):
    return render(request, 'follow.html')

def media(request):
    return render(request, 'media.html')

def profile(request):
    return render(request, 'profile.html')

def requests(request):
    return render(request, 'request.html')

def setting(request):
    return render(request, 'setting.html')

def loginUser(request):
    if request.method == 'POST':
            # check if user has entered correct credentials 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'login.html')
    
    return render(request, 'login.html')    

def logoutuser(request):
    logout(request)
    return redirect('/login')

def Signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('ConfirmPassword')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please try a different one.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered. Please use a different email.')
            else:
                myuser = User.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password)
                )
                myuser.first_name = fullname
                myuser.save()
                messages.success(request, 'Your Face-Chat account has been successfully created!')
                return redirect('/')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    else:
        messages.error(request, 'Invalid request method. Please try again.')

    return render(request, 'login.html')
