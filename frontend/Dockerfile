FROM node:16-alpine3.14

WORKDIR /App

COPY . ./

ENV PATH /app/node_modules/.bin:$PATH


COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN npm install axios --silent
CMD ["npm", "run" ,"start"]
EXPOSE 3000
