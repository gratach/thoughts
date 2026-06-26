# Recurring tasks

Scripts that get executed on a regular basis can be implemented using Crontab ([source](https://linuxhandbook.com/crontab/)).

## Crontab

Depending on the distro the crontab configuration is saved in directories like `/var/spool/cron/crontabs/`.

The crontab configuration file can be edited with `crontab -e`
To edit the crontab configuration of a specific user run `crontab -u <name-of-linux-user> -e`

It has the following format:
```
<minute (0-59)> <hour (0-23)> <day of month (1-31)> <moth of year (1-12)> <day of week (0-6) start with sunday> <command>
```
Instead of a number for one of these fields an asterisk (`*`) can be used to allow every possible input for this field.

## Time zone

Chrontab uses the time zone of your system.
Get the current zone with:
```
timedatectl
```
Set UTC as time zone:
```
timedatectl set-timezone UTC
```

### Advanced

Fields can have one of these formats:
|Description|Example|
|---------------|---------|
|        Arbitrary       |        `*`       |
|      List     |    `1,5,6`    |
|        Range       |        `1-3`       |
|          Every nth time          |          `*/3`          |

`1,5,6` 

### Example:
```
17 3 * * 2 /usr/bin/certbot renew >> /var/log/le-renew.log
```
Execute on minute 17 of hour 3 every Tuesday.

## Bugs

[etc crontab syntax bug](../../code/bugs/etc-crontab-syntax-bug.md)

