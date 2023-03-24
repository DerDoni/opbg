# Use the official Python image as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install MySQL server and other dependencies
RUN apt-get update && apt-get install -y mariadb-server libmariadb-dev mariadb-client

# Create a directory for the Django app
RUN mkdir /app
WORKDIR /app

# Copy requirements.txt and install the dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /app/

# Expose the ports for Django and MySQL
EXPOSE 8000

# Add a custom entrypoint script
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
