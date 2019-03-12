# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from ..models import TeacherInfo,TeacherCategory,ArticleCategory,Article
# Create your views here.
category_map = {
    "hot":"新闻热点",
    "all": "新闻中心",
    "party":"党团工作",
    "international": "国际化教育",
    "job": "就业工作",
    "student": "学生管理",
    "enrol": "招生工作"
}

show_category_map = {
    "hot":"新闻热点",
    "all": "新闻中心",
    "party": "党团工作",
    "international": "国际化教育",
    "job": "就业工作",
    "student": "学生管理",
    "enrol": "招生工作"
}

def index(request,category):
    # teacher = TeacherInfo.objects.get(id=0)
    # context = {'teacher': teacher}
    temp = category_map.get(category, None)
    show_categor = show_category_map.get(category, None)

    if temp == None:
        return render(request, '404.html')
    else:
        if category_map.get(category) == '新闻中心':
            Article_list = Article.objects.all()
            paginator = Paginator(Article_list, 6)  # Show 25 contacts per page

            page = request.GET.get('page',1)
            try:
                Articles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Articles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Articles = paginator.page(paginator.num_pages)

            return render(request, 'articles.html', {'Articles': Articles, 'category': show_categor})
        else:
            list = ArticleCategory.objects.get(category=category_map.get(category, None)).article.all()
            for e in list:
                print (e.id)
            return render(request, 'articles.html', {'list': list,'category': show_categor})
    # teacher.id = teacher.id + 1
    # teacher.save()



