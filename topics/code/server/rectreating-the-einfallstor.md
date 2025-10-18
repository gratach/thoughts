
# Recreationg the einfallsor

To recreate the einfallstor go to Hetzner and rebuild a server with the `dritt-server-mit-einfallstor` snapshot.

Login as root using the dritt ssh key in elefantpc.

Run:

```
su zombie
cd ~
nohup python3 /home/netzablage/prog.py < /dev/null &> /dev/null &
```

Make sure that the domains are pointing to the correct server.