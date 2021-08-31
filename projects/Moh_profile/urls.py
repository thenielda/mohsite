from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index, name='get_index'),
    path('about/',views.about, name='about'),
    path('events/',views.events, name='events'),
]