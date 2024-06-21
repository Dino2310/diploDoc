from django.shortcuts import render
from django_ajax.decorators import ajax
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q

from ..models import*

def detail (request, slug = 0):
    learn = Education.objects.get(slug = slug)
    trainingMaterial = ContetnLearn.objects.filter(education = learn).order_by('queue')
    contetn = {"learn":learn, "trainingMaterial": trainingMaterial}
    print(contetn)
    return render(request, 'shop/detail.html', contetn )