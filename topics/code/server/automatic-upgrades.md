# Automatic upgrades

Automatic upgrades can be implemented using unattended upgrade:

## Unattended upgades

(See [this guide](https://linuxiac.com/how-to-set-up-automatic-updates-on-debian/))
```
apt install python3-gi
apt install unattended-upgrades
apt install mailutils
```
Mailutils is needed for mailx but the previously installed postfix is needed for it to function

Edit `/etc/apt/apt.conf.d/50unattended-upgrades` and change the following:
- Uncomment the line `Unattended-Upgrade::Mail "<the-email-address-where-information-about-the-upgrade-should-be-send-to>";` and insert your email address.
- Uncomment all `Unattended-Upgrade::Origins-Pattern { "origin=..."` lines
- Uncomment line `Unattended-Upgrade::Remove-Unused-Dependencies "true";` and set the value to `true`
- Uncomment and set to true: `Unattended-Upgrade::Automatic-Reboot "true";`

Enable unattended upgrade using:
```
dpkg-reconfigure --priority=low unattended-upgrades
```
Choose Yes

Check the service status by typing:
```
systemctl status unattended-upgrades.service
```
Logs can be found in `/var/log/unattended-upgrades/`

## Set the time of the reboot

Set UTC as the default time zone of your server:
```
timedatectl set-timezone UTC
```
Check timezone with
```
timedatectl status
```
Modify `/etc/apt/apt.conf.d/50unattended-upgrades` and uncomment and change:
`Unattended-Upgrade::Automatic-Reboot-Time "HH:MM";`
Where `HH` are the hours and `MM` are the minutes of the reboot in UTC. ([Source](https://serverfault.com/questions/1152848/unattended-upgrade-configuration-time-used))
Select a time that is far away from other relevant recurring events and is not affected by leap seconds at midnight.