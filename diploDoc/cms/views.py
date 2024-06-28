from django.shortcuts import render,redirect
from django.http import HttpResponse
<<<<<<< HEAD
from shop.models import *
from shop.forms import *
=======

from .forms import ProductForm
from shop.models import Product

>>>>>>> origin/Aleksandr

def products(request):
    filter = request.GET.get('filter')
    products=Product.objects.filter(status='open' if not filter else 'archived')
    products = products.filter(status ='archived') if filter else products
    return render(request,'products.html',{'products': products,'filter':filter})

def orders(request):
    ord = Order.objects.all()
    return render(request,'orders.html',{'ord':ord})
def customers(request):
    user = User.objects.all()
    return render(request,'customers.html',{'user':user})
def ed_materials(request):
    meterials = Education.objects.all()
    return render(request,'ed_materials.html',{'meterials':meterials})

def add_product(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cms:products')
    return render(request, 'product_form.html',{'form': form})

def edit_product(request,pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None,request.FILES or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('cms:products')
    return render(request, 'product_form.html', {'form': form})

def archive_product(request,pk):
    product= Product.objects.get(pk=pk)
    if product.status =='open':
        product.status = 'archived'
    else:
        product.status ='open'
    product.save()
    return redirect('cms:products')

