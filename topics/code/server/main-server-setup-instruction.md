# Main server setup instruction

This is a detailed instruction on how I did the setup of my server
### Create a server

Create an account on [Hetzner](hetzner.com)
Navigate to Hetzner Cloud
Create a new Server or [Rebuild an existing Server](../bugs/rebuilding-the-hetzner-server.md) with the Debian 12 image
[Configure a ssh key](configure-ssh-key-for-server.md)
[Change keyboard setting to German](debian-change-keyboard-setting-to-german.md)

### Create webuser

Create a new user to store the hosted content
```
adduser --disabled-password webuser
```
Press enter to use default values and confirm with yes

(Optional) Enable ssh key for webuser
```
su -c "mkdir -p ~/.ssh" webuser
chmod 700 /home/webuser/.ssh
cp ~/.ssh/authorized_keys /home/webuser/.ssh/authorized_keys
chown webuser:webuser /home/webuser/.ssh/authorized_keys
```
### Download the content

Install git
```
apt update
apt install git
```

Switch user and change into the home directory of webuser
```
su - webuser
```

Get the pa.trickrichter.de website
```
git clone --depth 1 https://github.com/gratach/pa-trickrichter-website
```

### Configure Nginx

Switch back to root
```
exit
```
Install Nginx
```
apt install nginx
```

Add the config file "server" to the directory /etc/nginx/sites-enabled/

```
cat > /etc/nginx/sites-enabled/server << 'EOF'

```

This is the file content

```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    return 301 https://$host$request_uri;
}

server {
	listen 443 ssl;
	listen [::]:443 ssl;
	server_name trickrichter.de;
	ssl_certificate /etc/letsencrypt/live/trickrichter.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/trickrichter.de/privkey.pem;
	return 301 https://pa.trickrichter.de$request_uri;
}

server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name pa.trickrichter.de;
	ssl_certificate /etc/letsencrypt/live/trickrichter.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/trickrichter.de/privkey.pem;

	root /home/webuser/pa-trickrichter-website/www;
	index index.html index.htm index.nginx-debian.html;

	location / {
		try_files $uri $uri/ =404;
	}
}

```
End the file
```
EOF
```

### Configure DNS Records

First the domain has to be registered (only necessary if not only done)
Navigate to [Hetzner->Robot->Domain](https://robot.hetzner.com/domain)
Register new domain

Next the registered domains have to be assigned to the servers by configuring DNS records
Navigate to [Hetzner->DNS](https://dns.hetzner.com/)
Navigate to the domain
Add or change the records

For the server the following DNS records were configured

| Domain          | Type | Name | Value                   |
| --------------- | ---- | ---- | ----------------------- |
| trickrichter.de | A    | @    | `<server IPv4 address>` |
| trickrichter.de | A    | pa   | `<server IPv4 address>` |
| trickrichter.de | A    | www  | `<server IPv4 address>` |
| trickrichter.de | A    | mail | `<server IPv4 address>` |
| trickrichter.de | AAAA | @    | `<server IPv6 address>` |
| trickrichter.de | AAAA | pa   | `<server IPv6 address>` |
| trickrichter.de | AAAA | www  | `<server IPv6 address>` |
| trickrichter.de | AAAA | mail | `<server IPv6 address>` |

### Configure HTTPS

```
apt install certbot
apt install python3-certbot-nginx
certbot register
certbot certonly -n --nginx -d trickrichter.de -d pa.trickrichter.de
```









