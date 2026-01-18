# List all listening ports

In order to show all listening ports on a linux device run

`sudo netstat -tunlp` 

[Source](https://linuxize.com/post/check-listening-ports-linux/)

## Beispiel output:

```
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      802/sshd: /usr/sbin 
tcp6       0      0 :::22                   :::*                    LISTEN      802/sshd: /usr/sbin 
udp        0      0 0.0.0.0:68              0.0.0.0:*                           590/dhclient
```

The IP addresses 0.0.0.0 and :: are the IPv4 and IPv6 placeholders for "listen on all IP addresses"

## See also
[host-a-website-on-a-different-port](../../software/hosting/host-a-website-on-a-different-port.md)