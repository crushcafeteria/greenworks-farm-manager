from django.conf import settings


def app_name(request):
    return {
        "APP_NAME"        : settings.APP_NAME,
        "APP_NAME_FOOTER" : settings.APP_NAME_FOOTER,
        'WEATHER_API_KEY' : settings.WEATHER_API_KEY,
        'WEATHER_ENDPOINT': settings.WEATHER_ENDPOINT,
    }
