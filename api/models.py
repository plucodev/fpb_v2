from rest_framework import serializers
from django.db import models

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    procedure = models.ManyToManyField(Procedure)
    
    def __str__(self):
        return self.address

class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    location = models.ManyToManyField(Location)
    
    def __str__(self):
        return self.name      
        
class Procedure_Location(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.IntegerField()
    
    
    # def __unicode__(self):
    #     return '%d: %s' % (self.price, self.procedure)
        