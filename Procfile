web: gunicorn app.backendApi.wsgi:application --log-file - --log-level debug
python app/manage.py collectstatic --noinput
app/manage.py migrate