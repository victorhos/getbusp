#-*- coding:utf-8 -*-


import json
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context, loader
from sptrans import SPTransClient

CLIENT = SPTransClient()

def home(request):

    template = '%shome.html' %settings.TEMPLATE_DIRS

    return render_to_response(template)

def auth_sptrans(request):

    res = CLIENT.auth()

    if res:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)

def buscar_bus(request):
    CLIENT.auth()

    try:
        term = request.GET['term']
    except:
        term = None

    res = CLIENT.search_by_bus(term=term)

    return HttpResponse(json.dumps(res), content_type='application/json')

def paradas_bus(request):
    CLIENT.auth()

    try:
        uid = request.GET['term']
    except:
        uid = None

    res = CLIENT.search_stops_by_bus(uid)

    return HttpResponse(json.dumps(res), content_type='application/json')
