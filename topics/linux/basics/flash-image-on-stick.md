# Flash image on stick

Download your image e.g. from the website of the distro.

To find your USB stick where you want to flash your image for installation list all USB devices that are available in your system:
```
lsblk -o NAME,SIZE,VENDOR,MODEL
```
USB sticks are often called sbX where X can be (a, b, c, ...).
You can find out which device is your stick by removing and reinserting it.
The partitions on the USB stick are then called sbXY where Y can be (1, 2, 3, ...).  Do not flush on a partition but directly on the stick.

You can flush the stick by running as root:
```
dd bs=64k if=<path-of-the-image> of=/dev/<the-name-of-the-stick> status=progress
```
==Replace `<the-name-of-the-sd-card-device>`with the actual device name. Choose the right one or you will overwrite important data==


See also:
[Install Mobian on PinePhone](../mobile/install-mobian-on-pinephone.md)
[Install Linux](install-linux.md)
[Standard Qubes PC setup](../qubes/standard-qubes-pc-setup.md)