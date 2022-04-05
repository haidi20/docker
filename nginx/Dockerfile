FROM nginx:1.21.6-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html

RUN apk add --update nano