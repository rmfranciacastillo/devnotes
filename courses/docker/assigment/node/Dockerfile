FROM alpine:latest

RUN mkdir -p /./var/www/sample

ENTRYPOINT apk add --update nodejs npm

WORKDIR /var/www/sample

COPY package.json . 

CMD ["npm", "install"]

COPY . .  

EXPOSE 3000

CMD ["npm", "start"]
