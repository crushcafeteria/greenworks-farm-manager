from django.db import models
from django.contrib.auth.models import User


class WeatherData(models.Model):
    epoch = models.BigIntegerField(null=True)
    observation_timestamp = models.DateTimeField(null=True)
    description = models.CharField(max_length=150, null=True)
    weather_icon = models.IntegerField(null=True)
    daytime = models.CharField(max_length=100, null=True)
    temperature = models.FloatField('Temp in celsius', null=True)
    range_24_hr_temp = models.FloatField(null=True)
    relative_humidity = models.FloatField(null=True)
    wind_direction = models.CharField(max_length=100, null=True)
    wind_speed = models.FloatField(null=True)
    uv_index = models.FloatField(null=True)
    cloud_cover = models.FloatField(null=True)
    cloud_ceiling = models.FloatField('Height in metres', null=True)
    precipitation_12_hr = models.FloatField('Precipitation in mm', null=True)

    def __str__(self):
        return self.observation_timestamp

    class Meta:
        verbose_name = ('Weather Data')
        ordering = ['-observation_timestamp']

    def relative_humidity_formatted(self):
        return str(self.relative_humidity) + '%'

    def precipitation_12_hr_formatted(self):
        return str(self.precipitation_12_hr) + ' mm'

    def temperature_formatted(self):
        return str(self.temperature) + ' <sup>o</sup>C'

    def icon(self):
        return 'https://developer.accuweather.com/sites/default/files/' + self.weather_icon + '-s.png'
