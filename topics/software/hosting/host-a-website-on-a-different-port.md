# Host a website on a different port

It is possible to host a website on a port different to 80 or 443.

It can be accessed in the web browser like:
`https://my-site.example.com:1234`

## Configuration in Apache

As explained [here](https://stackoverflow.com/questions/3940909/configure-apache-to-listen-on-port-other-than-80):

Modify `/etc/apache2/ports.conf` and add `Listen 1234`

Modify virtual host file in `/etc/apache2/sites-enabled` in the following way:
`<VirtualHost *: 1234>`

Restart Apache:
`systemctl reload apache2`

## See also
[listen-on-a-different-ip](listen-on-a-different-ip.md)
[list-all-listening-ports](../../linux/hosting/list-all-listening-ports.md)