from django.shortcuts import render
from django_ajax.decorators import ajax
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q
import requests, json
from ..models import*
from django.views.decorators.csrf import csrf_exempt

import struct



@csrf_exempt
@ajax
def savelern(request):
    answer = request.POST.get
    learn = Education.objects.create(
        word = answer('slug'),
          image = request.FILES.get('title'),
            name = answer('name'),
              attributes = answer('attributes'),
                slug = answer('slug'))
    
    for index, type_in in enumerate(answer('list').split(',')):
        print(index, type_in )
        if type_in == 'text':
            ContetnLearn.objects.create(
                text = answer(str(index)),
                  education = learn , 
                  queue = index)
            
        elif type_in == 'img':
            ContetnLearn.objects.create(
                image = request.FILES.get(str(index)),
                  education = learn ,
                    queue = index)
    return {}