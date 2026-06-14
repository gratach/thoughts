# Install Zettlr

The [Zettlr](../../tools/writing/zettlr.md) software can be installed using the [official instructions for Debian/Ubuntu](https://apt.zettlr.com/):
```
curl -s --compressed "https://apt.zettlr.com/KEY.gpg" | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/zettlr_apt.gpg > /dev/null
sudo curl -s --compressed -o /etc/apt/sources.list.d/zettlr.list "https://apt.zettlr.com/zettlr.list"
sudo apt update
sudo apt install zettlr
```
See also:
[Install Zettlr in a Qubes template](../../linux/qubes/install-zettlr-in-a-qubes-template.md)


