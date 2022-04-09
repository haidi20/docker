FROM nginx:1.21.6-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html
COPY haidinata.com/index.html /var/www/haidinata.com/html/index.html
COPY subdomain.haidinata.com/index.html /var/www/subdomain.haidinata.com/html/index.html

# RUN apk add --update nano