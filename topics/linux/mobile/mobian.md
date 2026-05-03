# Mobian

[Mobian](https://www.mobian.org/) is an mobile linux operating system that is derived from [Debian](../debian/debian.md).

## Add cusom keyboards

The keyboard kan be customized using squeekboard.

Install squeekboard:
```
sudo apt install squeekboard
```
Set it as default using
```
sudo update-alternatives --config Phosh-OSK
```
Shutdown and restart device.

A customized keyboard that supports specific keys like arrow keys can be installed like this:

Get the keyboard from a source like [this one](https://github.com/mikeshenson/Phosh-Squeekboard-Keyboard):
```
git clone https://github.com/mikeshenson/Phosh-Squeekboard-Keyboard
```
Copy the files to the correct location:
```
mkdir -p ~/.local/share/squeekboard/keyboards/
cp Phosh-Squeekboard-Keyboard/* ~/.local/share/squeekboard/keyboards/
```

## Disabeling the haptic feedback for the keyboard

All haptic feedback can be disabled with
```
gsettings set org.sigxcpu.feedbackd profile silent
```
It can be enabled again with
```
gsettings set org.sigxcpu.feedbackd profile silent
```

## Install and configure file manager

As described [here](https://forum.pine64.org/showthread.php?tid=18273) and [here](https://www.youtube.com/watch?v=-nbUXABJw0c&list=PLUd45KipRCgiaJC8EeDBCcPixZG94pj99&index=4) the file manager pcmanfm is a good choice for Mobian.

Install with
```
sudo apt install pcmanfm
```
By default doubleclicking on a folder to open it does not work but it can be configured by selecting

View > Folder View > Detailed List View

The sidebar can be disabled by deselecting:

View > Side Pane > Show Side Pane