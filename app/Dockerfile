FROM python:3.8-alpine

WORKDIR /tmp/app

COPY ./tmp .

RUN pip install -r requirements --no-cache-dir

WORKDIR /var/www/app

ENTRYPOINT ["python", "serve.py"]

EXPOSE 80
