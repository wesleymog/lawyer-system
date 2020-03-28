from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users, Document
from django.contrib import messages
from django.http import HttpResponseRedirect
import urllib
from .tasks import search_task
from django.shortcuts import redirect

def helloWorld(request):
    return HttpResponse('Hello World')

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = Users.objects.all()
            context = {'users':users}
            return render(request, 'dashboard/home.html', context)
        else:
            documents = Document.objects.filter(user = request.user)
            context = {'documents':documents}
            return render(request, 'dashboard/documents.html', context)
    else:
        return redirect('/accounts/login')

def search(request):
    search_task(request.POST['search'])
    messages.success(request, 'A pesquisa será feita! Agora espere os resultados!', extra_tags='alert-success')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
