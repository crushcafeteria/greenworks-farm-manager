from django.urls import path
from django.contrib import admin
from weather.views import WeatherListView

urlpatterns = [
    path('', WeatherListView.as_view(), name='weather_list'),
]
