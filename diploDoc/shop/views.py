from django.shortcuts import render
from django_ajax.decorators import ajax

from .models import*

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.filter( quantity__gt = 0)
    
    content = {
        'ad' : ad,
        'lenAd':len(ad),
        'rAd':range(len(ad)),
        'prod':prod,
    }
    return render(request, 'shop/index.html', content)

def search(request):
    if request.method == "POST":
        print('yes')
        print(request.POST.get('search'))
    return index(request)

def category(request):
    prod = Product.objects.filter( quantity__gt = 0)
    content = {
        "prod":prod,
    }
    return render(request, 'shop/category.html', content)


def learn(request):
    return render(request, 'shop/learn.html', {})

def prod(request, c_id):

    return render(request, 'shop/prod.html', {'prod':Product.objects.filter(id = c_id)[0]})
