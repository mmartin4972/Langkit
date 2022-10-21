FROM tensorflow/tensorflow:latest
COPY ./server /app
WORKDIR /app
RUN pip install -r requirements.txt
