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
