from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import *
from .forms import *

def products(request):
    filter = request.GET.get('filter')
    products=Product.objects.filter(status='open' if not filter else 'archived')
    products = products.filter(status ='archived') if filter else products
    return render(request,'products.html',{'products': products,'filter':filter})

def orders(request):
    return render(request,'orders.html',{})
def customers(request):
    return render(request,'customers.html',{})
def ed_materials(request):
    return render(request,'ed_materials.html',{})

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

