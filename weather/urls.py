from django.urls import path
from django.contrib import admin
from .views import weather

urlpatterns = [
    path('fetch/', weather.fetch, name='weather_fetch'),
    path('databank/', weather.list, name='weather_list'),
]
