source venv/bin/activate
redis-server &
python manage.py slave &
python manage.py runserver &
