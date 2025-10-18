# What functionalities should the decentralized network fulfill

## Question

What functionalities would be useful for a [decentralized-consistent-data-network](../../../topics/data/graph/decentralized-consistent-data-network.md)? What properties would I like such a network to have? What properties are mandatory? What properties are optional?

## Brainstorming

 
* The network should be able to store data nodes that contain arbitrary data and links to other data nodes
* The content of a data node that is linked by an other data node should not change over time to make sure that the other data node is always pointing to the content that was originally intended by its author
* The network should be decentralized
* Every member of the network should be able to create new data nodes
* Every member of the network should be able to decide what data nodes he wants to store
* When all members of the network decide that they do not want to store a specific data node, all links to this data node should point to an "empty space" which represents an unknown content. This empty space should not be filled with a new node because this might have a different content than the original one which might not reflect the intended target content of the links.
* Every data node is identified by an unique address
* There should be an efficient address resolution algorithm that finds the location on the servers where the data that belongs to an address is stored
* It should be documented where the data comes from and which network members where involved in distributing it: If network member A created a node X and member B copied it to its server and member C copies it from member B then member C should store the whole chain of distributers A->B->C. If it later turns out that the data content that C possesses is wrong it can be traced that B might be responsible for altering the content.
* It should be possible to store multiple versions of data nodes for the same address where only one of them can be the correct one. If network member C receives a version of the node X with the [distribution-chain](../../../topics/data/distribution/distribution-chain.md) A->B->C and an other version of the node X with the distribution chain A->D->C which differs from the first version it should be able to store both versions with their distribution chains. In this case one or more of this three cases have to be true:
	1) B is malicious or dysfunktional and changed the content of X
	2) D is malicious or dysfunctional and changed the content of X
	3) A is malicious or dysfunctional and gave different versions of X to B and D
* The network members should keep track of which other network members they trust to be sincere and follow the rules. If they have multiple versions of a node they can decide which they believe to be the correct version based on how they trust the members which where involved in the different distribution chains
## Related Topics
[plan-dunin-network](../../../tasks/planning/data/plan-dunin-network.md)



