from django.db import models
import datetime

# Create your models here.
class UserType(models.Model):
    usertypeLib=models.CharField(max_length=30)
    usertypedesc=models.CharField(max_length=200)
    usertypedatecreation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usertypeLib
    
class User(models.Model):
    userFirstname=models.CharField(max_length=30, unique=True)
    userLastname=models.CharField(max_length=30)
    userEmail=models.EmailField()
    userNumber=models.IntegerField()
    userdatecreation = models.DateTimeField(auto_now=True)
    userType=models.ForeignKey(UserType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.userEmail
    
class Materiel(models.Model):
    materiellib = models.CharField(max_length=30)
    materieldesc = models.CharField(max_length = 150)
    materieldatearrivee = models.DateField()
    materieldatecreation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.materieldatecreation