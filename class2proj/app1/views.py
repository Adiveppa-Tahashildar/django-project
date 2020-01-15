from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hello1(request):
    return  HttpResponse('<h1> hello class2 ap1 </h1>')