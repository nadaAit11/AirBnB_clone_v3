#!/usr/bin/env bash
# Sets up web servers for deployment of web_static.

# Install Nginx if not installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
