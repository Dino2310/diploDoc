from django.shortcuts import render
from django_ajax.decorators import ajax
from django.db.models import Count, Sum, Avg, Max, Min

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

def search (request):
    print(request.POST)
    return render(request, 'shop/search.html', {})

    


def learn(request):
    return render(request, 'shop/learn.html', {})

@ajax
def prod(request):
    c_id = request.GET.get('id')
    print(c_id)
    return {'res' : render(request, 'shop/prod.html', {'prod':Product.objects.filter(id = c_id)[0]})}

@ajax
def ajax_ansvwer(request):
    price_min, price_max = Product.objects.filter( quantity__gt = 0).aggregate(Min('price'), Max('price')).values()
    
    if request.GET.get('max'):
        filter_max = request.GET.get('max')
        filter_min = request.GET.get('min')
    else:
        filter_min, filter_max = price_min, price_max
    contetnt = {
        'change':{"max":filter_max, 'min':filter_min},
        'price': {"max":price_max,'min':price_min} 
    }

    return {"res" :render(request, 'shop/price.html', contetnt)}