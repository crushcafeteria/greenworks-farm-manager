from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from weather.models import WeatherData
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegistrationForm

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created for ' + form.cleaned_data.get('username'))
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def dashboard(request):
    context = {
        'current_weather': WeatherData.objects.order_by('-id').first()
    }
    return render(request, 'dashboard.html', context)