# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime as dt


# Create your views here.
def index(request):
      today = dt.now().date()
      daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
      return render(request, "myapp_template.html",{"today" : today,"days_of_week" : daysOfWeek})

def morning(request):
     text = """<h1>Good Morning !<br/> welcome to my app !</h1>"""
     return HttpResponse(text)

def hello_with_parameter(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def main_page_home(request):
      return render(request, "index_main_page.html", {})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticles(request, month,year):
   text = "Displaying article of : %s/%s"%(month ,year)
   return HttpResponse(text)
