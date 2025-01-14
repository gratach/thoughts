# Configure a Linux mail server

[Detailed tutorial using POSTFIX](https://www.linuxbabe.com/mail-server/setup-basic-postfix-mail-sever-ubuntu)

### Testing sending and receiving mails

Send mail
```
echo "Some text" | sendmail my@mailaddress.com
```
Received mails end up in the file `/var/mail/<username>`

### Strange MX record behavior 

[MX Records on Hetzner are strange](https://docs.hetzner.com/dns-console/dns/manage-records/managing-mx-records)
If the target domain name is the same as the current one one has to write only the subdomain without the domain. So "mail" instead of "mail.example.com". If the target is different the domain name has to end with a dot. If the target domain name is the same as the current one and the full domain name ending with a dot is specified in the record sending mails per GMX does not work for some reason.
