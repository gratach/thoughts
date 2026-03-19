# Search for files

## By name 

```
find . -type f -name "filename.txt"
```

## By partial name

```
find . -type f -name "*partial*"
```

## Search by content

```
grep -rnw '/the/path/where/to/search/' -e 'pattern'
```
[source](https://stackoverflow.com/questions/16956810/find-all-files-containing-a-specific-text-string-on-linux)