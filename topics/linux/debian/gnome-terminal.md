# GNOME Terminal

For the gnome terminal the [dark mode can be configured on i3 in the following way](configure-i3-darkmode.md).

The top bar can be removed and restored in the following way:

```
gsettings set org.gnome.Terminal.Legacy.Settings default-show-menubar false

gsettings set org.gnome.Terminal.Legacy.Settings default-show-menubar true
```