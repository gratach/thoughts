# Install i3 on Qubes

[i3 on the official qubes os documentation](/home/user/Documents/projects/thoughts/topics/software/content/install-zettlr.md)

To install i3 on qubes open a dom0 console and run
```
sudo qubes-dom0-update i3 i3-settings-qubes
```
## Configure i3 on qubes

Use the Win key for the default config.
Add the following to `~/.config/i3/config`
```
# Turn off bell
exec --no-startup-id xset b off 

# Brightness control
bindsym XF86MonBrightnessUp exec brightnessctl set +2%
bindsym XF86MonBrightnessDown exec brightnessctl set 2%-

# Screenshots
bindsym Print exec --no-startup-id "gnome-screenshot"
bindsym Shift+Print exec --no-startup-id "shutter -s -e"

# Move workspaces between monitors
bindsym $mod+Shift+period move workspace to output right
bindsym $mod+Shift+comma move workspace to output left

# Add and remove second monitor
bindsym $mod+period exec "xrandr --output HDMI-2 --auto --right-of eDP-1"
bindsym $mod+comma exec "xrandr --auto"

# Dark mode toggle
bindsym $mod+n  exec "/home/gratach/.config/i3/toggle-color"

# Qubes manager
bindsym $mod+q exec "qubes-qube-manager"

# Browser
bindsym $mod+b exec "qvm-run <standard-vm-name> firefox"
bindsym $mod+Shift+b exec "qvm-run <private-vm-name> firefox"

# Shortcut for menu key
bindsym --release $mod+m exec --no-startup-id "xdotool key Menu"
```
Replace `<standard-vm-name>` and `<private-vm-name>` with your actual vm names.

## Clipboard

Configure the clipboard to use Win+C and Win+V to copy and paste between the Qubes vms and the global clipboard by opening the "Qubes global config" navigating to "Clipboard" and changing the key bindings.

Change in the i3-config `bindsym $mod+v` into `bindsym $mod+j` (remove the default `$mod+j` keybinding)

## Configure screenshots

To configure screenshots in i3 run in dom0 terminal:
```
sudo qubes-dom0-update gnome-screenshot shutter
```
Every screenshot is stored in the ~/Pictures folder in dom0. (Gnome-screenshot screenshots are called "Screenshot from XXX" and shutter screenshots are called Selection_XXX)
To move a screenshot to a other qube vm run in dom0 terminal:
```
qvm-move-to-vm <name-of-the-vm> ~/Pictures/<name-of-the-screenshot>
```
==There is a bug when taking screenshots using shutter:== 
When you start the screenshot multiple times before it loads it blocks the gui after saving the first screenshot. Pressing escape does not help.
**Fix:** To solve this bug select an area with the mouse, right-click to open the menu and then press escape. 

## See also:
[Debian i3 PC setup](../../tools/linux/debian-i3-pc-setup.md)