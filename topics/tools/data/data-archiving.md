
# Handling .zip files

Bundle the content of `mydirectory` into the zip file `myzipfile.zip` using

```bash
(cd mydirectory; zip -r ../myzipfile.zip * .*)
```

Extract the content of `myzipfile.zip` into `mydirectory`

```bash
unzip myzipfile.zip -d mydirectory
```

List all the files in the directory `mydirectory`

```bash
find mydirectory -type f
```
