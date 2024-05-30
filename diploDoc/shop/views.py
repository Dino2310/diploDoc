from django.shortcuts import render
from django_ajax.decorators import ajax

from .models import*

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.all()[:4]

    content = {
        'prod' : prod,
        'ad' : ad
    }
    return render(request, 'shop/index.html', content)

def category(request):
    cat = Categorical.objects.all()
    return render(request, 'shop/category.html',{"cat":cat})

@ajax
def cat_filter(request):
    tmp = Categorical.__doc__.split(',')
    if request.method == "POST":
        res = request.POST
        answer = True
        for i in tmp:
            if res[i] == 'ON':
                answer &= Categorical.objects.filter(i=True)
        return {'filter': answer }

        

