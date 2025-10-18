# Having a decentralized method to create a network of linked data

This goal is to make a technology available to the public where individuals can collectively create an maintain a decentralized network consisting of data nodes that can contain links to other data nodes. Thereby it should be ensured that the data within this network stays consistent. When a data node contains a link to an other data node within the network it should be ensured that the data content that the link points to never gets changed even if there are a few malicious or dysfunctional members in the decentralized network. Each member of the network should be able to decide itself what data nodes it wants to store locally. The same data node should be able to be stored in multiple locations within the decentralized network. When a data node A gets created and an other node B contains a link to it this link should never point to something else then the content of node A. When all members of the decentralized network decide that they do not want to store A this would lead to the network forgetting the content of A. In this case it should be ensured that the link in B that originally pointed to A always points to the empty place of the missing data node and never gets assigned to a new data node.

## Overriding Goals
[having-an-open-platform-for-collective-thinking](../thinking/having-an-open-platform-for-collective-thinking.md)

## Goal-Oriented Tasks
[[plan-dunin-network]]