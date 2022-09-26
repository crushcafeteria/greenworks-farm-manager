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