from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    CPF = models.CharField(max_length=11)
    Endereço = models.CharField(max_length=255)
    RG = models.CharField(max_length=9)
    Profile_picture = models.CharField(max_length=255)

    # if your additional field is a required field, just add it, don't forget to add 'email' field too.
    # REQUIRED_FIELDS = ['mobile', 'email']