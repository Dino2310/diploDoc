from django.shortcuts import render
from django_ajax.decorators import ajax
from django.db.models import Count, Sum, Avg, Max, Min

from ..models import*

def client(request):
    ord = Order.objects.filter(user = request.user).order_by('date')
    delivery = Delivery_address.objects.filter(user = request.user)

    contetn = {"ord":ord,
               "delivery":delivery}
    return render(request, 'shop/client.html', contetn)