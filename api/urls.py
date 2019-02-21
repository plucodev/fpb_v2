from django.contrib import admin
from django.urls import re_path, include, path
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('specialtys/<int:specialty_id>', views.SpecialtysView.as_view(), name='id-specialtys'),
    path('specialtys/', views.SpecialtysView.as_view(), name='all-specialtys'),
    path('procedures/<int:procedure_id>', views.ProceduresView.as_view(), name='id-procedures'),
    path('procedures/', views.ProceduresView.as_view(), name='all-procedures'),
    path('providers/<int:provider_id>', views.ProvidersView.as_view(), name='id-providers'),
    path('providers/', views.ProvidersView.as_view(), name='all-providers'),
    path('locations/<int:location_id>', views.LocationsView.as_view(), name='id-locations'),
    path('locations/', views.LocationsView.as_view(), name='all-locations'),
    path('users/<int:user_id>', views.UserViewSet.as_view(), name='id-users'),
    path('users/', views.UserViewSet.as_view(), name='all-users'),
    # path('profiles/', views.ProfileViewSet.as_view(), name='all-profiles'),
    # path('profiles/<int:user_id>', views.ProfileViewSet.as_view(), name='id-profiles'),
    # path('patients/', views.PatientRecordView.as_view(), name='all-patients'),
    # re_path('procedures(?P<name>.+)/$', views.ProceduresView.as_view (), name='getResults')
]
