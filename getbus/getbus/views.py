#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context, loader
from sptrans import SPTransClient

def home(request):

    template = '%shome.html' %settings.TEMPLATE_DIRS

    client = SPTransClient()

    client.auth()

    return render_to_response(template)
