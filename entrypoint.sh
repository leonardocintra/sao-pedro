#!/bin/sh

set -e

echo "Rodando migrations..."
python manage.py migrate --noinput

echo "Iniciando Gunicorn..."
exec gunicorn sao_pedro.wsgi:application --bind 0.0.0.0:8000