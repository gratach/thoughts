# Contribute to Debian

Contribute to [Debian](debian.md):

Packaging:
	[Maintainer guide](https://www.debian.org/doc/manuals/maint-guide/index.en.html)
Bug report:
	[Bugreport manual](https://www.debian.org/Bugs/Reporting)
Package informations
	[tracker](https://tracker.debian.org/)

## Wnpp

An overview over all packages that are orphaned, intended to package or intended to adopt can be found [here](https://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=wnpp;dist=unstable) on wnpp some introduction and the explanation of the abbreviations can be found [here](https://www.debian.org/devel/wnpp/):

- **O** Orphaned package
- **RFA** Request for adoption
- **RFH** Request for help
- **ITP** Intend to package
- **RFP** Request for package
- **ITA** Intend to adapt an orpaned package



## Packaging 
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

## Visualize package dependencies

[source](https://wiki.julian-lemmerich.de/doku.php?id=knowledge_base:linux:debtree)

```
apt install debtree graphviz
debtree <name-of-package> | dot -Tpng > <name-of-output-file>.png
```