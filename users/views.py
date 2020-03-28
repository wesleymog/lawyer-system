from django.shortcuts import render
from users.forms import UserModelForm, DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect   
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Users, Document, Searches
from django.urls import reverse_lazy

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'users/cadastro.html', context)

class UserUpdate(UpdateView):
    model = Users
    fields = ['first_name','last_name','CPF','email','Endereço','RG']
    success_url = reverse_lazy('home')

class UserDelete(DeleteView):
    model = Users
    success_url = reverse_lazy('home')

def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'users/documents.html', {
        'form': form
    })
def document_user(request, pk):
    documents = Document.objects.filter(user__pk=1)
    return render(request, 'users/documents_users.html', {
        'documents': documents
    })
def search_results(request):
    search = Searches.objects.all()
    return render(request, 'users/search_results.html', {
        'search': search
    })
