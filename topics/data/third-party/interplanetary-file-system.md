# Interplanetary file system

The [Interplanetary file system](https://docs.ipfs.tech/) (IPFS) is a protocol for a distributed data storage that addresses each file with a Contend identifier (CID). The network consists of [IPFS nodes](https://docs.ipfs.tech/concepts/nodes/#types) which are individual programs that can [pinn](https://docs.ipfs.tech/concepts/lifecycle/#_2-pinning) data files and make them public within the network. The network can find the data assigned to a specific CID by querying a [distributed hash table](https://docs.ipfs.tech/concepts/dht/#distributed-hash-tables-dhts) which IPFS node has the content of the wanted CID. The most common application to run an IPFS node is [Kubo](kubo.md).

The CID is [not only dependent on the content and the filename](https://discuss.ipfs.tech/t/how-to-calculate-file-directory-hash/777/3) of the data but also on other parameters like the used hash algorithm.

Resources on the IPFS can be accessed via a 