FROM node:19

# Set environment variables

ENV NODE_ENV=development

# Set working directory

WORKDIR /opt/django_realms/django_realms-frontend

# Install packages

COPY ./django_realms-frontend/package.json ./package.json
COPY ./django_realms-frontend/package-lock.json ./package-lock.json


RUN npm ci

# Expose port

EXPOSE 3000

# Start server

CMD ["npm", "run","dev"]