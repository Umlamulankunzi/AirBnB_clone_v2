#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static.

# Update package repository
apt update -y

# Install Nginx web server
apt install nginx -y

# Allow HTTP traffic through the firewall
ufw allow 'Nginx HTTP'

# Create necessary directories for web_static deployment
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create index.html file with content
cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link to the latest release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the directories to 'ubuntu' user and group
chown -R ubuntu:ubuntu /data

# Configure Nginx to serve /hbnb_static/ from the current release directory
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# Restart Nginx to apply the configuration changes
service nginx restart
