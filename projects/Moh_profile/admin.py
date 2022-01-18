from django.contrib import admin
from Moh_profile.models import Covid19, Health_Priorities, Mohevents, Documents, Eventcategory, Contact


# Register your models here.
admin.site.register(Covid19)
admin.site.register(Health_Priorities)
admin.site.register(Mohevents)
admin.site.register(Documents)
admin.site.register(Eventcategory)
admin.site.register(Contact)
