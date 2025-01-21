# etc crontab syntax bug

In the file `/etc/crontab`the following line works correctly and writes A to `/root/cronlog`

```
* * * * * root echo A >> /root/cronlog 2>&1
```

for some reason this line does not work

```
* * * * * root echo B &>> /root/cronlog
```

In bash both commands execute as expected

```
echo C >> /root/cronlog 2>&1
echo D &>> /root/cronlog
```


Also [escaping percentage sighns](https://serverfault.com/questions/274475/escaping-double-quotes-and-percent-signs-in-cron) is necessary or an error will occour




Both bugs occurred when setting up cron jobs on the [main server](../server/main-server-setup-instruction.md).