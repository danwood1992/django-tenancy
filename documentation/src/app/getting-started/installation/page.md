---
title: Installation
---

## Prerequisites

1. Docker: The project runs in a Docker container, so you'll need to have Docker installed. If you haven't installed it already, you can download and install Docker from here.

2. WSL (Optional): If you're on Windows, the project uses WSL, but this isn't mandatory for running the project. If you wish to set up WSL, you can follow the guide here.

## Steps:

### **Go to the github repository** [Click Here.](https://github.com/imperisoft/django-tenancy)

### **Click on the "Use this template" button**  

![Alt text](/images/use-this-template.png)

### **Clone the repository to your local machine**

### **Set up the Environment File:**

You need to set up a .env file inside a .dev folder to store environment-specific settings.

- First, create the .dev directory in the root of the project.

*linux and windows*
```shell
mkdir .dev

```
### **Next create a .env file inside the .dev directory**

This file will contain all the environment variables for the project. You can copy the contents of the .env.example file and paste it into the .env file.
Set the values of the environment variables as per your requirements.

```shell
DEBUG=1
DEV_MODE=1

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_realms
SQL_USER=django_realms
SQL_PASSWORD=your_password
SQL_HOST=django_realms-db
SQL_PORT=5432

POSTGRES_DB=django_realms
POSTGRES_USER=django_realms
POSTGRES_PASSWORD=your_postgres_password

MANAGEMENT_DOMAIN=localhost

EMAIL_HOST_USER='your_email@example.com'
EMAIL_HOST_PASSWORD=your_email_password

```

Make sure to replace your_password, your_postgres_password, your_email@example.com, and your_email_password with your actual credentials.

### Set up the Docker Compose File:

The project uses Docker Compose to run the all containers. It should run out of the box without any changes, but you can modify it as per your requirements.

### **Run The Project**

To run the project, you need to run the following command:

```shell
docker-compose up --build
```

This command will build the Docker containers and start the project. You should now be able to access the project in your web browser at the URL specified in the output https://localhost:8000 for the backend
and http:/localhost:3000 for the frontend ive put the docs at 3001, your welcome.

Congratulations! You should now have Django Realms up and running on your local machine. If you face any issues, please refer to the project's documentation or open an issue on the GitHub repository.