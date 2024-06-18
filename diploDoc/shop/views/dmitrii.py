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
    if (request.user.is_authenticated):
        заказ = Order.objects.filter(Q(user__username = request.user) & Q(status = 'assembling'))
        if заказ:
            for i in ReservProduct.objects.filter(order = заказ[0]):
                count[i.product.id] = i.quantity
    else:
        for key in count.keys():
            count[key] = request.session.get(str(key),0)
    
    
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
    counter = 0
    if request.user.is_authenticated:
        заказ = Order.objects.filter(Q(user__username = request.user) & Q(status = 'assembling'))
        if заказ:
            for i in ReservProduct.objects.filter(order = заказ[0]):
                counter = i.quantity
    else:
        counter = request.session.get(str(request.GET.get(c_id)),0)
    
    contetn = {
        'prod': Product.objects.filter(id = c_id)[0],
        "counter": counter

    }
    return {'res' : render(request, 'shop/poduct.html', contetn)}

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
    if request.user.is_authenticated:
        заказ = Order.objects.filter(Q(user__username = request.user) & Q(status = 'assembling'))
        if заказ:
            for i in ReservProduct.objects.filter(order = заказ[0]):
                prod[i.product.id] = i.quantity
    else:
        for key in prod.keys():
            prod[key] = request.session.get(str(key),0)

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
    count = 0
    if  not request.user.is_authenticated:

        if not request.session.get(product := request.GET.get('id')):
            request.session[product] = 1
        if ((answer :=request.GET['fn']) == '1'):
            request.session[product] += 1
        elif answer == '0':
            request.session[product] -= 1
        
        count = request.session[product]

    else: 
        product = Product.objects.get(id = request.GET.get('id'))
        orders = Order.objects.filter(Q(user = request.user) & Q(status = 'assembling'))
        if len(orders) == 0:
            ord = Order.objects.create(user = request.user)
            ord.save()
        elif len(orders) == 1: ord = orders[0]
        else: pass #дописать проверку если заказов больше одного. надо будет всё подулаять и присовокупить их между собой
        products = ReservProduct.objects.filter(Q(order = ord) & Q(product = product))
        if request.GET.get('fn')=='fn':
            
            if len(products)==0:
                
                products = ReservProduct.objects.create(order = ord, product = product, price = product.price)
                products.save()
        
        elif len(products):
            count = products[0].quantity
            if request.GET.get('fn') == '1':
                products.update( quantity = (count := count+1))
            else:
                products.update( quantity = (count := count-1))
                if count == 0: 
                    products.delete()
                    if not len(ReservProduct.objects.filter(order = ord)):
                        ord.delete()
        else:
            pass

 
    return {'count' : count}