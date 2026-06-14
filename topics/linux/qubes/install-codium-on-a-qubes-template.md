# Install codium on a Qubes template

The following commands can install [Codium](../../tools/editor/codium.md) on a [Qubes OS](qubes-os.md) template:
```
sudo apt install extrepo
sudo extrepo enable vscodium
sudo apt install codium
```
There are problems creating the sha256 checksum `880957c1310498fcf1f91025fbcdf5dfb5b41832919e1f0646bcbafdb7101bd7`  from the public key of the repo.