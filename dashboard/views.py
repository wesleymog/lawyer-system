from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('Hello World')

def home(request):
    return render(request, 'dashboard/home.html')