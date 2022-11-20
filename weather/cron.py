# Get latest weather data from Accuweather API for the specified location
from django.conf import settings
import requests
from weather.models import WeatherData


def fetch_latest_weather():
    url = settings.WEATHER_ENDPOINT + \
        '/currentconditions/v1/226539/historical/24?details=true&apikey=' + \
        settings.WEATHER_API_KEY
    res = requests.get(url)

    # print(res.text)
    res = res.json()

    # Save latest data
    if 'Code' in res:
        print('Accuweather Service Unavailable')
    else:
        save_latest_response(res)


def save_latest_response(res):
    for i in range(len(res)):
        data = WeatherData.objects.filter(epoch=res[i]['EpochTime'])
        if not data:
            data = WeatherData(
                epoch=res[i]['EpochTime'],
                observation_timestamp=res[i]['LocalObservationDateTime'],
                description=res[i]['WeatherText'],
                weather_icon=res[i]['WeatherIcon'],
                daytime=res[i]['IsDayTime'],
                temperature=res[i]['Temperature']['Metric']['Value'],
                range_24_hr_temp=res[i]['Past24HourTemperatureDeparture']['Metric']['Value'],
                relative_humidity=res[i]['RelativeHumidity'],
                wind_direction=str(res[i]['Wind']['Direction']['Degrees']) + ' ' + res[i]['Wind']['Direction'][
                    'English'],
                wind_speed=res[i]['Wind']['Speed']['Metric']['Value'],
                uv_index=res[i]['UVIndex'],
                cloud_cover=res[i]['CloudCover'],
                cloud_ceiling=res[i]['Ceiling']['Metric']['Value'],
                precipitation_12_hr=res[i]['PrecipitationSummary']['Past12Hours']['Metric']['Value'],
            )
            data.save()
