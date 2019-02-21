from rest_framework import serializers
from .models import Contact, Provider, Procedure, Specialty, Location, Profile
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        exclude = ()
        fields = ('id', 'name', 'description', 'CPT_Code')

class ProviderSerializer(serializers.ModelSerializer):
    # location = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Provider
        exclude = ()
        fields = ('id', 'name', 'description')
        
        
class LocationSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(read_only=True, many=True)
    provider = ProviderSerializer(read_only=True, many=True)
    class Meta:
        model = Location
        exclude = ()
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone', 'lat', 'long', 'procedure','provider')
        

        
class SpecialtySerializer(serializers.ModelSerializer):
    # provider = ProviderSerializer()
    # procedure = ProcedureSerializer()
    # location = LocationSerializer()
    
    class Meta:
        model = Specialty
        exclude = ()
        # fields = ('id','price','provider', 'procedure', 'location')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ('user_id','is_loggedIn', 'is_patient')

        
class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta: 
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

# class ProfileSerializer(serializers.ModelSerializer):
#     """
#     A student serializer to return the student details
#     """
#     user = UserSerializer(required=True)

#     class Meta:
#         model = Profile
#         fields = ('user', 'is_loggedIn', 'is_patient')
