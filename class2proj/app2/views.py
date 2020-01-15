from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
# def Hello2(request):
#     print("running successfully")
#     return HttpResponse("<p style=color:red>Hello World</p>")



def Display(request):
    a = datetime.datetime.now()
    x = '<h1> '+ str(a) + '</h1>'
    return HttpResponse(x)