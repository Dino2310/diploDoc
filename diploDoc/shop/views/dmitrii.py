from django.shortcuts import render
from django_ajax.decorators import ajax
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q

from ..models import*


cat_lib = {
    'all' : ['buttons','sensors', 'panels_management', 'controllers_management', 'rely'],
    'button':['buttons','sensors', 'panels_management'],
    'controller' : ['panels_management', 'controllers_management'],
    'relay' :['relay']
}

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
    result = request.GET
    price_min, price_max = list(map(int,Product.objects.filter( quantity__gt = 0).aggregate(Min('price'), Max('price')).values()))
    cinnects = ['Wi_Fi', 'TWI', "RS485"]
    if result.get('max'):
        filter_max = result.get('max')
        filter_min = result.get('min')
    else:
        filter_min, filter_max = price_min, price_max
    products = Product.objects.filter(Q(price__range = (filter_min, filter_max)) & Q(quantity__gt = 0))
    tmp = Product.objects.filter(Q(id =-1))

    # if result.get('type_dev'):
    #     answer =  cinnects if result.get('interface') is None else result.get('interface')
    #     filter_list = cat_lib.get(result.get('type_dev') or 'all') + answer
    #     for filter_cat in filter_list:
    #         tmp |= products.filter(Q(**{'categorical__'+filter_cat : True}))
    #     products = tmp

    if (answer := result.get('sort')):
        products = products.order_by(answer)
    if (answer := result.get('search')):
        
        products = products.filter(Q(**{'name__icontains':answer})|Q(**{'description__icontains':answer}))
    contetnt = {
        'change':{"max":filter_max, 'min':filter_min},
        'price': {"max":price_max,'min':price_min},
        'products' : products,
        'cinnects' : cinnects
    }
    return {"res" : render(request, 'shop/price.html', contetnt),
             'prod': render(request, 'shop/cat_prod.html', contetnt),
             'search': render( request, 'shop/sorted_and_search.html', contetnt)
            }

def count_prod(request):
    # if (user:= request.GET.get('user')):
    #     заказ = Order.objects.filter(user__id)
    #     prod = Products.objects.filter()
    #     pass
    # else:
    #     request.seesion[request.GET.get('id')] = 0
    count = 0
    return {'count' : count}