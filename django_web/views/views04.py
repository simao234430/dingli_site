from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    context = {}

    return render(request, "lab.html", context)
    # return render(request, 'index.html', context)
