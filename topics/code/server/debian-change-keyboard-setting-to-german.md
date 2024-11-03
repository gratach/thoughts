# Debian change keyboard setting to German

```
dpkg-reconfigure keyboard-configuration
```

Select default keyboard model (generic 105 key pc)
Select language German
Select default options

```
setupcon
update-initramfs -u
```

Reboot the server