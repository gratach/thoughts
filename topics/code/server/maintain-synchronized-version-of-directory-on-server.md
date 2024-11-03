# Maintain synchronized version of directory on server

### Using scp

Files can be copied recursive from client to server via

`scp -r <source directory> <server>:<destination directory>`

This does not work if the destination directory already exists

### Using rsync

With rsync an directory on the server can be synchronized to the current version of a local directory

Therefore rsync has to be installed on server and client (`apt install rsync` on debian)

The following command can be used for the synchronization:

```
rsync -a --delete <source directory>/ <server>:<destination directory>
```

Use with care. The old content of the destination directory is deleted.

Note the `/` symbol after the `<source directory>`. It is important to replace the destination directory with the source directory. If missing the source directory will be placed in the destination directory