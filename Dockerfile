FROM tensorflow/tensorflow:latest
COPY ./server /app
WORKDIR /app
RUN pip install -r requirements.txt

# install of tensorflow-text must be separate to ensure all of tensorflow is not installed
RUN pip install --no-deps tensorflow-text==2.10.0 

