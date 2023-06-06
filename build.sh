#!/bin/bash

pip install -r requirements.txt

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Criou o statico"
python3 manage.py collectstatic --no-input