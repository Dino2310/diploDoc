from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import *
from shop.forms import *
from .forms import ProductForm,StatusForm


def products(request):
    filter = request.GET.get('filter')
    products = Product.objects.filter(status='open' if not filter else 'archived')
    products = products.filter(status='archived') if filter else products
    for product in products:
        if product.quantity==0:
            product.status='archived'
            product.save()

    return render(request, 'products.html', {'products': products, 'filter': filter})



def orders(request):
    ord = Order.objects.all()
    return render(request, 'orders.html', {'ord': ord})


def customers(request):
    users = SubUser.objects.all()
    return render(request, 'customers.html', {'users': users})


def ed_materials(request):
    meterials = Education.objects.all()
    return render(request, 'ed_materials.html', {'meterials': meterials})


def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    cat_form = CatForm(request.POST or None)

    if form.is_valid():
        add_prod = CatForm(dict([(elem, True) for elem in set(cat_form.fields)&set(request.POST)])).save(commit=False)
        add_prod.prod = form.save()
        add_prod.save()

        return redirect('cms:products')
    return render(request, 'product_form.html', {'form': form, 'cat_form':cat_form})


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('cms:products')
    return render(request, 'product_form.html', {'form': form})


def archive_product(request, pk):
    product = Product.objects.get(pk=pk)
    if product.status == 'open':
        product.status = 'archived'
    else:
        product.status = 'open'
    product.save()
    return redirect('cms:products')
def add_education_material(request):
    return render(request,'add_education_material.html')
def status_edit(request,pk):
    product = Product.objects.get(pk=pk)
    form = StatusForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        isinstance.status  = request.POST('status')
        instance.save()
        return redirect('cms:orders')
    return  render(request,'status_edit.html',{'form':form})