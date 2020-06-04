FROM ubuntu:latest
MAINTAINER NewstarCorporation
CMD ["sudo", "apt-get", "install", "httpd"]
COPY index.php /var/www/html/
CMD [“/usr/sbin/httpd”, “-D”, “FOREGROUND”]
EXPOSE 80