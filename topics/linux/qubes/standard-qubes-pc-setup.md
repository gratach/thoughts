# Standard Qubes PC setup

[Qubes OS](qubes-os.md) can be downloaded [here](https://www.qubes-os.org/).
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

## Change the keyboard shortcuts

To change the keyboard shortcuts you can edit `./config/i3/config` and add a line like `bindsym $mod+i exec "your command"`
Apply the changes with the refresh command `$mod+Shift+c` by default.
The names of the keys can be obtained by typing `xev -event keyboard` in a not dom0 terminal focus the window that pops up and press the key of intrest. In the terminal a line like `state xx keycode xx (keysym xx, <your-key-name>) same_screen XX` appears that contains your key name.

[Using capslock as modifier key in i3](using-caps-lock-as-modifyer-file-in-i3.md)

## Setup copy mechanism

In the `~/.bashrc` of all individual qubes add the following lines:
```
# Move qubesIncoming to current working directory
m-q() {
    shopt -s dotglob nullglob
    mv ~/QubesIncoming/*/* .
    shopt -u dotglob nullglob
}
alias q-m=qvm-move
```
This way you can move files and directories fast between qubes by typing in the source qube
```
q-m <name-of-file-or-directory>
```
entering the target qube name in the gui form
and by typing in the target qube in the correct current working dir:
```
m-q
```
Make sure to keep your QubesIncoming dirs always clean and empty or else you will copy unwanted debris in your current working directory when using this command. 

## Enable prining

See [Printing in Qubes](printing-in-qubes.md)