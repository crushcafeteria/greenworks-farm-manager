from django.conf import settings
import requests
from django.http.response import JsonResponse
from weather.models import WeatherData
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView


class WeatherListView(ListView):
    model = WeatherData
    context_object_name = 'weatherdata'
    template_name = 'weather/list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = WeatherData.objects.latest('observation_timestamp')
        return context


# def list(request):
#     weather = WeatherData.objects.all()
#     paginator = Paginator(weather, 10)
#     context = {
#         'weather': paginator.get_page(request.GET.get('page')),
#         'current': weather.first()
#     }
#     return render(request, 'weather/list.html', context=context)
