# event-app-API
small test app on drf

To build project
```bash
docker-compose up
```

To create superuser
```bash
docker-compose run web python manage.py createsuperuser
```

To get all events
```bash
GET /events/
```

To get event detail page
```bash
GET /event/<int:pk>/
```

To create registration 
```bash
POST /registration/ {'user': <user_id>, 'event': <event_id>}
```


To run tests
```bash
docker-compose run web python manage.py test