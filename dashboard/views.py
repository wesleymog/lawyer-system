from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users, Document
from django.contrib import messages
from django.http import HttpResponseRedirect
import urllib
import requests
from bs4 import BeautifulSoup

def helloWorld(request):
    return HttpResponse('Hello World')

def home(request):
    if request.user.is_superuser:
        users = Users.objects.all()
        context = {'users':users}
        return render(request, 'dashboard/home.html', context)
    else:
        documents = Document.objects.filter(user = request.user)
        context = {'documents':documents}
        return render(request, 'dashboard/documents.html', context)

def search(request):
    messages.success(request, 'Pesquisa sendo realizada')
    query = request.POST['search']
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    context = {'results':results}
    print("olha os results aiiiiiiiiiiiiiii")
    print(results)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)
