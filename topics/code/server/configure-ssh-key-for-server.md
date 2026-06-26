# Configure ssh key for server

### Create a new ssh key

```
ssh-keygen
```

Enter the path of the key
Set a password or let free for no password

The command creates a private key at the location of the entered path and a public key at the same file path with a .pub extension

### Reset known hosts

Only necessary if the server is already known but has changed its identity e.g. due to rebuild
In this case the ssh connection is refused with a message `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`.

To forget the previous server identity type the following with the ip address `<ip address>`

`ssh-keygen -R <ip address>`

### Copy the key to the server

```
ssh-copy-id -i <public key path> <username>@<ip address>
```

Here `<public key path>`is the path of the generated public key on the client
`<username>`is the name of the linux user that wants to log in on the server (e.g. root)
`<ip address>`is the ipv4 or ipv6 address of the server (on [Hetzner](../../software/infastructure/hetzner.md) servers the ipv6 address can be obtained by replacing the /64 of the network mask by an 1)

If the fingerprint of the server is not yet registered it has to be confirmed. Check the key fingerprint on the server with `ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub` and compare it to the one from ssh-copy-id. (`_`can be typed by pressing `?` on [german keyboard with english keyboard setting](debian-change-keyboard-setting-to-german.md)).
This command saves the public key in the file `~/.ssh/authorized_keys` in the home directory of the respective user on the server

## SSH access

```
ssh -i ~/.ssh/<path-to-key> -o IdentitiesOnly=yes <user>@123.456.123.456
```
Replace `123.456.123.456` with your IP address

### Configure a ssh shortcut on the client

a ssh shortcut to a server `<username>@<ip address>` can be configured in file `~/.ssh/config` in the home directory of the client

To implement this add the following lines to the file:
```
Host <shortcut>c-l c-

        HostName <ip address>
        User <username>
        IdentityFile <path to private key>
        IdentitiesOnly yes
```
The server can now be accessed via

`ssh <shortcut>`

## IPv6

If your server is available via an IPv6 address run:
```
ssh -6 -i ~/.ssh/<path-to-key> -o IdentitiesOnly=yes <user>@1234:1234:1234:1234::1
```
Alternatively use the following config file:
```
Host claw
	HostName @1234:1234:1234:1234::1
	User <user>
	AddressFamily inet6
	IdentityFile /home/user/<path-to-key>
	IdentitiesOnly yes
```