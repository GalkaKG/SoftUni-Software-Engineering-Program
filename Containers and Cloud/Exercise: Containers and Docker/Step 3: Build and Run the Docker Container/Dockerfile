FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir /app/staticfiles

COPY static /app/staticfiles

EXPOSE 8000

CMD [ "gunicorn", "SimplePageApp.wsgi:application", "--bind", "0.0.0.0:8000" ]