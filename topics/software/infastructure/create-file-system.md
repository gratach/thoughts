# Create file system

A new file system can be created on a device like an usb stick or a sd card in the following way:

1) List the available devices with the partitions and the existing file systems:
    ```
    lsblk -o NAME,SIZE,VENDOR,MODEL,FSTYPE
    ```
2) Unmount the device or partition that should be overwritten if necessary. Get a list of all mountet file systems with `cat /proc/mounts` or `findmnt`. You can unmount the device as root with `unmount /dev/<name-of-the-device>` where `<name-of-the-device>` has to be replaced.
3) Optionaly partition the device ==This will make all existing data on the device unusable do not partition the wrong device==
4) Choose a file system
    There are many different types of file systems available (see [this list](https://en.wikipedia.org/wiki/List_of_file_systems))
5) Create the file system on the device or a partition of the device. Replace `<name-of-the-device>` with the name of the device or the partition from the NAME column of the output of the lsblk prompt. ==Do not choose the wrong device or the data on your computer might be overwritten==. Run the following commands as root:
    - To create a ext4 filesysten (standard for linux) run:
       ```
       mkfs.ext4 /dev/<name-of-the-device>
       ```
   - To create a exfat filesystem (can be used on linux and windows) run:
       ```
       mkfs.exfat /dev/<name-of-the-device>
       ```
6) If needed mount the file system again as root with `mount /dev/<name-of-the-device> <path-of-the-mount-location> -o uid=<name-of-the-linux-user>` . Replace `<name-of-the-device>` with the actual name of the device, `<name-of-the-linux-user>` with the name of your current linux user and `<path-of-the-mount-location>` with the location in the file system where the device should be mountet like for example `/media/<name-of-the-linux-user>/<choose-your-own-device-name>`. By navigating to this path the files can then be written into the device.

## See also
[Install Linux](../../linux/basics/install-linux.md)
[Install Mobian on PinePhone](../../linux/mobile/install-mobian-on-pinephone.md)
       