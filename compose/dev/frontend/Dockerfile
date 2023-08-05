FROM node:19

# Set environment variables

ENV NODE_ENV=development

# Set working directory

WORKDIR /opt/django_tenancy/frontend

# Install packages

COPY ./frontend/package.json ./package.json
COPY ./frontend/package-lock.json ./package-lock.json

RUN npm ci

# Expose port

EXPOSE 3000

# Start server

CMD ["npm", "start"]