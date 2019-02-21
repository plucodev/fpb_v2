from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    CPT_Code = models.CharField(max_length=10, default='')
    
    
    def __str__(self):
        return self.name
        
class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    # location = models.ManyToManyField(Location, through='Procedure_Location')
    
    def __str__(self):
        return self.name      

class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    procedure = models.ManyToManyField(Procedure, through='Specialty')
    provider = models.ManyToManyField(Provider, through='Specialty')
    
    
    def __str__(self):
        return self.name + ' -- ' + self.address


        
class Specialty(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name = 'procedure')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name = 'location')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, related_name = 'provider')
    price = models.IntegerField()
    
    
    # def __unicode__(self):
        # return '%d: %s' % (self.price, self.procedure)
    def __str__(self):
        return ('price')
        # return 'PROVIDER: ' + self.provider.name + ' LOCATION: ' + self.location.address + ' PROCEDURE: ' + self.procedure.name + ' PRICE: $ ' + str(self.price)
    
    # def snippets(self):
    #     return self.name[:10]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_patient = models.BooleanField(default=False)
    is_loggedIn = models.BooleanField(default=False)
    
    
    
    # @receiver(post_save, sender=User)
    # def create_user_profile(self, sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(self, sender, instance, **kwargs):
    #     instance.profile.save()
        
        
        
        
#WORKING CODE       
# class Contact(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
    
# class Procedure(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=200)
    
    
#     def __str__(self):
#         return self.name
        
# class Provider(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=150)
#     # location = models.ManyToManyField(Location, through='Procedure_Location')
    
#     def __str__(self):
#         return self.name      

# class Location(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     address = models.CharField(max_length=100, null=True)
#     city = models.CharField(max_length=100, null=True)
#     state = models.CharField(max_length=100, null=True)
#     zip_code = models.CharField(max_length=100, null=True)
#     phone = models.CharField(max_length=100, null=True)
#     procedure = models.ManyToManyField(Procedure, through='Specialty')
#     provider = models.ManyToManyField(Provider, through='Specialty')
    
    
#     def __str__(self):
#         return self.name


        
# class Specialty(models.Model):
#     procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name = 'procedure')
#     location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name = 'location')
#     provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, related_name = 'provider')
#     price = models.IntegerField()
    
    
#     # def __unicode__(self):
#         # return '%d: %s' % (self.price, self.procedure)
#     def __str__(self):
#         return 'PROVIDER: ' + self.provider.name + ' LOCATION: ' + self.location.address + ' PROCEDURE: ' + self.procedure.name + ' PRICE: $ ' + str(self.price)
    
#     def snippets(self):
#         return self.name[:10]