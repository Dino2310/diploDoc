from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from shop.models import SubUser


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save()
        SubUser.objects.create(user=instance)
        return redirect('users:log_in')
    return render(request, 'register.html', {'form': form})


def log_in(request):
    valid_user = True
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:index')
        valid_user = False
    form = LoginForm()
    return render(request, 'log_in.html', {'form': form, 'valid_user': valid_user})


def log_out(request):
    logout(request)
    return redirect('users:log_in')
