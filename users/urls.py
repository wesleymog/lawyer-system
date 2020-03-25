from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
]
