FROM node:19

# Set environment variables

ENV NODE_ENV=development

# Set working directory

WORKDIR /opt/django_realms/documentation

# Install packages

COPY ./documentation/package.json ./package.json
COPY ./documentation/package-lock.json ./package-lock.json

RUN npm ci

# Expose port

EXPOSE 3000

# Start server

CMD ["npm", "run", "dev"]