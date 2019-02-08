from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, Provider, Procedure, Procedure_Location, Location
from api.serializers import ContactSerializer, ProviderSerializer, ProcedureSerializer, LocationSerializer, Procedure_LocationSerializer

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
            
class ProceduresView(APIView):
    def get(self, request, procedure_id=None):

        if procedure_id is not None:
            procedure = Procedure.objects.get(id=procedure_id)
            serializer = ProcedureSerializer(procedure, many=False)
            return Response(serializer.data)
        else:
            procedures = Procedure.objects.all()
            serializer = ProcedureSerializer(procedures, many=True)
            return Response(serializer.data)
            
    def post(self, request):
                
            serializer = ProcedureSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, procedure_id):
        
        procedure = Procedure.objects.get(id=procedure_id)
        procedure.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class LocationsView(APIView):
    def get(self, request, location_id=None):

        if location_id is not None:
            location = Location.objects.get(id=location_id)
            serializer = LocationSerializer(location, many=False)
            return Response(serializer.data)
        else:
            locations = Location.objects.all()
            serializer = LocationSerializer(locations, many=True)
            return Response(serializer.data)
            
    def post(self, request):
                
            serializer = LocationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, location_id):
        
        location = Location.objects.get(id=location_id)
        location.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class Procedure_LocationsView(APIView):
    def get(self, request, procedure_Location_id=None):

        if procedure_Location_id is not None:
            procedure_Location = Procedure_Location.objects.get(id=procedure_Location_id)
            serializer = Procedure_LocationSerializer(procedure_Location, many=False)
            return Response(serializer.data)
        else:
            procedure_Locations = Procedure_Location.objects.all()
            serializer = Procedure_LocationSerializer(procedure_Locations, many=True)
            return Response(serializer.data)
            
    def post(self, request):
                
            serializer = Procedure_LocationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    def delete(self, request, procedure_Location_id):
        
        procedure_Location = Procedure_Location.objects.get(id=procedure_Location_id)
        procedure_Location.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
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
