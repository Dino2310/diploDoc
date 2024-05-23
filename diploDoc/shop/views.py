from django.shortcuts import render
<<<<<<< HEAD
from .models import*

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.all()[:4]
=======
from .models import *

def index(request):

    ad = 'Моедль выгруженна из рекламы'
    prod = 'Моедль выгруженна из товаров 4шт'
>>>>>>> b68cdf655362cc333c3045fa9cb7a0eb0bac9809

    content = {
        'prod' : prod,
        'ad' : ad
    }
<<<<<<< HEAD
    return render(request, 'shop/index.html', content)
=======
    return render(request, 'shop/index.html', content)
>>>>>>> b68cdf655362cc333c3045fa9cb7a0eb0bac9809
