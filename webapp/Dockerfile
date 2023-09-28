FROM node:12-alpine as node

WORKDIR /app
COPY package.json ./
RUN npm install
COPY ./ /app/
RUN npm run build

FROM nginx:1.14.2
COPY --from=node /app/build/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf
