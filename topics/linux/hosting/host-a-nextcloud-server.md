# Host a nextcloud server

A nextcloud server can be hosted as described in the [official documentation](https://docs.nextcloud.com/server/latest/admin_manual/index.html).

There is a App in Hetzner that includes a default installation. The hetzner default image can be configured via console on the first console connection. The console installation asks you to select your url. Choose `<your choosen nextcloud url>` a url that points to your server 

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

When [setting up the ssl configuration](https://sdk.collaboraonline.com/docs/installation/Configuration.html#ssl-configuration) for Collabora Online the service can be configured with ssl termination which means that a sssl termination proxy handles the ssl requests and passes them on unencrypted to the collabora service.

To change the collabora ssl settings open `/etc/coolwsd/coolwsd.xml` navigate to the `<ssl>` tag and set the `<enable>` tag from true to false and the `<termination>` tag from false to true.

Change the listen address where collabora binds to to localhost because we are using an reverse proxy to forward requests from the main IP address to the localhost: Navigate to `<net>` and change the `<listen>`tag from any to loopback.

To allow your nextcloud server to use the collabora server set the storage.wopi.host to the url of the nextcloud: Therefore navigate to `<storage>`, `<wopi>` and change the `<host>` tag to your choosen nextcloud url without `https://`.

All these changes of the `/etc/coolwsd/coolwsd.xml` file can also be done with coolconfig.
e.g. `sudo coolconfig set ssl.enable false`

Set the admin password for using the collabora admin account:
`sudo coolconfig set-admin-password`
You can access the admin account in the browser by calling:
`<your choosen collabora url>/browser/dist/admin/admin.html`
This gives you information about usage.

To refresh the settings run:

`systemctl restart coolwsd`

### Collabora reverse proxy

You have to chose a url `<your choosen collabora url>` that points to the server where you installed collabora.

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
certbot certonly -n --apache -d <your choosen collabora url>
```

Add a new server configuration file `collabora.conf` to `/etc/apache2/sites-available/` that has the following content:

```
<IfModule mod_ssl.c>
	<VirtualHost *:443>
		ServerAdmin webmaster@localhost
		ServerName <your choosen collabora url>
		ServerAlias www.<your choosen collabora url>
		SSLCertificateFile /etc/letsencrypt/live/<your choosen collabora url>/fullchain.pem
		SSLCertificateKeyFile /etc/letsencrypt/live/<your choosen collabora url>/privkey.pem

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
Replace `<your choosen collabora url>` with the actual url (without `https://`)

This configuration requires collabora to listen on IPv6 port. Make sure that is the case.

Create a symlink from `sites-enabled` to this configuration.
`ln -s /etc/apache2/sites-available/collabora.conf /etc/apache2/sites-enabled/collabora.conf` 

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
Enter `https://<your choosen collabora url>`
Press Save

