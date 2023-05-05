# odoo_scientific_project
Docker compose for odoo 15.0 with scientific manager app

This repository is created to set up fast oddo software and create some custom apps

___

## Commands

- Start container

`docker-compose up -d`

- Nginx configuration part 1
```
sudo apt update
sudo apt install nginx
sudo ufw allow "Nginx Full"
sudo nano /etc/nginx/sites-available/odoo.conf
```

- odoo.conf
```
server {
    listen       80;
    listen       [::]:80;
    server_name  your_domain_here;

    access_log  /var/log/nginx/odoo.access.log;
    error_log   /var/log/nginx/odoo.error.log;

    location / {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Proto https;
      proxy_pass http://localhost:8069;
  }
}
```

- Nginx configuration part 2

```
sudo ln -s /etc/nginx/sites-available/odoo.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx.service

```

- Certbot configuration 

```
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain_here

```