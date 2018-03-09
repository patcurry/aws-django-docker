#!/bin/bash

# Database Migrations
#echo Make Migrations.
#exec python manage.py makemigrations
#
#echo Migrate.
#exec python manage.py migrate

#exec python manage.py runserver 8000

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn main.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
