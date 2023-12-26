FROM node

COPY . ./app

WORKDIR ./app

COPY package*.json ./app

RUN npm install -g @angular/cli

RUN npm install --force

EXPOSE 4200

CMD ["ng", "serve"] 