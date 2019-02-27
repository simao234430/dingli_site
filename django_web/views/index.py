from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime
from ..models import Article
# Create your views here.
def index(request):
    context = {}
    # list = ["a", "b", "c", "d"]
    # for i in list:
    #     print i
    Article_list = Article.objects.all()[:3]
    return render(request, 'index.html', {'list': Article_list})

def test(request):
    return render_to_response('enroll.html')

def enroll(request):
    return render_to_response('enroll.html')