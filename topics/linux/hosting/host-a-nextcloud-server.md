# Host a nextcloud server

A nextcloud server can be hosted as described in the [official documentation](https://docs.nextcloud.com/server/latest/admin_manual/index.html).

There is a App in Hetzner that includes a default installation. The hetzner default image can be configured via console on the first console connection. The console installation asks you to select your url. Choose `<your choosen nextcloud domain>` a url that points to your server 

## Controlling Nextcloud with the occ command

Run the [occ cpmmand](https://docs.nextcloud.com/server/latest/admin_manual/occ_command.html) by typing:
`sudo -u www-data php /var/www/html/occ <your occ command>`

A password can be changed by typing:
`sudo -E -u www-data php /var/www/html/occ user:resetpassword <your username>`

### Add additional domains

If you want to add more domains that point to the same nextcloud instance:
Make the domain point to the server.
Add certificate: `certbot certonly -n --apache -d <your choosen additional domain>`
Copy the nextcloud configuration files in `/etc/apache2/sites-enabled` for http and https
In the copied versions change the domains to the new one.
(Enable new created VirtualHosts using `a2ensite sitename` if you have copied it in sites-available)
Add new created host names in the trusted_domains array in `/var/www/html/config/config.php`
Reload apache: `systemctl reload apache2`

## Collabora

For Collaboration on the same documents `Nextcloud Office` needs to be installed.
However for `Nextcloud Office` to work there needs to be an `collabora online` server configured. Collabora can be installed on the same server as the nextcloud installation.

### Collabora installation

[Here](https://sdk.collaboraonline.com/docs/installation/index.html) is the installation guide for Collabora Online from the official website and [here](https://docs.nextcloud.com/server/latest/admin_manual/office/installation.html) the installation instruction for setting up Collabora for Nextcloud Office.

There is a free Collabora Online Development Edition (CODE) that comes with no support and is only suitable for small teams. See [here](https://www.collaboraonline.com/de/code/#learnmorecode) for details.

Installation of CODE:

```
cd /usr/share/keyrings
wget https://collaboraoffice.com/downloads/gpg/collaboraonline-release-keyring.gpg
```

```
cat << EOF > /etc/apt/sources.list.d/collaboraonline.sources
Types: deb
URIs: https://www.collaboraoffice.com/repos/CollaboraOnline/CODE-deb
Suites: ./
Signed-By: /usr/share/keyrings/collaboraonline-release-keyring.gpg
EOF
```

```
sudo apt update && sudo apt install coolwsd code-brand
```

### Collabora configuration

When [setting up the ssl configuration](https://sdk.collaboraonline.com/docs/installation/Configuration.html#ssl-configuration) for Collabora Online the service can be configured with ssl termination which means that a ssl termination proxy handles the ssl requests and passes them on unencrypted to the collabora service.

To change the collabora ssl settings open `/etc/coolwsd/coolwsd.xml` navigate to the `<ssl>` tag and set the `<enable>` tag from true to false and the `<termination>` tag from false to true.

Change the listen address where collabora binds to to localhost because we are using an reverse proxy to forward requests from the main IP address to the localhost: Navigate to `<net>` and change the `<listen>`tag from any to loopback.

To allow your nextcloud server to use the collabora server set the storage.wopi.host to the url of the nextcloud: Therefore navigate to `<storage>`, `<wopi>` and change the `<host>` tag to your choosen nextcloud domain without `https://`.

All these changes of the `/etc/coolwsd/coolwsd.xml` file can also be done with coolconfig.
e.g. `sudo coolconfig set ssl.enable false`

Set the admin password for using the collabora admin account:
`sudo coolconfig set-admin-password`
You can access the admin account in the browser by calling:
`<your choosen collabora domain>/browser/dist/admin/admin.html`
This gives you information about usage.

To refresh the settings run:

`systemctl restart coolwsd`

### Collabora reverse proxy

You have to chose a url `<your choosen collabora domain>` that points to the server where you installed collabora.

[Proxy manual](https://sdk.collaboraonline.com/docs/installation/Proxy_settings.html)

In  `/etc/coolwsd/coolwsd.xml` edit the `<server_name>`tag to match the server name (eg. `collabora.example.com`)

Install the modules for the apache web server
```
a2enmod proxy
a2enmod proxy_http
a2enmod proxy_connect
a2enmod proxy_wstunnel
```

Get a letsencrypt certificate
```
certbot certonly -n --apache -d <your choosen collabora domain>
```

Add a new server configuration file `collabora.conf` to `/etc/apache2/sites-available/` that has the following content:

```
<IfModule mod_ssl.c>
	<VirtualHost *:443>
		ServerAdmin webmaster@localhost
		ServerName <your choosen collabora domain>
		ServerAlias www.<your choosen collabora domain>
		<IfModule mod_headers.c>
			Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains"
		</IfModule>
		SSLCertificateFile /etc/letsencrypt/live/<your choosen collabora domain>/fullchain.pem
		SSLCertificateKeyFile /etc/letsencrypt/live/<your choosen collabora domain>/privkey.pem

		#Include /etc/letsencrypt/options-ssl-apache.conf

	 	########################################
		# Reverse proxy for Collabora Online   #
		########################################

		AllowEncodedSlashes NoDecode
		ProxyPreserveHost On

		# static html, js, images, etc. served from coolwsd
		# browser is the client part of Collabora Online
		ProxyPass           /browser http://[::1]:9980/browser retry=0
		ProxyPassReverse    /browser http://[::1]:9980/browser

		# WOPI discovery URL
		ProxyPass           /hosting/discovery http://[::1]:9980/hosting/discovery retry=0
		ProxyPassReverse    /hosting/discovery http://[::1]:9980/hosting/discovery

		# Capabilities
		ProxyPass           /hosting/capabilities http://[::1]:9980/hosting/capabilities retry=0
		ProxyPassReverse    /hosting/capabilities http://[::1]:9980/hosting/capabilities

		# Main websocket
		ProxyPassMatch      "/cool/(.*)/ws$"      ws://[::1]:9980/cool/$1/ws nocanon

		# Admin Console websocket
		ProxyPass           /cool/adminws ws://[::1]:9980/cool/adminws

		# Download as, Fullscreen presentation and Image upload operations
		ProxyPass           /cool http://[::1]:9980/cool
		ProxyPassReverse    /cool http://[::1]:9980/cool

		# Compatibility with integrations that use the /lool/convert-to endpoint
		ProxyPass           /lool http://[::1]:9980/cool
		ProxyPassReverse    /lool http://[::1]:9980/cool

	</VirtualHost>
</IfModule> 
```
Replace `<your choosen collabora domain>` with the actual url (without `https://`)

This configuration requires collabora to listen on IPv6 port. Make sure that is the case.

Enable the site:
`a2ensite collabora`

Reload apache
`systemctl reload apache2`

### Starting and stopping collabora

- `systemctl enable coolwsd` – enable coolwsd on system start
- `systemctl disable coolwsd` – disable coolwsd on system start
- `systemctl status coolwsd` – check status of coolwsd
- `systemctl stop coolwsd` – stop coolwsd service
- `systemctl start coolwsd` – start coolwsd service
- `systemctl restart coolwsd` – stop then start coolwsd service
- `journalctl -u coolwsd` – read the log produced by coolwsd

### Configuring collabora in nextcloud

Log into nextcloud using the admin account. Navigate to the user icon in the top right corner and to apps. Install and activate `Nextcloud office`.

 Navigate to the user icon in the top right corner and to `Administration settings`.
 In the left bar 
Navigate to Office
Select `Use your own server`
Enter `https://<your choosen collabora domain>`
Press Save

Scroll down and add the IP adresses of the collabora server to the Allow list for WOPI requests.

Set the checkbox at Use Office Open XML because [loading of new documents is sometimes slow otherwise](https://github.com/nextcloud/richdocuments/issues/4402)

## Configuring Talk

Talk is a communication platform within Nextcloud that also includes video conferences.
It can be enabled by going to the Apps settings in the top Right corner of the admin account and enabling it in the Featured apps section.
[Admin documentation](https://nextcloud-talk.readthedocs.io/en/latest/#administration-documentation)

### Configuring a coturn server

In order for the video conferences to function properly (outside a local network) a stun and a turn server needs to be configured. [Turn server confoguration](https://nextcloud-talk.readthedocs.io/en/latest/TURN/)

One possible choice for a turn server is Coturn. [Coturn configuration](https://nextcloud-talk.readthedocs.io/en/latest/coturn/).

To configure coturn you have to use a new server or new dedicated Ip address (not the one that already serves the nextcloud website) because the turn protocol blocks the port 443 that is usually used for https and [it is not possible to configure a reverse proxy](https://github.com/processone/eturnal/issues/18) to serve multiple contents on that port.

So create a new (e.g. debian) server with a domain `<your choosen turn server domain>` pointing to it.

#### Install coturn:
`apt install coturn`

Enable the deployed sysvinit service by modifying `/etc/default/coturn`:
`sudo sed -i '/TURNSERVER_ENABLED/c\TURNSERVER_ENABLED=1' /etc/default/coturn`

Allow the turn server to bind to privileged ports even if it runs as turnserver user:
`setcap cap_net_bind_service=+ep /usr/bin/turnserver`

#### Config
Modify `/etc/turnserver.conf` in the following way:
- Uncomment `listening-port=3478`
- Add a sectret generated with `openssl rand -hex 32` to `static-auth-secret=` and uncomment
- Uncomment `fingerprint`
- Uncomment `use-auth-secret`
- Add `<your choosen turn server domain>` to `realm=`and uncomment.
- Uncomment `total-quota=0`. This are the allowed simultaneous connections. For DoS attack prevention set it to some number (maybe 300?) but for max availability set it to unlimited (0).
- Uncomment `bps-capacity=0`
- Uncomment `stale-nonce=600`
- Uncomment `no-multicast-peers`
- Uncomment `no-stdout-log`
- Uncomment `log-file=` and set the value tols  `/var/tmp/turn.log`
- Uncomment (if not already done) `syslog`
- Uncomment `simple-log`

Add the following lines to prevent forwarding to private network adresses:
```
denied-peer-ip=10.0.0.0-10.255.255.255
denied-peer-ip=172.16.0.0-172.31.255.255
denied-peer-ip=192.168.0.0-192.168.255.255
denied-peer-ip=100.64.0.0-100.127.255.255
denied-peer-ip=169.254.0.0-169.254.255.255
denied-peer-ip=192.0.0.0-192.0.0.255
denied-peer-ip=192.0.2.0-192.0.2.255
denied-peer-ip=198.18.0.0-198.19.255.255
denied-peer-ip=198.51.100.0-198.51.100.255
denied-peer-ip=203.0.113.0-203.0.113.255
denied-peer-ip=fc00::-fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=fe80::-febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=::ffff:0:0-::ffff:ffff:ffff
denied-peer-ip=64:ff9b::-64:ff9b::ffff:ffff
denied-peer-ip=64:ff9b:1::-64:ff9b:1:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=2001::-2001:1ff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=2001:db8::-2001:db8:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=2002::-2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff
```


#### Logging

System logs of coturn can be seen via
`journalctl -u coturn`
#### SSL

Create certificate
`certbot certonly --standalone -d <your choosen turn server domain>`

The certificate can not be read from turnserver because it is not root so it has to be copied to a readible version

```
mkdir /etc/coturn
mkdir /etc/coturn/certs
bash
umask 077
cp /etc/letsencrypt/live/<your choosen turn server domain>/fullchain.pem /etc/coturn/certs/
cp /etc/letsencrypt/live/<your choosen turn server domain>/privkey.pem /etc/coturn/certs/
exit
chown turnserver /etc/coturn/certs/*
chmod 400 /etc/coturn/certs/*
```

Modify `/etc/turnserver.conf` and add the certificate paths:
- Uncomment `cert=` and set it to `/etc/coturn/certs/fullchain.pem`
- Uncomment `pkey=` and set it to `/etc/coturn/certs/privkey.pem`

##### Set up a letsencrypt hook
As explained [here](https://serverfault.com/questions/849683/how-to-setup-coturn-with-letsencrypt) you can copy the following code in
`/etc/letsencrypt/renewal-hooks/deploy/coturn-certbot-deploy.sh`

```
#!/bin/sh
set -e
for domain in $RENEWED_DOMAINS; do
        case $domain in
        <your choosen turn server domain>)
                daemon_cert_root=/etc/coturn/certs
                umask 077
                cp "$RENEWED_LINEAGE/fullchain.pem" "$daemon_cert_root/fullchain.pem"
                cp "$RENEWED_LINEAGE/privkey.pem" "$daemon_cert_root/privkey.pem"
                chown turnserver "$daemon_cert_root/fullchain.pem" \
                        "$daemon_cert_root/privkey.pem"
                chmod 400 "$daemon_cert_root/fullchain.pem" \
                        "$daemon_cert_root/privkey.pem"
                systemctl restart coturn >/dev/null
                ;;
        esac
done
```
(==Important:== Replace `<your choosen turn server domain>`)

Set permissions:
`chmod 700 /etc/letsencrypt/renewal-hooks/deploy/coturn-certbot-deploy.sh`

Edit crontab with `crontab -e`
Add:
```
17 3 * * 2 /usr/bin/certbot renew >> /var/log/le-renew.log
```

### Configuration in Nextcloud

In Nextcloud admin account:
Navigate to Administration Settings (top right corner menue)
Navigate to Talk (left sidebar)
Scroll down to STUN servers
change `stun.nextcloud.com:443` to `<your choosen turn server domain>:443`

## Enable HTTP Strict Transport Security 

Add to all apache virtual host files that listen on 443 directly after the ServerName row:
```
<IfModule mod_headers.c>
      Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains"
</IfModule>
```
You can also add `; preload` directly after includeSubDomains in order to add the server to a preload list that is hard coded into browsers. 
==WARNING:== this has long term consequences for all subdomains [as described here](https://hstspreload.org/).
## Nextcloud backup

[docs](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/backup.html)

## Lets Encrypt

Make sure that the automatic certificate refreshing is enabled.
Edit the `crontab` using the command:
`crontab -e`
## Security

Check the security & setup warnings in your nextcloud admin account by navigating to administration settings (top right corner menu) > overview

