# Qubes OS

[Qubes OS](https://en.wikipedia.org/wiki/Qubes_OS) is an operating system that builds on virtual machines running other operating systems like Debian and Fedora.
[Official website](https://www.qubes-os.org/)

## Copy files between Qubes VMs

Files can be copied or moved between qubes VMs using the commands
```
qvm-copy <file-or-directory>
qvm-move <file-or-directory>
```
A dom0 window pops up where you can select the target vm.
The file or directory appears in `~/QubesIncoming/<source-vm-name>`

If you follow the setup instrucions in [Standard Qubes PC setup](standard-qubes-pc-setup.md) you can copy from one working directory to another with:
`q-c`
and
`c-q`

## See also:
[Standard Qubes PC setup](standard-qubes-pc-setup.md)
[Install Zettlr in a Qubes template](install-zettlr-in-a-qubes-template.md)