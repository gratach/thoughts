# Zettlr

Zettlr is a software for creating a markdown knowledge base.

## Maintaining relative links

Links in Zettlr are written in the following way:

```
[[file-name-of-the-link|visible-link-name]]
```

They can be converted into relative markdown links by using the script that can be found in `.commands/make_links_relative.py` (Also available [Here](https://github.com/gratach/thoughts/blob/master/.commands/make_links_relative.py)).

This script needs to be located in a folder that is contained in the base folder of the knowledge base. It needs a command line argument that is the path of the file whose links need to be changed.

This file name can be obtained by right clicking on the according markdown tab in zettlr and chosing  `Copy path`.

When using the [Debian i3 PC setup](../linux/debian-i3-pc-setup.md) the script can be executed by typing `c-l <path-of-link-file>` in the console.

## See also
[Install Zettlr in a Qubes template](../../linux/qubes/install-zettlr-in-a-qubes-template.md)