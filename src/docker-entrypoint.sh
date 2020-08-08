#!/bin/bash

echo "collect static"
python manage.py collectstatic --no-input

echo "Starting gunicorn server"
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --preload --timeout 90 -w 4
