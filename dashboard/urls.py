from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.home),
]
