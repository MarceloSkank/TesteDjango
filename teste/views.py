from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request, "index.html"))

def marceloJanke(request):
    return HttpResponse(render(request, "user_data.html"))