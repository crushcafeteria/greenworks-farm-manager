from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from weather.models import WeatherData
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    context = {
        'current_weather': WeatherData.objects.order_by('-id').first()
    }
    return render(request, 'dashboard.html', context)