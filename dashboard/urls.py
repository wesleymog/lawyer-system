from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('search/', views.search),
    path('dashboard', views.home, name="home"),
    path('', views.home, name="home"),
]
