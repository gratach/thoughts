# Standard Qubes PC setup

Qubes OS can be downloaded [here](https://www.qubes-os.org/).
[Flash image on stick](../basics/flash-image-on-stick.md)
[Install Linux](../basics/install-linux.md)
[Install Zettlr in a Qubes template](install-zettlr-in-a-qubes-template.md)
[Install i3 on Qubes](install-i3-on-qubes.md)
[Add applications to Qubes OS](add-applications-to-qubes-os.md)

## Enable IPV6

Run as described [here](https://doc.qubes-os.org/en/latest/developer/system/networking.html) in dom0 terminal:
```
qvm-features sys-net ipv6 1
```
Restart the sys-net qube and the current qube.
Sometimes you have to retry to sucessfully establish a connection.

See also [Configure ssh key for server](../../code/server/configure-ssh-key-for-server.md)

## Get overview over the CPU usage of all qubes
An overview over the CPU usage of the qubes can be received using:
```
xentop
```
