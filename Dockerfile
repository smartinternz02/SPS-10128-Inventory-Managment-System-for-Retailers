FROM python:3.9.2-alpine
WORKDIR /app
ADD . /app

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        mariadb-dev \
        python-dev \
        postgresql-dev \

COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
