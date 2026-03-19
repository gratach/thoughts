# Configure i3 darkmode

To toggle between dark-mode and light-mode the following script can be used:

```
#!/bin/bash

current=$(gsettings get org.gnome.desktop.interface color-scheme)
if [ $? -ne 0 ]; then echo "Could not fetch current color-scheme" >&2; exit 1; fi
echo "Current color-scheme: $current"

profile=$(gsettings get org.gnome.Terminal.ProfilesList default)
profile=${profile:1:-1}

case "$current" in
        "'prefer-dark'") 
                new_color_scheme="prefer-light"
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" use-theme-colors false
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" foreground-color '#2e3440'
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" background-color '#ffffff' 
                ;;
        "'prefer-light'"|"'default'") 
                new_color_scheme="prefer-dark"
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" use-theme-colors false
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" foreground-color '#cdd6f4'
                gsettings set "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/" background-color '#1e1e2e'
                ;;
esac

echo "New color-scheme: $new_color_scheme"

if ! $(gsettings set org.gnome.desktop.interface color-scheme "$new_color_scheme"); then
        echo "Could not set new color-scheme" >&2
        exit 1
fi

```

It is inspired by [this article](https://iamnearlythere.com/dark-mode-ubuntu-i3/)

The scripts asserts that you use [gnome-terminal](gnome-terminal.md) which does not support automatic adaption to system dark mode so it does the configuration manually.