from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base_framework/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'base_framework/signupuser.html', {'Form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'base_framework/signupuser.html',
                              {'Form': UserCreationForm(), 'error': 'this user name already used'})
        else:
            return render(request, 'base_framework/signupuser.html',
                          {'Form': UserCreationForm(), 'error': 'password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'base_framework/login.html', {'Form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'base_framework/login.html',
                          {'Form': AuthenticationForm(), 'error': 'Логин и пароль не совпадают'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        logout(request)
        return redirect('home')
