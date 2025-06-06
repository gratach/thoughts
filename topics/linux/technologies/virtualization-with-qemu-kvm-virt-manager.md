# Virtualization with qemu & kvm & virt-manager

### Setup

Virtualization setup as described in [this tutoruial](https://linuxconfig.org/setting-up-virtual-machines-with-qemu-kvm-and-virt-manager-on-debian-ubuntu)

Switch to root
```bash
su -
```

Install required packages
```bash
apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```

Add the existing nonroot user to the two groups libvirt and kvm
```bash
adduser <name of the user> libvirt
adduser <name of the user> kvm
```

Check if the libvirt service is running

```bash
systemctl status libvirtd
```

If the service is not running start it

```bash
systemctl start libvirtd
systemctl enable libvirtd
```