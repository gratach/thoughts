# Add applications to Qubes OS

As described [here](https://dataswamp.org/~solene/2023-05-14-qubes-os-custom-application.html) applications can be added to [Qubes OS](qubes-os.md) by adding files named `<name-of-the-application>.desktop` to `~/.local/share/applications`

These files need to contain the following:
```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=False
Exec=/home/user/path/to/the/application
Name=<name-of-the-application>
```
The application can now be added in the qubes manager via `selected qube > right klick > Settings > Applications > Refresh Applications > Move it via arrow to the right side`
