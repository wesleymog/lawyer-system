from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('document_upload/', views.document_upload, name="document_upload"),
    path('documents-user/<int:pk>', views.document_user, name="document_user"),
    path('search_results', views.search_results, name="search_results"),
    path('edit-user/<int:pk>', views.UserUpdate.as_view(), name='user_edit'),
    path('delete-user/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
    path('delete-user/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]

