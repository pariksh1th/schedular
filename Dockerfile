FROM node:alpine

WORKDIR /app

COPY package.json ./
RUN npm install

COPY next.config.js ./next.config.js
COPY tailwind.config.js ./tailwind.config.js
COPY postcss.config.js ./postcss.config.js

COPY pages ./pages
COPY components ./components
COPY lib ./lib
COPY public ./public
COPY styles ./styles

CMD ["npm", "run", "dev"]
