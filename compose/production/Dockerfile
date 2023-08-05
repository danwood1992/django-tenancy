# Pull base image
FROM ubuntu:22.04

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv \
    python3.10-dev \
    build-essential \
    libpq-dev \
    gcc \
    wget \
    autoconf \
    automake \
    pkg-config \
    libtool \
    procps \
    supervisor 

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy Supervisor configuration files
COPY ./compose/production/supervisor.conf /etc/supervisor/conf.d/

# Set Supervisor as the default command
CMD "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"

# Copy project files
COPY ./compose/production/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/start /start
RUN chmod +x /start

# Set working directory
WORKDIR /opt/django-tenancy

ENTRYPOINT [ "/entrypoint" ]