FROM nginx:1.23.3-alpine

RUN apk add --update openssl

RUN mkdir -p /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 10000 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt \
    -subj "/CN=localhost"

COPY /compose/dev/nginx/nginx.conf /etc/nginx/conf.d/default.conf