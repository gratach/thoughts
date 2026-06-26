# Using capslock as modifier key in i3

As explained [here](https://faq.i3wm.org/question/6430/remapping-both-caps-lock-and-windows-key/index.html) you can define keyboard shortcuts in i3 that start with capslock by creating a file `~/.Xmodmap` in dom0 that has the following content:
```
clear lock
keycode 66 = Hyper_R
add mod3 = Hyper_R
```
You can then add lines like the following in `~/.config/i3/config`:
```
bindsym mod3+a exec "<your-command>"
```
You need to lock out of your i3 session and log in again to make your changes take effect.
