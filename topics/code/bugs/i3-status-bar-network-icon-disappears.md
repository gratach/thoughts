# i3 status bar network icon disappears

When using multiple screens with i3 window manager the network manager icon disappears from the status bar after removing the additional screen.

### Fix
Add `tray_output primary` to the i3 config file (`~/.config/i3/config`) in the `bar` block like this:

```
bar {
         tray_output primary
         status_command i3status
}
```

refresh with `$mod+Shift+c` 