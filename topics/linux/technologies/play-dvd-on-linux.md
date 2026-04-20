# Play DVD on Linux

It is a bit complicated to [play a DVD on debian](wiki.debian.org/CDDVD).
The opensource library [libdvdcss](https://code.videolan.org/videolan/libdvdcss) can be used to decrypt them.

```
git clone https://code.videolan.org/videolan/libdvdcss.git
```
Get the latest meson version (the version on apt could be to old)
```
python3 -m venv dvdvenv
source dvdvenv/bin/activate
pip install meson
pip install ninja
```
Build and install libdvdcss
```
cd libdvdcss
meson setup build --prefix=/usr
sudo ninja -C build install
```
Install vlc player
```
apt install vlc
```