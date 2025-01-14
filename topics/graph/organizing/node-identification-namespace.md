# Node identification namespace

A node identification namespace is a system that assigns byte addresses to the nodes of a semantic network. For a given semantic network multiple node identification namespaces can exist. A node identification namespace can serve the following purposes:

* It can make it possible to save semantic networks or parts of them in a file by allowing for the use of byte references to other nodes in the network.
* It should make sure that each node in the network has exactly one byte address representing it.
* It can come with some mechanism to find the nodes data resource of a given byte address.
## dwll

A node identification namespace is needed when storing [dwll](../../data/graph/data-with-link-list-network.md) data (for example in the [dwllr file format](../../data/graph/data-with-link-list-rows-file.md)). A node identification namespace for dwll data is the [dudin](dwll-url-node-identification-namespace.md).