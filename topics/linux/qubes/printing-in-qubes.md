# Printing in Qubes

To enable printing in a Qubes vm first install cups (if not already installed)
```
sudo apt install cups
```
Make sure it is running
```
sudo systemctl start cups
sudo systemctl enable cups
```
Test if it is running
```
systemctl status cups.service
```
If it is not running it may be because you have not enabled the cups service in the qube manager settings.
If this is the case open the Qube manager. Go to settings of the vm go to services and add the cups service.
Restart the vm if necessary

Test if cubes is running and if your printer is recognized

If your printer is not recogniced you can log into your router and find out the local ip address of your printer

Test if the printer service is available and listening with
```
ping <your-local-printer-ip-address>
sudo apt install netcat-openbsd
nc -vz <your-local-printer-ip-address> 631
```
If the connection succedet open the cubes setting in your vms brower
`http://localhost:631/`

Navigate to admin and enter your vms username and password

If your vm has no password set you first need to do this with
```
passwd
```
You can unset it later with
```
passwd -d
```
If you still do not have any access you need to add your user to lpadmin group
```
sudo usermod -aG lpadmin <your-user-name>
```
In the admin panel go to `Add printer`
Select Internet printing protocol (ipp) -> Continue
Enter `ipps://<your-local-printer-ip-address>/ipp/print` -> Continue
Enter Name Description and Location (you do not need to share) -> Continue
Select the Make
Select `IPP Everywhere`
Click Add Printer