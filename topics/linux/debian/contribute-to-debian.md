# Contribute to debian

Contribute to [Debian](debian.md):

Packaging:
	[Maintainer guide](https://www.debian.org/doc/manuals/maint-guide/index.en.html)
Bug report:
	[Bugreport manual](https://www.debian.org/Bugs/Reporting)
Package informations
	[tracker](https://tracker.debian.org/)


Packaging 
```
apt install sbuild devscripts piuparts lintian git-buildpackage quilt
apt get source hello
cd hello-2.10/
dpkg-buildpackage -uc -us
```

```
wget https://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz
tar -xf hello-2.10.tar.gz 
cd hello-2.10/
git init
gbp import-orig ../hello-2.10.tar.gz --debian-branch=debian/latest --upstream-branch=upstream/latest --pristine-tar

```

