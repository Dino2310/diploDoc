from django.shortcuts import render
from django_ajax.decorators import ajax
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q
import requests, json
from ..models import*
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@ajax
def savelern(request):
    print("/"*10)
    print(request.POST)
    print(type(request.POST.get('title')))
    print(request.FILES)
    # print(request.read().get('title'))
    return {}