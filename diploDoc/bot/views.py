from django_ajax.decorators import ajax
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q
from shop.views import *
import requests, json
from shop.models import*
from environs import Env

from django.views.decorators.csrf import csrf_exempt

env: Env = Env()
env.read_env()


@csrf_exempt
def bot (request):
    answer = json.loads(request.read())
    url_home = "https://hagfish-star-strangely.ngrok-free.app/bot/"
    

    token = env("TOKEN_BOT")


    if 'message' in answer:
        mess_text_date = answer.get('message').get('chat').get('first_name') # Тут выцепляются данные пользователя отправившего сообщение
        chat_id = answer.get('message').get('chat').get('id')
        mess_text = answer.get('message').get('text')  # Это текст самого сообщения
        mess = str(mess_text) +','+str(mess_text_date) + ','+ str(chat_id)

    else:  
        mess_callb_data = answer.get("callback_query").get('data')
        chat_id = answer.get('callback_query').get('from').get('id')
        mess = str(mess_callb_data)+','+ str(chat_id)

    if mess.startswith('/start'):
        r = requests.post(url_home, data=mess)

    elif mess.startswith('btn'):
        r = requests.post(url_home, data=mess)
    if r.status_code != 200:
        mess = f"извините, но в данный момент Ваше устройсвто отключено или не имеет доступа в интрнет"
        chat  = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text= {mess}"
        requests.get(chat)

    return index(request)
    # return Response({"Status Code":'201'})
