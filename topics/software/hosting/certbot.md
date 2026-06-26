# Certbot

Certbot is a free service provided by the [Internet Security Research Group](https://en.wikipedia.org/wiki/Internet_Security_Research_Group) that allows one to recieve a HTTPs certificate.

## Install
```
apt install certbot
certbot register
```
## Receiving certificates with Nginx
```
apt install python3-certbot-nginx
certbot certonly -n --nginx --force-renewal --cert-name your-domain.example.com -d your-domain.example.com -d optional-subdomain.your-domain.example.com -d another-optional-subdomain.your-domain.example.com
```

In Nginx you can setup an HTTPs server with
```
server{
	listen 443 ssl;
	listen [::]:443 ssl;
	
	server_name your-domain.example.com optional-subdomain.your-domain.example.com;
	ssl_certificate /etc/letsencrypt/live/your-domain.example.com/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/your-domain.example.com/privkey.pem;
    
	...
}
```

## Receiving certificates with Apache

This is not yet tested
```
apt install certbot python3-certbot-apache
certbot certonly -n --apache --force-renewal --cert-name your-domain.example.com -d your-domain.example.com -d optional-subdomain.your-domain.example.com -d another-optional-subdomain.your-domain.example.com
```
## Certificate location

Certificates from letsencrypt are saved in 
`/etc/letsencrypt/live/`

## Automatic certificate update

 Spawn an editor to edit the crontab file with the following command:

 `crontab -e`

 Add the following line:
 ```
<chose-an-minute> <chose-a-hour> * * <chose-a-day-of-the-week> /usr/bin/certbot renew >> /var/log/le-renew.log
```
See also [Recurring tasks](../../linux/basics/recurring-tasks.md)

## List all certificates
```
certbot certificates
```
## Delete certificates
```
certbot delete --cert-name your-domain.example.com
```

## Choose a new email address

This is not yet tested
```
certbot update_account -m <your-email-address>
```