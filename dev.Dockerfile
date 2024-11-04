FROM python:alpine3.11

COPY . /app/

WORKDIR /app

RUN apk update && apk upgrade \
&& apk add --no-cache build-base \
&& apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make gcc \
&& apk add --no-cache python3-dev  py-pip \
&& apk add --no-cache py-pip py-virtualenv \
&& pip install --upgrade pip setuptools \
&& pip install --upgrade pip \
&& pip install wheel \
&& make activate \
&& make install

EXPOSE 3005

ENTRYPOINT ["sh", "./docker/entrypoint.sh"]