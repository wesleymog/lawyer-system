from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('search/', views.search),
    path('', views.home, name="home"),
]
