# Linux disk space commands

### Get the used and available disk space for different devices

As plain number:
```
df
```
In human readable format:
```
df -h
```

### List all directories in the current file ordered by size

As plain number:
```
ls -A | xargs -I {} du -s {} | sort -rn

```
Human readable:
```
ls -A | xargs -I {} du -sh {} | sort -rh
```
This command is available under the shortcut `ls-s`if the pc is configured like described in [debian-i3-pc-setup](debian-i3-pc-setup.md)
See also:
[How to sort by size](https://unix.stackexchange.com/questions/106330/sort-all-directories-based-on-their-size)
[How to include hidden and special files and directories](https://superuser.com/questions/342448/du-command-does-not-parse-hidden-directories)

### Find duplicate files

Install fdupes
```
apt install fdupes
```
Search file duplicates in chosen directory
```
fdupes -r /my/chosen/directory
```