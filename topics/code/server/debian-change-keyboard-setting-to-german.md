# Debian change keyboard setting to German

```
dpkg-reconfigure keyboard-configuration
```

The `-`character can be typed by using the German `ß` key. `z` and `y` are swapped.

Select default keyboard model (generic 105 key pc)
Select language German
Select default options

```
setupcon
update-initramfs -u
```

Reboot the server

## Key mapping

When using a german keyboard on an server with english keyboard settings the mapping is the following:

| German key | English character |
| ---------- | ----------------- |
| ?          | _                 |
| ü          | `[`               |
| _          | ?                 |
| ;          | <                 |
| :          | >                 |
| >          | >                 |
| <          | <                 |
| ö          | ;                 |
| ä          | `'`               |
| `'`        | \|                |
| \`         | +                 |
| ´          | =                 |
| +          | ]                 |
| `*`        | }                 |
| =          | )                 |
| )          | (                 |
| /          | &                 |
| &          | ^                 |
| %          | %                 |
| $          | $                 |
| $          | #                 |
| "          | @                 |
| !          | !                 |
| ^          | \`                |
| °          | ~                 |
| -          | /                 |
| #          | \\                |
| ß          | -                 |
| y          | z                 |
| z          | y                 |
| shift ü    | {                 |
| shift ä    | "                 |
| shift ö    | :                 |
