FROM postgres:14.1-alpine

COPY init.sql /docker-entrypoint-initdb.d

RUN apt-get update && apt-get install nano