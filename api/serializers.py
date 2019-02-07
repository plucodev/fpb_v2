from rest_framework import serializers
from .models import Contact, Provider, Procedure, Procedure_Location, Location

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        exclude = ()
        
        
class LocationSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(read_only=True, many=True)
    class Meta:
        model = Location
        exclude = ()
        fields = ('id', 'address', 'procedure')
        
class ProviderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Provider
        exclude = ()
        fields = ('id', 'name', 'location')
        
class Procedure_LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Procedure_Location()
        exclude = ()
        


