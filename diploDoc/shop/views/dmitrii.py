from django.shortcuts import render
from django_ajax.decorators import ajax
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q

from ..models import*


cat_lib = {
    'all' : ['buttons','sensors', 'panels_management', 'controllers_management', 'relay'],
    'button':['buttons','sensors', 'panels_management'],
    'controller' : ['panels_management', 'controllers_management'],
    'relay' :['relay']
}

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.filter( quantity__gt = 0)
    count = dict([(i.id,0) for i in Product.objects.all()])
    if (request.user != "AnonymousUser"):
        заказ = Order.objects.filter(Q(user__username = request.user) & Q(status = 'assembling'))
        if заказ:
            for i in ReservProduct.objects.filter(order = заказ[0]):
                count[i.id] = i.quantity
    
    content = {
        'ad' : ad,
        'lenAd':len(ad),
        'rAd':range(len(ad)),
        'prod':prod,
        'count' : count
    }
    return render(request, 'shop/index.html', content)

def search(request):
    if request.method == "POST":
        return index(request)


def category(request):
    prod = Product.objects.filter( quantity__gt = 0)
    content = {
        "prod":prod,
    }
    return render(request, 'shop/category.html', content)

def search (request):
    answer = request.POST.get('search')
    products = Product.objects.filter(Q(**{'name__icontains':answer})|Q(**{'description__icontains':answer}))
    ''' тут ещё добавиьт поиск по обучяющим материалам'''
    contetnt = {'products':products}
    return render(request, 'shop/search.html', contetnt)

    


def learn(request):
    return render(request, 'shop/learn.html', {})

@ajax
def prod(request):
    c_id = request.GET.get('id')
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

    prod = dict([(i.id,0) for i in Product.objects.all()])
    if (request.user != "AnonymousUser"):
        заказ = Order.objects.filter(Q(user__username = request.user) & Q(status = 'assembling'))
        if заказ:
            for i in ReservProduct.objects.filter(order = заказ[0]):
                prod[i.id] = i.quantity

    

    if result.get('type_dev'):
        answer = tmp if (tmp := result.get('interface').split(','))[0] else cinnects
        filter_list = cat_lib.get(result.get('type_dev') or 'all')
        tmp = Product.objects.filter(Q(id =-1))
        for filter_cat in filter_list:
            tmp |= products.filter(Q(**{'categorical__'+filter_cat : True}))
        products = tmp
        tmp = Product.objects.filter(Q(id =-1))
        for filter_cat in answer:
            tmp |= products.filter(Q(**{'categorical__'+filter_cat : True}))
        products = tmp

    if (answer := result.get('sort')):
        products = products.order_by(answer)
    if (answer := result.get('search')):
        products = products.filter(Q(**{'name__icontains':answer})|Q(**{'description__icontains':answer}))
    contetnt = {
        'change':{"max":filter_max, 'min':filter_min},
        'price': {"max":price_max,'min':price_min},
        'products' : products,
        'cinnects' : cinnects,
        'count' : prod
    }
    return {"res" : render(request, 'shop/price.html', contetnt),
             'prod': render(request, 'shop/cat_prod.html', contetnt),
             'search': render( request, 'shop/sorted_and_search.html', contetnt)
            }
@ajax
def count_prod(request):
    if request.GET.get('fn')=='fn':
        заказ = Order.objects.filter(Q(user__username = request.GET.get('user')) & Q(status = 'assembling'))[0]
        if not заказ:
            заказ = Order.objects.create(user = User.objects.get(username = request.GET.get('user')))
        ReservProduct.objects.create(product = Product.objects.filter(id = request.GET.get('id'))[0], price = Product.objects.filter(id = request.GET.get('id'))[0].price, order = заказ)  

    count = 0
    if (user := request.GET.get('user')):
        заказ = Order.objects.filter(Q(user__username = user) & Q(status = 'assembling'))[0]
        # if заказ:
        #     заказ = Order.objects.create(user = user)
        prod = ReservProduct.objects.filter(Q(order = заказ)& Q(id = request.GET.get('id')))

        if(prod):
            count = prod[0].quantity
            if request.GET.get('fn') == "1":
                prod.update( quantity = (count := count+1))
            else:
                prod.update( quantity = (count := count-1))

                

    # else:
    #     request.seesion[request.GET.get('id')] = 0
    return {'count' : count}