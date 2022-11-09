FROM tensorflow/tensorflow:latest
COPY ./server /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/app/add-google-credentials.sh"]
