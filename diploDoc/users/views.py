from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from shop.models import *


def reservProduct_create(order, request):
    for prod in Product.objects.all():
        if (count := request.session.get(str(prod.id))): 
            if (buy := ReservProduct.objects.filter( order=order ).filter(product  = prod)):
                buy[0].quantity += count
            else:
                ReservProduct.objects.create( product = prod, quantity = count, price = prod.price, order = order ) 

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save()
        instance.is_stuff = False
        SubUser.objects.create(user=instance)
        if instance.is_staff:
            bye = [request.session.get(str(i), 0) for i in  dict([(i.id,0) for i in Product.objects.all()]).keys()]
        else:
            reservProduct_create(Order.objects.create(user_id = instance.id), request)   
           
    return redirect('shop:index')
    return render(request, 'register.html', {'form': form})





def log_in(request):
    valid_user = True
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                bye = [request.session.get(str(i), 0) for i in  dict([(i.id,0) for i in Product.objects.all()]).keys()]
            else:
                reservProduct_create( Order.objects.filter(user_id = user.id).get(status = 'created') or Order.objects.create(user_id = user.id, status = 'created' ), request)   
            return redirect('shop:index')
        valid_user = False
    form = LoginForm()
    return render(request, 'log_in.html', {'form': form, 'valid_user': valid_user})


def log_out(request):
    logout(request)
    return redirect('shop:index')
    return redirect('users:log_in')
