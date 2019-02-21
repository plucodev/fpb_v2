from django.contrib import admin
from api.models import Contact, Provider, Procedure, Location, Specialty, Profile

class ProviderAdmin(admin.ModelAdmin):
    list_display=('name', 'description')
    search_fields=['name', 'description']

class ProcedureAdmin(admin.ModelAdmin):
    pass
    
class LocationAdmin(admin.ModelAdmin):
    pass






# Register your models here.
admin.site.register(Contact)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Procedure)
admin.site.register(Location)
admin.site.register(Specialty)
admin.site.register(Profile)
