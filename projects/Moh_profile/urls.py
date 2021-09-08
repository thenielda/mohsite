from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('e-services/', views.services, name='e-services'),
    path('resources/', views.resources, name='resources'),
    path('complaints/', views.complaints, name='complaints'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('contacts/', views.contacts, name='contacts'),
    path('admin-panel', views.admin_panel, name='admin-panel')
]
