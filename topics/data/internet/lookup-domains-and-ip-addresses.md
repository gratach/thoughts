# Lookup domains and IP addresses

The IP Address of a domain can be found out from the linux console by typing:

```
nslookup <name-of-the-domain>
```
It returns a result like:
```
Server:		<ip-address-of-the-dns-server-that-is-used>
Address:	<ip-address-of-the-dns-server-that-is-used-with-port>

Non-authoritative answer:
Name:	<name-of-the-looked-up-url>
Address: <ipv4-address-of-the-looked-up-url>
Name:	<name-of-the-looked-up-url>
Address: <ipv6-address-of-the-looked-up-url>

```
When the domain has changed recently the latest changes may not be available in the prompted dns server.
To obtain the latest information you can write:

`nslookup -type=soa <name-of-the-domain>`

This returns the start of authority dns server formatted like this:
```
Server:		<ip-address-of-the-dns-server-that-is-used>
Address:	<ip-address-of-the-dns-server-that-is-used-with-port>

Non-authoritative answer:
google.com
	origin = <the-primary-name-server-of-the-domain>
	mail addr = <email-addres-of-administrator-without-at>
	serial = <serial-number>
	refresh = <refresh-time-in-seconds>
	retry = <retry-time-in-seconds>
	expire = <expire-time-in-seconds>
	minimum = <minimum-cache-time-in-seconds>

```
The `<the-primary-name-server-of-the-domain>` information can now be used to get the latest ip information:
```
nslookup <name-of-the-domain> <the-primary-name-server-of-the-domain>
```


## Applications

This can be used for [finding the ip address of spam emails to report them](../../software/security/redirect-spam-mails.md).