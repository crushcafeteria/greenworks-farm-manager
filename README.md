# Greenworks Farm Manager

I am a software engineer living in Kenya. On the side, I also love growing plants and raising animals for profit.
I run a 2 acre farm with my bae in Western Kenya where we grow Black Nightshade for commercial purposes. I have
been struggling with record keeping for a while and thought, why not just write software to make my life easier?
So the journey began. I would like to track all expenses, sales, farm inspection notes, pesticides and weather.
I have decided to open-source this application to give other budding farmers tested tools they need to succeed in
commercial agriculture. The problems I face are a small subset to what other farmers may face, so I cannot promise
an end to end solution that fits all agriculture operations... but, you are free to fork and add features to
increase the richness of the application.

## Running migrations

```
python manage.py makemigrations && python manage.py migrate
```

# Loading seed data

```
python manage.py loaddata [fixture_name]
```

## Run background queue

```
python manage.py qcluster
```

## Run production server (Gunicorn)

```
gunicorn greenworks.wsgi:application --bind=0.0.0.0:9000
```

## Activate venv

```
source ../python_venvs/greenworks/bin/activate
```

## Fetching weather data periodically

This application pulls hourly weather data from Accuweather. Automatic data fetching has been implemented with [`django-crontab`](https://pypi.org/project/django-crontab/) package with the following settings:-

```
CRONJOBS = [
    ('0 * * * *', 'weather.cron.fetch_latest_weather')
]
```

You can review the defined cronjob at [`weather/cron.py`](weather/cron.py) to understand more about how this feature works.

To insert this cronjob in the `crontab` utiliy on UNIX, please run the following command once:-

```
python manage.py crontab add
```

To see all active cron jobs, please run the following command:-

```
python manage.py crontab show
```
