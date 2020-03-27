from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('document_upload/', views.document_upload, name="document_upload"),
]

