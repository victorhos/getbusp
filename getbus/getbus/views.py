#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context, loader
from sptrans import SPTransClient

def home(request):

    template = '%shome.html' %settings.TEMPLATE_DIRS

    return render_to_response(template)

def auth_sptrans(request):

    client = SPTransClient()
    res = client.auth()

    if res:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)
