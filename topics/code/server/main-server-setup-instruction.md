# Main server setup instruction

This is a detailed instruction on how I did the setup of my server.
If you find any security flaws in this configuration please do not exploit them but notify me so I can fix them (patrick-richter(at)posteo.de).
### Create a server

Create an account on [Hetzner](hetzner.com)
Navigate to Hetzner Cloud
Create a new Server or [Rebuild an existing Server](../bugs/rebuilding-the-hetzner-server.md) with the Debian 12 image

### Configure the ssh key

[Configure a ssh key](configure-ssh-key-for-server.md):

Run the following on the ==local pc==

Set the ssh variables
```
read -p "Chose a name for the server > " MYSERVERNAME
read -p "Select the ip address of the server > " MYSERVERIP
MYKEYPATH="/home/$(whoami)/.ssh/"
MYSERVERWEBUSERNAME=web${MYSERVERNAME}
MYSERVERPUSERNAME=p${MYSERVERNAME}
```

Generate the key

```
ssh-keygen -f ${MYKEYPATH}${MYSERVERNAME}
```

Copy the key to the server

```
ssh-copy-id -i ${MYKEYPATH}${MYSERVERNAME} root@${MYSERVERIP}
```

Append the ssh info to the config file

```
cat >> /home/$(whoami)/.ssh/config << EOF
Host $MYSERVERNAME
	HostName $MYSERVERIP
	User root
	IdentityFile ${MYKEYPATH}${MYSERVERNAME}
	IdentitiesOnly yes
Host $MYSERVERWEBUSERNAME
	HostName $MYSERVERIP
	User webuser
	IdentityFile ${MYKEYPATH}${MYSERVERNAME}
	IdentitiesOnly yes
Host $MYSERVERPUSERNAME
	HostName $MYSERVERIP
	User p
	IdentityFile ${MYKEYPATH}${MYSERVERNAME}
	IdentitiesOnly yes
EOF
```

Log into the server with

```
ssh $MYSERVERNAME
```

Run the following on the ==server=== :
### Change keyboard setting to German

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
### Prepare the web content

Install [rsync](maintain-synchronized-version-of-directory-on-server.md) on the server

```
apt update
apt install rsync
```

```
exit
```

Run this code on the ==local pc== in a directory in which you want to store the websites

Install git and rsync on the local pc (only necessary if not already done)
```
su -
apt update
apt install git
apt install rsync
exit
```

##### Prepare the trickrichter website
```
git clone --depth 1 https://github.com/gratach/pa-trickrichter-website
rsync -a --delete pa-trickrichter-website/www/ $MYSERVERNAME:/var/www/pa-trickrichter-website
```

##### Prepare the linchat website
```
git clone --depth 1 https://github.com/gratach/linchat
```

Insert the new websocket address
```
cat > linchat/custom_config.json << EOF
{
	"websocket_url" : "wss://linchat.trickrichter.de/webs"
}
EOF
python3 linchat/prepare_for_upload.py
```
Upload content to server
```
rsync -a --delete linchat/dist/ $MYSERVERNAME:/var/www/linchat
scp linchat/chat_server.py $MYSERVERWEBUSERNAME:~/chat_server.py
```
Ssh into the server as webuser
```
ssh $MYSERVERNAME
```
Install python3 websockets
```
apt install python3-websockets
```
Switch user to webuser
```
su - webuser
```
Create a directory for the websocket server
```
mkdir linchat
mv chat_server.py linchat
cd linchat
```
Start the websocket server as a [background process](working-with-background-processes-in-bash.md)
```
nohup python3 chat_server.py > /dev/null 2>&1 &
```
Check if the process is running
```
ps -f -u webuser
```
### Configure Nginx

Switch back to root
```
exit
```
Install [Nginx](nginx.md)
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

	root /var/www/pa-trickrichter-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name linchat.trickrichter.de;
	ssl_certificate /etc/letsencrypt/live/trickrichter.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/trickrichter.de/privkey.pem;

	location /webs {
		proxy_pass http://localhost:9249;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "Upgrade";
	}

	location / {
		root /var/www/linchat/;
		index index.html index.htm;
		try_files $uri $uri/ =404;
	}
}

```
End the file
```
EOF
```

Reload Nginx
```
nginx -s reload
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

| Domain          | Type | Name    | Value                   |
| --------------- | ---- | ------- | ----------------------- |
| trickrichter.de | A    | @       | `<server IPv4 address>` |
| trickrichter.de | A    | pa      | `<server IPv4 address>` |
| trickrichter.de | A    | www     | `<server IPv4 address>` |
| trickrichter.de | A    | server  | `<server IPv4 address>` |
| trickrichter.de | A    | linchat | `<server IPv4 address>` |
| trickrichter.de | AAAA | @       | `<server IPv6 address>` |
| trickrichter.de | AAAA | pa      | `<server IPv6 address>` |
| trickrichter.de | AAAA | www     | `<server IPv6 address>` |
| trickrichter.de | AAAA | server  | `<server IPv6 address>` |
| trickrichter.de | AAAA | linchat | `<server IPv6 address>` |
| trickrichter.de | MX   | @       | server                  |
### Configure the revers DNS records
Navigate to [Hetzner->Cloud->Projects](https://console.hetzner.cloud/projects)
Navigate to the server + click on it
Navigate to networking
Set the reverse DNS records

| IP                      | Reverse-DNS            |
| ----------------------- | ---------------------- |
| `<server IPv4 address>` | server.trickrichter.de |
| `<server IPv6 address>` | server.trickrichter.de |
-
### Configure HTTPS

```
apt install certbot
apt install python3-certbot-nginx
certbot register
certbot certonly -n --nginx -d trickrichter.de -d pa.trickrichter.de -d linchat.trickrichter.de
certbot certonly -n --nginx  --staple-ocsp --force-renewal -d server.trickrichter.de
```

Set automatic certificate renewals with cron (use this syntax to avoid [bug](../bugs/etc-crontab-syntax-bug.md))

```
cat >> /etc/crontab << EOF
# Lets encrypt certificate renewal
11 22 * * 3 root certbot renew -n --nginx >> /dev/null 2>&1
EOF
```

### Configure the mail server

[configure-a-linux-mail-server](configure-a-linux-mail-server.md)

Set the hostname of the server
```
hostnamectl set-hostname server.trickrichter.de
```

Install postfix
```
apt install postfix
```
Select postfix configuration "Internet site"
Select `trickrichter.de`  as the system mail name

Set a maximum mailbox size by editing the line starting with `mailbox_size_limit =` in the file `/etc/postfix/main.cf` and change it into:

```
mailbox_size_limit = 30000000
```

Restart the mail server

```
postfix reload
```
### Create p user

Create a new user to recieve the mail traffic
```
adduser --disabled-password p
```
Press enter to use default values and confirm with yes

(Optional) Enable ssh key for webuser
```
su -c "mkdir -p ~/.ssh" p
chmod 700 /home/p/.ssh
cp ~/.ssh/authorized_keys /home/p/.ssh/authorized_keys
chown p:p /home/p/.ssh/authorized_keys
```





### Update the server

```
apt update
apt upgrade
```
When updating postfix a configuration popup might appear -> choose "No configuration"