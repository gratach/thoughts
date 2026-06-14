# Configure a Linux mail server

[Detailed tutorial using POSTFIX](https://www.linuxbabe.com/mail-server/setup-basic-postfix-mail-sever-ubuntu)

## Set dns records

Choose a mail domain `<your mail domain>` that forms the end of the email address: `<user name>@<your mail domain>` e.g. `me@example.com`.
Select a subdomain `<your mail subdomain>` of `<your mail domain>` that form together the host name `<your mail subdomain>.<your mail domain>` of the server like `mail.example.com`.

Set a `AAAA` and `A` records for `<your mail domain>` and `<your mail subdomain>` pointing to the server.

Set a `MX` record for `<your mail domain>` with `{priority: 10, value: <your mail subdomain>.<your mail domain>, TTL: 86400}`

## Install postfix

`apt install postfix`
Select postfix configuration "Internet site"
Select `<your mail domain>`  as the system mail name

## Set mailbox size limit

Set a maximum mailbox size by editing the line starting with `mailbox_size_limit =` in the file `/etc/postfix/main.cf` and change it into:
```
mailbox_size_limit = 30000000
```
Restart the mail server and restart the system
```
postfix reload
reboot now
```
## Testing sending and receiving mails

Send mail
```
echo "Some text" | sendmail my@mailaddress.com
```
Received mails end up in the file `/var/mail/<username>`

## Rejecting all incoming mail

Edit `/etc/postfix/main.cf` and set `inet_interfaces` to `loopback-only` as described [here](https://superuser.com/questions/430023/in-postfix-how-could-i-disable-incoming-mail).

In order for this change to take effect run `postfix reload` and restart the server.

## Automatic upgrades

See [this guide](automatic-upgrades.md)

## Strange MX record behavior 

[MX Records on Hetzner are strange](https://docs.hetzner.com/dns-console/dns/manage-records/managing-mx-records)
If the target domain name is the same as the current one one has to write only the subdomain without the domain. So "mail" instead of "mail.example.com". If the target is different the domain name has to end with a dot. If the target domain name is the same as the current one and the full domain name ending with a dot is specified in the record sending mails per GMX does not work for some reason.
