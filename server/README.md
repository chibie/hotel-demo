# Properties API Documentation

This is a REST API built using Django Rest Framework. It allows users to view properties (hotels to be precise), check for hotels in a particular area, and book hotel rooms.

## Endpoints

`BASE_URL = http://127.0.0.1:8000/api/`

- GET /properties (list all properties)
- GET /properties?at=lat,long (list all hotels in a particular area)
- GET /properties/:id/bookings (list all bookings corresponding to a property (hotel))
- GET /bookings (list all bookings)
- POST /bookings (create a booking)
- GET /docs (generated documentation)

## Local Setup

- Ensure you have docker and docker-compose installed
- Run `docker-compose up --build`
- Run `docker-compose run app sh -c "python manage.py loaddata bookings.json properties"` to load database with some data.
- Visit http://127.0.0.1:8000/api/ to access the homepage.
