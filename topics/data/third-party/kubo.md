# Kubo

A application to run an [interplanetary-file-system](interplanetary-file-system.md) node.

[Installation](https://docs.ipfs.tech/install/command-line/#install-official-binary-distributions):
```
wget https://dist.ipfs.tech/kubo/v0.30.0/kubo_v0.30.0_linux-amd64.tar.gz
tar -xvzf kubo_v0.30.0_linux-amd64.tar.gz
cd kubo
sudo bash install.sh
ipfs --version
```

Run the daemon:
```
ipfs daemon
```
Add the file
```
ipfs add <name of the file>
```
This returns the CID of the added file
Pin the file
```
ipfs pin add <CID of the file>
```
The uploaded files can now be accessed publicly via the CID (e.g. under the URL ```https://ipfs.io/ipfs/<CID of the file>```) but [with very long latency](https://www.reddit.com/r/ipfs/comments/t2bjbw/long_delay_between_host_upload_public_link_working/).