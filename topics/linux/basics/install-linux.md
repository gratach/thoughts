# Install Linux

### 1) 
Download image
	Debian:
		[Download](https://www.debian.org/)
		Create automatic installation images with fai
			[Create Image](https://fai-project.org/FAIme/)
	Fedora:
		[Download](https://fedoraproject.org/workstation/)
	Arch Linux:
		[Download](https://archlinux.org/download/)
	
### 2) 
Write image to usb stick
	Find out the name of the usb device
		Compare with stick in and out:
			Option 1
				`cat /proc/partitions`
			Option 2
				`ls /dev`
	Copy the image to the stick
		Option 1
			`cp <path to iso file> <name of device>`
			`sync`
		Option 2
			using dd
### 3) 
Boot PC with stick and go to uefi
	Find out what key to press when booting the pc to get to uefi
		Enter
		f12
	Select stick as boot device
	Proceed with installation
	After installation select default as boot device again