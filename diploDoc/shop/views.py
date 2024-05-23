from django.shortcuts import render
from .models import*

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.all()[:4]

    content = {
        'prod' : prod,
        'ad' : ad
    }
    return render(request, 'shop/index.html', content)
