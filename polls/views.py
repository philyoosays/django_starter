# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    res = now.strftime("%Y-%m-%d %H:%M")
    return HttpResponse(res)
