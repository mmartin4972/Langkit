FROM registry.heroku.com/langkit-prod/web
ADD ./server /app
WORKDIR /app
