web: gunicorn eight_bit_bazaar.wsgi:application
release: python manage.py makemigrations --noinput && python manage.py migrate --noinput