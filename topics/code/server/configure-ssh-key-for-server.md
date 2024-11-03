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
`<ip address>`is the ipv4 or ipv6 address of the server (on hetzner servers the ipv6 address can be obtained by replacing the /64 of the network mask by an 1)

This command saves the public key in the file `~/.ssh/authorized_keys` in the home directory of the respective user on the server

### Configure a ssh shortcut on the client

a ssh shortcut to a server `<username>@<ip address>` can be configured in file `~/.ssh/config` in the home directory of the client

To implement this add the following lines to the file:
```
Host <shortcut>
        HostName <ip address>
        User <username>
        IdentityFile <path to private key>
        IdentitiesOnly yes
```
The server can now be accessed via

`ssh <shortcut>`
