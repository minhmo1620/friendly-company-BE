web: gunicorn --bind 0.0.0.0:$PORT app.backendApi.wsgi:application --log-file - --log-level debug
python app/manage.py collectstatic --noinput
app/manage.py migrate