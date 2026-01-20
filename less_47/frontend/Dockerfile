FROM nginx:1.27-alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY . . 

WORKDIR /etc/nginx/conf.d
RUN rm -rf ./*
COPY backend.conf default.conf
