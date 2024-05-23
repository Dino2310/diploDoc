from django.shortcuts import render
from .models import *

def index(request):

    ad = 'Моедль выгруженна из рекламы'
    prod = 'Моедль выгруженна из товаров 4шт'

    content = {
        'prod' : prod,
        'ad' : ad
    }
    return render(request, 'shop/index.html', content)
