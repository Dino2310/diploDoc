from django_ajax.decorators import ajax
from django.shortcuts import render, redirect, HttpResponse
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
    url_bot = 'https://api.telegram.org/bot'
    answer = json.loads(request.read())
    url_home = "https://hagfish-star-strangely.ngrok-free.app/bot/"
    

    token = env("TOKEN_BOT")


    if 'message' in answer:
        name = answer.get('message').get('chat').get('first_name') # Тут выцепляются данные пользователя отправившего сообщение
        chat_id = answer.get('message').get('chat').get('id')
        mess_text = answer.get('message').get('text')  # Это текст самого сообщения
        mess = str(mess_text) +','+str(name) + ','+ str(chat_id)

    else:  
        mess_callb_data = answer.get("callback_query").get('data')
        chat_id = answer.get('callback_query').get('from').get('id')
        name =  answer.get('callback_query').get('from').get('first_name')
        mess = str(mess_callb_data)+','+str(name)+','+ str(chat_id)

    if mess_text == '/start':
        reply_markup = {'inline_keyboard': [
                            [{'text': 'Перейти за покупками', 'url': 't.me/ghghguihtuh_bot/elicta'},
                            {'text': 'Отправиться домой', 'callback_data': 'home'}]]}
        data = {'chat_id': chat_id, 'text': 'Привет, '+name , 'reply_markup': json.dumps(reply_markup)}
        requests.post(f'{url_bot}{token}/sendMessage', data=data)

    elif mess.startswith('btn'):
        r = requests.post(url_home, data=mess)
    elif mess.startswith('home'):
        r = requests.post(url_home, data=mess)
    if r.status_code != 200:
        mess = f"извините, но в данный момент Ваше устройсвто отключено или не имеет доступа в интрнет"
        chat  = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text= {mess}"
        requests.get(chat)

    return HttpResponse(status = 201)
    # return index(request)
    # return Response({"Status Code":'201'})
