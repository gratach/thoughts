# Main server setup instruction

This is a detailed instruction on how I did the setup of my server.
If you find any security flaws in this configuration please do not exploit them but notify me so I can fix them (patrick-richter(at)posteo.de).
### Create a server

Create an account on [Hetzner](https://hetzner.com)
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

##### Prepare the debablo website

```
git clone --depth 1 https://github.com/gratach/debablo-website
rsync -a --delete debablo-website/www/ $MYSERVERNAME:/var/www/dabablo-website
```
##### Prepare the spiralife website

```
git clone https://github.com/gratach/spiralife
cd spiralife
git switch javascript
cd javascript
npm run build
rsync -a --delete dist/ $MYSERVERNAME:/var/www/spiralife-website
cd ../..
```

##### Prepare the quantsimulant website
```
# Install emskripten
git clone https://github.com/emscripten-core/emsdk.git
cd emsdk
./emsdk install latest
./emsdk activate latest
source ./emsdk_env.sh
cd ..
# Prepare quantsimulant website
git clone --depth 1 https://github.com/gratach/quantsimulant.git
git clone --depth 1 https://github.com/gratach/quantsimulant-website.git
python3 quantsimulant-website/create_website.py
rsync -a --delete quantsimulant-website/dist/ $MYSERVERNAME:/var/www/quantsimulant
```
##### Prepare klangqualm website

```
git clone https://github.com/gratach/klangqualm-website
```
Copy the user data that has been obtained by scraping it from the previous server or getting it from an archive into the folder `klangqualm-website/data`.

Build the website:
```
cd klangqualm-website
pnpm run build
cd ..
```
```
rsync -a -v --stats --progress --delete klangqualm-website/dist/ $MYSERVERNAME:/var/www/klangqualm-website
```

##### Prepare the thoughts website

```
git clone --depth 1 https://github.com/gratach/thoughts
python3 thoughts/.commands/create_sphinx_documentation.py
rsync -a --delete thoughts/.commands/output/ $MYSERVERNAME:/var/www/thoughts
```

##### Prepare cokurs and scratch website
```
git clone --depth 1 https://github.com/gratach/cokurs-website
git clone --depth 1 https://github.com/gratach/scratch-gui-custom-project-host
```
Obtain the old user data of the cokurs website ether by extracting it from an existing cokurs website or by getting it from the archive.

Bevore loading the user data from the directory path `<path-of-the-user-data>` into the website the correct variables have to be set:

Therefore alter the file `<path-of-the-user-data>/config.json`
Insert the following values (add them to the other existing values):
```json
{
    "cokurs-url": "cokurs.de",
    "full-scratch-url-prefix": "https://scratch.cokurs.de",
}
```
Now load the user data into the cokurs website:
```
python3 cokurs-website/build_website.py -i <path-of-the-user-data>
```
Upload the cokurs website:
```
rsync -a -v --stats --progress --delete cokurs-website/dist/ $MYSERVERNAME:/var/www/cokurs-website
rsync -a -v --stats --progress --delete cokurs-website/metadata/ $MYSERVERWEBUSERNAME:~/cokurs-metadata
```
Upload the scratch assets and projects:
```
ssh $MYSERVERNAME 'mkdir -p /var/www/scratch-data'
rsync -a -v --stats --progress --delete cokurs-website/scratch-assets/ $MYSERVERNAME:/var/www/scratch-data/assets
rsync -a -v --stats --progress --delete cokurs-website/scratch-projects/ $MYSERVERNAME:/var/www/scratch-data/projects
```
Prepare build of the scratch website.
Create a file `scratch-gui-custom-project-host/settings.json` with the following content:
```
{
    "project_host": "https://scratch-data.cokurs.de/projects",
    "asset_host": "https://scratch-data.cokurs.de/assets"
}
```
Build the scratch website:
```
cd scratch-gui-custom-project-host
npm install
npm run build
```
Upload the scratch website to the server:
```
rsync -a -v --stats --progress --delete build/ $MYSERVERNAME:/var/www/scratch
cd ..
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
##### Prepare the linkinator-test website

Clone the website generator
```
git clone --depth 1 https://github.com/gratach/linkinator-test-scrape-website
```
Generate the website:
```
python3 linkinator-test-scrape-website/create_website.py -n 1234
```
Upload the website:
```
rsync -a -v --stats --progress --delete linkinator-test-scrape-website/dist/ $MYSERVERNAME:/var/www/linkinator-test
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
	server_name trickrichter.de www.trickrichter.de;
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
	
	server_name debablo.de www.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/debablo-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name spiralife.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/spiralife-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name thoughts.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/thoughts/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name klangqualm.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/klangqualm-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name klangqualm.de www.klangqualm.de;
	ssl_certificate /etc/letsencrypt/live/klangqualm.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/klangqualm.de/privkey.pem;

	root /var/www/klangqualm-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name cokurs.de www.cokurs.de;
	ssl_certificate /etc/letsencrypt/live/cokurs.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/cokurs.de/privkey.pem;

	root /var/www/cokurs-website/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name scratch.cokurs.de;
	ssl_certificate /etc/letsencrypt/live/cokurs.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/cokurs.de/privkey.pem;

	root /var/www/scratch/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name scratch-data.cokurs.de;
	ssl_certificate /etc/letsencrypt/live/cokurs.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/cokurs.de/privkey.pem;

	root /var/www/scratch-data/;
	index index.html index.htm;

	location / {
		add_header 'Access-Control-Allow-Origin' 'https://scratch.cokurs.de' always;
		add_header 'Access-Control-Allow-Methods' 'GET, OPTIONS' always;
		add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization' always;
		add_header 'Vary' 'Origin' always;

		if ($request_method = 'OPTIONS') {
			add_header 'Access-Control-Max-Age' 86400;
			add_header 'Content-Type' 'text/plain; charset=utf-8';
			add_header 'Content-Length' 0;
			return 204;
		}
    
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name linkinator-test.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/linkinator-test/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name quantsimulant.debablo.de;
	ssl_certificate /etc/letsencrypt/live/debablo.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/debablo.de/privkey.pem;

	root /var/www/quantsimulant/;
	index index.html index.htm;

	location / {
		try_files $uri $uri/ =404;
	}
}
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name quantsimulant.de www.quantsimulant.de
	ssl_certificate /etc/letsencrypt/live/quantsimulant.de/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/quantsimulant.de/privkey.pem;

	root /var/www/quantsimulant/;
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

| Domain           | Type | Name          | Value                   |
| ---------------- | ---- | ------------- | ----------------------- |
| trickrichter.de  | A    | @             | `<server IPv4 address>` |
| trickrichter.de  | A    | pa            | `<server IPv4 address>` |
| trickrichter.de  | A    | www           | `<server IPv4 address>` |
| trickrichter.de  | A    | server        | `<server IPv4 address>` |
| trickrichter.de  | A    | linchat       | `<server IPv4 address>` |
| trickrichter.de  | AAAA | @             | `<server IPv6 address>` |
| trickrichter.de  | AAAA | pa            | `<server IPv6 address>` |
| trickrichter.de  | AAAA | www           | `<server IPv6 address>` |
| trickrichter.de  | AAAA | server        | `<server IPv6 address>` |
| trickrichter.de  | AAAA | linchat       | `<server IPv6 address>` |
| trickrichter.de  | MX   | @             | server                  |
| debablo.de       | A    | @             | `<server IPv4 address>` |
| debablo.de       | A    | www           | `<server IPv4 address>` |
| debablo.de       | A    | spiralife     | `<server IPv4 address>` |
| debablo.de       | A    | thoughts      | `<server IPv4 address>` |
| debablo.de       | A    | quantsimulant | `<server IPv4 address>` |
| debablo.de       | A    | klangqualm    | `<sever IPv4 address>`  |
|         debablo.de         |   A   |        linkinator-test       |             `<sever IPv4 address>`            |
| debablo.de       | AAAA | @             | `<server IPv6 address>` |
| debablo.de       | AAAA | www           | `<server IPv6 address>` |
| debablo.de       | AAAA | spiralife     | `<server IPv6 address>` |
| debablo.de       | AAAA | thoughts      | `<server IPv6 address>` |
| debablo.de       | AAAA | quantsimulant | `<server IPv6 address>` |
| debablo.de       | AAAA | klangqualm    | `<sever IPv6 address>`  |
|         debablo.de         |   AAAA   |        linkinator-test       |             `<sever IPv6 address>`            |
| cokurs.de        | A    | @             | `<server IPv4 address>` |
| cokurs.de        | A    | www           | `<server IPv4 address>` |
| cokurs.de        | A    | scratch       | `<server IPv4 address>` |
| cokurs.de        | A    | scratch-data  | `<server IPv4 address>` |
| cokurs.de        | AAAA | @             | `<server IPv6 address>` |
| cokurs.de        | AAAA | www           | `<server IPv6 address>` |
| cokurs.de        | AAAA | scratch       | `<server IPv6 address>` |
| cokurs.de        | AAAA | scratch-data  | `<server IPv6 address>` |
| quantsimulant.de | A    | @             | `<server IPv4 address>` |
| quantsimulant.de | A    | www           | `<server IPv4 address>` |
| quantsimulant.de | AAAA | @             | `<server IPv6 address>` |
| quantsimulant.de | AAAA | www           | `<server IPv6 address>` |
|         klangqualm.de         |   A   |        @       |             `<server IPv4 address>`            |
|                      klangqualm.de                      |      A     |         www        |                                    `<server IPv4 address>`                                   |
|                klangqualm.de               |    AAAA   |        @        |                        `<server IPv6 address>`                        |
|                      klangqualm.de                      |      AAAA     |         www        |                                    `<server IPv6 address>`                                   |
### Configure the revers DNS records
Navigate to [Hetzner->Cloud->Projects](https://console.hetzner.cloud/projects)
Navigate to the server + click on it
Navigate to networking
Set the reverse DNS records

| IP                      | Reverse-DNS            |
| ----------------------- | ---------------------- |
| `<server IPv4 address>` | server.trickrichter.de |
| `<server IPv6 address>` |  server.trickrichter.de |

### Configure HTTPS

```
apt install certbot
apt install python3-certbot-nginx
certbot register
certbot certonly -n --nginx --force-renewal --cert-name trickrichter.de -d trickrichter.de -d pa.trickrichter.de -d linchat.trickrichter.de -d www.trickrichter.de
certbot certonly -n --nginx --force-renewal --cert-name debablo.de -d debablo.de -d www.debablo.de -d spiralife.debablo.de -d thoughts.debablo.de -d quantsimulant.debablo.de -d klangqualm.debablo.de -d linkinator-test.debablo.de
certbot certonly -n --nginx -d cokurs.de -d www.cokurs.de -d scratch.cokurs.de -d scratch-data.cokurs.de
certbot certonly -n --nginx -d quantsimulant.de -d www.quantsimulant.de
certbot certonly -n --nginx --force-renewal -d klangqualm.de -d www.klangqualm.de
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

## Update and migration

### Update the server
```
apt update
apt upgrade
```
When updating postfix a configuration popup might appear -> choose "No configuration"

Restarting the server after the update might be necessary.

### Restart the server

The server can be rebooted with:
```
shutdown -r now
```
After rebooting start linchat websocket service:
```
su - webuser
cd linchat
nohup python3 chat_server.py > /dev/null 2>&1 &
```

### Scrape the user data from the server for migration

Some of the data is not stored in github but only on the server and local archives.

#### Scrape Klangqualm website
```
rsync -a --delete $MYSERVERNAME:/var/www/klangqualm-website/data/ <path-of-the-new-user-data>
```

#### Scrape Cokurs and Scratch

The following commands can be used to scrape the cokurs and scratch user data from the server and put them back into a local cokurs project.
```
git clone --depth 1 https://github.com/gratach/cokurs-website
rsync -a --delete $MYSERVERNAME:/var/www/cukurs-website/ cokurs-website/dist
rsync -a --delete $MYSERVERNAME:/var/www/scratch-data/assets/ cokurs-website/scratch-assets
rsync -a --delete $MYSERVERNAME:/var/www/scratch-data/projects/ cokurs-website/scratch-projects
rsync -a --delete $MYSERVERWEBUSERNAME:~/cokurs-metadata/ cokurs-website/metadata
```
They can then be exported to a local user data directory `<path-of-the-new-user-data>`:
```
python3 cokurs-website/export_data.py --export-folder <path-of-the-new-user-data>
```

## Check server setup

The status of the server setup can be checked with linkinator.

### Install linkinator
```
npm install -g linkinator
```
### Scan all websites
The websites can be scanned with [Linkinator](../web-development/linkinator.md)
```
linkinator \
https://trickrichter.de \
https://pa.trickrichter.de \
https://www.trickrichter.de \
https://linchat.trickrichter.de \
https://debablo.de \
https://www.debablo.de \
https://spiralife.debablo.de \
https://thoughts.debablo.de \
https://quantsimulant.debablo.de \
https://klangqualm.debablo.de \
https://cokurs.de \
https://www.cokurs.de \
https://scratch.cokurs.de \
https://quantsimulant.de \
https://www.quantsimulant.de \
https://klangqualm.de \
https://www.klangqualm.de \
--recurse
```
