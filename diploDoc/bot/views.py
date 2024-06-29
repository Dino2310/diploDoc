from django_ajax.decorators import ajax
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Q
import requests, json
from shop.models import*
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bot (request):
    answer = json.loads(request.read())
    url_home = "https://hagfish-star-strangely.ngrok-free.app/bot/"
    

    token = '7175352991:AAEsJ7VRKrzzsu6qy79kuSJkeVakLM2yrkE'


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
    return {'response':'200'}
