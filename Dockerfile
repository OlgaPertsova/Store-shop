FROM python:3.11-slim

WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y curl && apt-get clean
RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py initialize_db \
    && python manage.py runserver 0.0.0.0:8003


#gunicorn docker_demo.wsgi:application -b 0.0.0.0:8000

