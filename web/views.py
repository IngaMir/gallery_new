from django.shortcuts import render

def index(request):
    return(request, 'index.html')

def detail(request):
    return(request, 'detail.html')