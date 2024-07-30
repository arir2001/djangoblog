from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def textMaker(request):
    text = HttpResponse('Hello, Blog!')
    return text

