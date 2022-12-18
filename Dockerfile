FROM python:3.10
# Allows docker to cache installed dependencies between builds

COPY webapp/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image

COPY webapp app
WORKDIR /app
ADD .env /env_file/.env

RUN python manage.py migrate