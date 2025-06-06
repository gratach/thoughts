# Data with link list network

The **dwll** (data with link list) network is a type of a semantic network in which each node has a block of byte data assigned to it and also a ordered list of directed edges pointing from the node to other nodes. The directed edges in the list that link two nodes do not have to be symmetric. For example it is possible that node A contains a link to node B at the first index of its list but node B does not contain any links to node A in its list.

Some of the nodes represent data formats. The first directed edge in the edges list of each node points always to the target node that represents the data format of the original node. 

In order to interpret the meaning of the byte data and the ordered edges list of each node one has to know how the data formats of the nodes representing data formats are defined. This is not defined by the **dwll** format itself.

### Benefits

The benefits of data formatted as a dwll network is that it is possible to store data records of arbitrary user defined formats but still having the links between different data records in a uniform format. This allows one to handle and store the interconnected data without knowing how to interpret it. It is also easier to transfer the data between different [node identification namespaces](../../graph/organizing/dwll-url-node-identification-namespace.md)
### File format

The [dwllr file format](data-with-link-list-rows-file.md) can be used to store dwll data. To identify nodes in this format the [dwll-url-node-identification-namespace](../../graph/organizing/dwll-url-node-identification-namespace.md) can be used.

### Node identification namespace

When a dwll network is implemented it is necessary to identify the nodes by some ID.

### Example of a dwll network

Node 1:
	Byte content: b"String"
	Edges list:
		1) Node 1

Node 2:
	Byte content: b"Int"
	Edges list:
		1) Node 1

Node 3:
	Byte content b"Sentence"
	Edges list:
		1) Node 1

Node 4:
	Byte content: b"Here"
		1) Node 1

Node 5:
	Byte content: b"are"
	Edges list:
		1) Node 1

Node 6:
	Byte content b"4"
	Edges list:
		1) Node 2

Node 7:
	Byte content: b"words"
	Edges list:
		1) Node 1

Node 8:
	Byte content: b"Language: English"
	Edges list:
		1) Node 3
		2) Node 4
		3) Node 5
		4) Node 6
		5) Node 7

This example has the following properties:
* The nodes 1,2 and 3 represent the string, the int and the sentence format. 
* The nodes 1,2,3,4,5 and 7 contain data of the string format because their first and only edge in the list points to node 1
* The node 6 contains data in the int format because its first and only edge in the list points to node 2
* The node 8 contains data in the sentence format because its first edge in the list points to node 3
* The other edges in the list of node 8 point to the different components of the sentences. Together they can be read as "Here are 4 words"

### Extension

A extended version of this network in which multiple versions of nodes with the same ID can exist is the [data-with-link-list-version-extension-network](data-with-link-list-version-extension-network.md)



