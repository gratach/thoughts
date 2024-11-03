# Rebuilding the Hetzner server

When I rebuild an existing Hetzner server with an new image I don't get any password information or an working ssh key and can not login as root user. 

#### Solution

Click on the server in Hetzner cloud
Navigate to rescue tab
Select `Reset Root Password`

The root login via ssh might be deactivated so it is only possible to log into the server via the integrated vnc console
Open vnc console

The keyboard setting of the server might be set to English
[debian-change-keyboard-setting-to-german](../server/debian-change-keyboard-setting-to-german.md)

The ssh root access can now be temporary enabled to configure a ssh key:
Open /etc/ssh/sshd_config
change line `PermitRootLogin prohibit-password`into `PermitRootLogin yes`

Restart ssh with: `systemctl restart ssh`

The ssh key can now be configured by the client

