from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id = models.IntegerField(primary_key=True,null=False)
   
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None  #this  is abstract so need to mention none

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []