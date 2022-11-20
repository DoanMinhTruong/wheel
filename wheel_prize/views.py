from json import load
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
# from symbol import yield_arg
# Create your views here.

from .models import *
def index(request):
    event = Event.objects.filter(status = 1).order_by("-id")[0]
    prize = EventPrize.objects.filter(event = event)
    template = loader.get_template('vongxoay.html')
    context = {
        'event' : event ,
        'prize' : prize
    }
    print(context['prize'][1].image)
    return HttpResponse(template.render(context , request))

# from dateutil.parser import parse
def getTimer(request):
    event = Event.objects.filter(status = 1).order_by("-id")[0]
    end = event._end
    return JsonResponse(
        {'end' : {
                'year' : end.year, 
                'month' : end.month,
                'day' : end.day,
                'hour' : end.hour,
                'minute' : end.minute,
                'second' : end.second,
            }
        }
    )
import random
@csrf_protect
def roll(request):
    if(request.method == 'POST'):
        uid = request.POST.get('uid')
        try:
            limit = Limit.objects.get(uid = uid)
        except:
            return JsonResponse({'uid' : 'invalid_uid'} , status = 404)
        if(limit.limit <= 0 ):
            return JsonResponse({'uid' : 'invalid_uid'} , status = 404)
        limit.limit -= 1
        limit.save()
        event = Event.objects.filter(status = 1).order_by("-id")[0]
        prizes = PrizeWinPercent.objects.all()
        list_prize = [([i.prize_number] * (int(i.percent)* 10)) for i in prizes]
        
        rand = (random.randint(0,len(list_prize) -1))
        result = list(set(list_prize[rand]))[0]
        prize = (request.POST.getlist('list_prize[]'))[result-1]
        log = PrizeLog(uid = uid , prize =  prize, event = event)
        log.save()
        return JsonResponse({'result' : result})

    return JsonResponse({'error' : 'Invalid Method'} , status = 500)

@csrf_protect
def turn_amount(request):
    if(request.method == "GET"):
        uid = request.GET.get('uid')
        try:
            limit = Limit.objects.get(uid = uid)
            return JsonResponse({'limit' : limit.limit , 'code' : 200} , status = 200)
        except:
            return JsonResponse({'code' : 404},status = 404)
    return JsonResponse({'code' : 500},status = 500)