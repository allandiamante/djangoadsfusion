#!/bin/bash

# Build the project
pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

python3 manage.py collectstatic --no-input