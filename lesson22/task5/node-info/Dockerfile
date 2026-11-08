FROM node:23.11.0
WORKDIR /node
COPY package.json .
RUN npm install
COPY server.js .
CMD ["node", "server.js"]

