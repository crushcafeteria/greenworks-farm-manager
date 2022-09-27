from django.conf import settings
import requests
from django.http.response import JsonResponse
from weather.models import WeatherData
from django_q.tasks import async_task
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages


def fetch(request):
    async_task('weather.tasks.fetch_weather')
    messages.success(request, 'Weather data will be updated soon! ')
    return redirect('weather_list');

def list(request):
    weather = WeatherData.objects.all()
    paginator = Paginator(weather, 10)
    context = {
        'weather': paginator.get_page(request.GET.get('page')),
        'current': weather.first()
    }
    return render(request, 'weather/list.html', context=context)
