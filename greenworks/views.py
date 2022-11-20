from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from sales.models import Sales
import datetime
from django.db.models import Sum
from expenses.models import Expenses
from weather.models import WeatherData


@login_required
def dashboard(request):
    month = datetime.datetime.now().month

    context = {
        'current_weather': WeatherData.objects.latest('observation_timestamp'),
        'sales_this_month': Sales.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum'],
        'total_sales': Sales.objects.aggregate(Sum('amount'))['amount__sum'],
        'expenses_this_month': Expenses.objects.filter(when__month=month).aggregate(Sum('amount'))['amount__sum'],
        'total_expenses': Expenses.objects.aggregate(Sum('amount'))['amount__sum']
    }

    return render(request, 'dashboard.html', context)
