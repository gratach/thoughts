# Listen on a different ip

When using hetzner servers each server gets assigned to a ipv6 address space like `1234:5678:90ab:cdef::/64`. The 64 means that the first 64 bits are part of the network prefix and the rest are the host addresses (which can be assigned).

When a server should listen on more than one of these addresses it can be configured in [netplan](https://wiki.ubuntuusers.de/Netplan/) by adding a new entry to `/etc/netplan/<name-of-the-file>` in `network.ethernets.eth0.addresses`.

To apply this setting temporary:
`sudo netplan try -timeout 180`
where 180 are the seconds until reset.

To apply permanently:
`sudo netplan apply`

## Specifying the listen IP in Apache

Edit `/etc/apache2/ports.conf`
Instead of `Listen 80`type `Liste [1234:5678:90ab:cdef::9]:80
as described [here](https://httpd.apache.org/docs/2.4/bind.html)

After that the new IP address needs to be configured in the `/etc/apache2/sites-available/<name-of-vhost>.conf` file like:
`<VirtualHost [1234:5678:90ab:cdef::9]:80>`

## See also
[host-a-website-on-a-different-port](host-a-website-on-a-different-port.md)