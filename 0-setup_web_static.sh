#!/usr/bin/env bash
# setting up the web servers for deplayment of the static page
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "<html>\n<head></head>\n<body>\ntest page for nginx\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu -hR /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
