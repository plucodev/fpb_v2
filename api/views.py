from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Contact, Provider, Procedure, Specialty, Location, Profile
from api.serializers import ContactSerializer, ProviderSerializer, ProcedureSerializer, LocationSerializer, SpecialtySerializer, UserSerializer, ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import FilterSet
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django.contrib.auth.models import User

class ProvidersView(APIView):
    def get(self, request, provider_id=None):

        if provider_id is not None:
            provider = Provider.objects.get(id=provider_id)
            serializer = ProviderSerializer(provider, many=False)
            return Response(serializer.data)
        else:
            providers = Provider.objects.all()
            serializer = ProviderSerializer(providers, many=True)
            return Response(serializer.data)
            
    def post(self, request):
                
            serializer = ProviderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, provider_id):
        
        provider = Provider.objects.get(id=provider_id)
        provider.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class SpecialtysView(APIView):
    def get(self, request, specialty_id=None):

        if specialty_id is not None:
            specialty = Specialty.objects.get(id=specialty_id)
            serializer = SpecialtySerializer(specialty, many=False)
            return Response(serializer.data)
        else:
            # specialtys = Specialty.objects.filter(procedure__id__startswith=request.GET.get("procedure_ID"), location__id=request.GET.get("location_ID"))
            specialtys = Specialty.objects.all()
            serializer = SpecialtySerializer(specialtys, many=True)
            return Response(serializer.data)
            
    def post(self, request):
                
            serializer = SpecialtySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, specialty_id):
        
        specialty = Specialty.objects.get(id=specialty_id)
        specialty.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
            
# class ProceduresView(APIView):
#     def get(self, request, procedure_id=None):

#         if procedure_id is not None:
#             procedure = Procedure.objects.get(id=procedure_id)
#             serializer = ProcedureSerializer(procedure, many=False)
#             return Response(serializer.data)
#         else:
#             procedures = Procedure.objects.all()
#             serializer = ProcedureSerializer(procedures, many=True)
#             return Response(serializer.data)
            
    # def getResults(self, request, name):
    #     result = Procedure.objects.all()
    #     data = request.data
    #     result.filter(name__contains=data['name'])
    #     serializer = ProcedureSerializer(result, many=True)
    #     return Response(serializer.data)
        
class ProceduresView(generics.ListAPIView):
    serializer_class = ProcedureSerializer
    queryset = Procedure.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('name', 'description', 'location__zip_code')  
    search_fields = ('name', 'description', 'location__zip_code')
            
    # def post(self, request):
                
    #         serializer = ProcedureSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    # def delete(self, request, procedure_id):
        
    #     procedure = Procedure.objects.get(id=procedure_id)
    #     procedure.delete()
        
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
class LocationsFilter(FilterSet):
    zip_code = filters.CharFilter('zip_code')
    procedure = filters.CharFilter('procedure__id')
    name = filters.CharFilter('procedure__name')
    provider = filters.CharFilter('provider__name')
    
    
    class Meta:
        model = Location
        fields = ('zip_code','procedure', 'name', 'provider')
        
    
class LocationsView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    # filter_fields = ('zip_code', 'city')  
    search_fields = ('address', 'zip_code')
    filter_class = LocationsFilter
    
    # def get(self, request, location_id=None):

    #     if location_id is not None:
    #         location = Location.objects.get(id=location_id)
    #         serializer = LocationSerializer(location, many=False)
    #         return Response(serializer.data)
    #     else:
    #         locations = Location.objects.filter(procedure__id=request.POST.get('procedure'))
    #         serializer = LocationSerializer(locations, many=True)
    #         return Response(serializer.data)
            
    # def post(self, request):
                
    #         serializer = LocationSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    # def delete(self, request, location_id):
        
    #     location = Location.objects.get(id=location_id)
    #     location.delete()
        
    #     return Response(status=status.HTTP_204_NO_CONTENT)
            

        
class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)

# class ProcedureList(generics.ListAPIView):
#     queryset = Procedure.objects.all()
#     serializer_class = ProcedureSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('name')

class UserViewSet(APIView):
    # """
    # A viewset for viewing and editing user instances.
    # """
    # serializer_class = UserSerializer
    # queryset = User.objects.all()
    def get(self, request, user_id=None):

        if user_id is not None:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            # users = User.objects.filter(procedure__id__startswith=request.GET.get("procedure_ID"), location__id=request.GET.get("location_ID"))
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
            
    def post(self, request, user_id=None):
                
        # if user_id is not None:
        #     user = User.objects.filter(id=user_id)
        #     data=request.data
        #     user.update(firstname=data['first_name'],lastname=data['last_name'],username=data['username'],email=data['email'],password=data['password'])
        #     return Response( status=status.HTTP_200_OK)    
        # else:
            
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, user_id):
        
        user = User.objects.get(id=user_id)
        user.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# class ProfileViewSet(APIView):
#     # """
#     # A viewset for viewing and editing user instances.
#     # """
#     # serializer_class = UserSerializer
#     # queryset = User.objects.all()
#     def get(self, request, user_id=None):

#         if user_id is not None:
#             profile = Profile.objects.get(id=user_id)
#             serializer = ProfileSerializer(profile, many=False)
#             return Response(serializer.data)
#         else:
#             # profiles = Profile.objects.filter(procedure__id__startswith=request.GET.get("procedure_ID"), location__id=request.GET.get("location_ID"))
#             profiles = Profile.objects.all()
#             serializer = ProfileSerializer(profiles, many=True)
#             return Response(serializer.data)
            
#     def post(self, request, user_id=None):
                
#         if user_id is not None:
#             profile = Profile.objects.filter(id=user_id)
#             data=request.data
#             profile.update(is_loggedIn=data['is_loggedIn'],is_patient=data['is_patient'])
#             return Response( status=status.HTTP_200_OK)    
#         else:
            
#             serializer = ProfileSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    # def delete(self, request, profile_id):
        
    #     profile = Profile.objects.get(id=profile_id)
    #     user.delete()
        
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        
