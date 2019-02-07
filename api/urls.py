from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('procedure_Locations/<int:procedure_Location_id>', views.Procedure_LocationsView.as_view(), name='id-procedure_Locations'),
    path('procedure_Locations/', views.Procedure_LocationsView.as_view(), name='all-procedure_Locations'),
    path('procedures/<int:procedure_id>', views.ProceduresView.as_view(), name='id-procedures'),
    path('procedures/', views.ProceduresView.as_view(), name='all-procedures'),
    path('providers/<int:provider_id>', views.ProvidersView.as_view(), name='id-providers'),
    path('providers/', views.ProvidersView.as_view(), name='all-providers'),
    path('locations/<int:location_id>', views.LocationsView.as_view(), name='id-locations'),
    path('locations/', views.LocationsView.as_view(), name='all-locations'),
]
