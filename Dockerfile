FROM mmartin4972/tensorflow:langkit
COPY . /app
CMD python3 wsgi.py
