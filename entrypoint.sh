#!/bin/bash

# Start the MySQL server
service mariadb start

# Create the MySQL database and user
mysql -u root -e "CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};"
mysql -u root -e "CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';"
mysql -u root -e "GRANT ALL PRIVILEGES ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"

# Apply migrations and start the Django application
python manage.py makemigrations browsergame
python manage.py migrate
python manage.py runserver
