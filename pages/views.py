from django.shortcuts import render

# Create your views here.

def index(request):
    res=render(request, 'index.html')
    return res

def about(request):
    res=render(request, 'about.html')
    return res
