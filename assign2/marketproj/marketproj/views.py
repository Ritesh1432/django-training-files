# from django.urls import reverse
from django.shortcuts import render,redirect
from market import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate,login
from market.forms import RegisterForm,LoginForm


def homepage_view(request):
    return render(request,'base.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    form = RegisterForm()
    return render(request,'register.html',context={'form':form})


def login_view(request):
    errmessage = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        for user in models.User.objects.all():
            if user.username == username and user.password == password:
                request.session['username'] = username
                request.session['budget'] = user.budget
                return redirect('/')
            else:
                errmessage = 'Username or Password Invalid'
    loginForm = LoginForm()
    return render(request,'login.html',context = {'form':loginForm,'errmessage':errmessage})

def logout_view(request):
    del request.session['username']
    del request.session['budget']
    return redirect('/')