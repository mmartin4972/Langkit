FROM tensorflow/tensorflow:latest
COPY ./server /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/app/translate/add-google-creds.sh"]
