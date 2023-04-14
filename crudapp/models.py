from django.db import models

# Create your models here.
class UserDetails(models.Model):
    firstName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    Checkbox = models.CharField(max_length=50, blank= True)
    
    
    
    