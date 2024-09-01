release: python manage.py showmigrations && python manage.py makemigrations && python manage.py migrate && python manage.py shell < create_superuser.py
web: gunicorn core.wsgi --log-file -