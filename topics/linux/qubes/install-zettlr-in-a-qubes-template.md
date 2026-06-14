# Install Zettlr in a Qubes template

[Zettlr](../../tools/writing/zettlr.md) can be installed in a [Qubes OS](qubes-os.md) template using the following commands:
```
sudo apt install extrepo
sudo extrepo enable zettlr
sudo apt install zettlr
```

When Zettlr is started the first time in an instance of the template it asks you for a new keyring password. If you leafe the password empty and confirm dispite of a warning it will not ask you again. When you select an password it wil ask you on every restart but continue anyway if you do not enter a password. The newly created keyring is stored in `~/.local/share/keyrings` in this directory the files `default`, `Default_keyring.keyring` and `user.keystore` get created. [Discussion about the meaning of these files](/home/user/Documents/projects/thoughts/topics/software/content/install-zettlr.md)