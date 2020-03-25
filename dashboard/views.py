from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users

def helloWorld(request):
    return HttpResponse('Hello World')

def home(request):
    users = Users.objects.all()
    context = {'users':users}

    return render(request, 'dashboard/home.html', context)