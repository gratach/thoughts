# Install Mobian on PinePhone

[Install description](https://wiki.debian.org/InstallingDebianOn/PINE64/PinePhone)

## Tow-Boot

Bevore installing Mobian Tow-Boot has to be installed on the PinePhone.

Download the Tow-Boot image from [this GitHub Repo](https://github.com/Tow-Boot/Tow-Boot/releases).
Choose the latest and download the `pine64-pinephoneA64-*.tar.xz` tar archive.

Extract the tar archive and follow [these instructions](https://tow-boot.org/devices/pine64-pinephoneA64.html):

Flash the `mmcboot.installer.img` to a suitable SD card:
```
dd if=mmcboot.installer.img of=/dev/XXX bs=1M oflag=direct,sync status=progress
```
==Replace the XXX with the correct device. Select the right one or you can overwrite important data of your computer==

Put the SD card in the PinePhone and restart it. Connect it to a charger while booting.

Select "Install Tow-Boot to eMMC Boot".

Romove SD card and restart.

## Installer Image

Usually you can flash the installer image on the sd card but due to [this issue](https://codeberg.org/Calamares/calamares-extensions/issues/33) it is not possible to use the latest mobian installer on the PinePhone

## Flash the PinePone directly with JumpDrive

Instead you can use the installation method using JumpDrive.

Download the pine64-pinephone.img.xz from [this source](https://github.com/dreemurrs-embedded/Jumpdrive/releases/).

Unpack it with 
`unxz pine64-pinephone.img.xz`

Flash it to the SD card with
```
dd bs=64k if=<path-of-the-unpacked-image> of=/dev/<the-name-of-the-sd-card-device> status=progress
```
==Replace `<the-name-of-the-sd-card-device>`with the actual device name. Choose the right one or you will overwrite important data==

Put it in the PinePhone restart and follow the instructions on the screen. Plug the phone to your PC.

Download the mobian image from [here](https://images.mobian.org/sunxi/). Use the `mobian-sunxi-phosh-*.img.xz`

Unpack it with 
`unxz mobian-sunxi-phosh-*.img.xz`

When flashing the Mobian image to the [PinePhone](pinephone.md) using JumpDrive the device can be found out using
```
lsblk -o NAME,SIZE,VENDOR,MODEL
```
Flash to the device with VENDOR=JumpDriv and MODEL=e_eMMC

Flash with
```
dd bs=64k if=mobian-sunxi-posh-<insert-version-number-here>.img of=dev/<insert-the-e_eMMC-device-name-from-above> status=progress
```
==Be careful do not enter the wrong device or you can overwrite your computers storage or operating system==
