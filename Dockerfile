FROM registry.heroku.com/langkit-prod/web
COPY . /app
WORKDIR /app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
