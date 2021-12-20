from django.contrib import admin
from .models import Covid19, Health_Priorities, Mohevents, Documents,Eventcategory

# Register your models here.
admin.site.register(Covid19)
admin.site.register(Health_Priorities)
admin.site.register(Mohevents)
admin.site.register(Documents)
admin.site.register(Eventcategory)
