FROM node:14

ADD . /log_js
WORKDIR /log_js

COPY package*.json ./

RUN npm install

EXPOSE 3000

CMD [ "node", "app.js" ]
