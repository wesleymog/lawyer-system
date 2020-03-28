from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    CPF = models.CharField(max_length=11)
    Endereço = models.CharField(max_length=255)
    RG = models.CharField(max_length=9)
    Profile_picture = models.CharField(max_length=255)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)     

class Searches(models.Model):
    result = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)   