from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('e-services/', views.services, name='e-services'),
    path('resources/', views.resources, name='resources'),
    path('complaints/', views.complaints, name='complaints'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('contacts/', views.contacts, name='contacts'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('admin-panel/', views.post_forms, name='admin-panel'),
]
