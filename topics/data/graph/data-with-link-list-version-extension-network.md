# Data with link list version extension network

A dwllve network is a extended version of a [dwll network](data-with-link-list-network.md) that deals with the uncertainty of not knowing what the exact content of a node is and allows for multiple versions of such nodes.

It can be viewed as a semantic network of two types of nodes: [original dwllve nodes](original-dwllve-node.md) and [versioned-dwllve-nodes](versioned-dwllve-node.md). The original dwllve nodes resemble the dwll nodes as they are known from the dwll network with the difference that their content (byte data together with ordered link list) may or may not be defined. The versioned dwllve nodes are always assigned to an original dwllve node and resemble some version of this specific node. The content of a versioned dwllve node (byte data together with ordered link list) is always defined.

The ordered link list of both original and versioned dwllve nodes may contain links to both types of nodes. Depending on the type of the linked node the links are called original links and versioned links.

A dwllve network must not contain any circles of versioned links. This means that if you start at a versioned node of the network, follow one versioned link of this nodes link list which leads to an other versioned node and repeat this step you are not allowed to arrive at the node where you have startet.

A versioned dwllve node is always completely defined by its byte content, its link list and the original node it belongs to. Within a dwllve network there must not exist two distinct versioned nodes that have identical values for these three properties. The same thing is not true for original nodes. If the link list and byte content of two original nodes match they do not have to be the same node.

### File format

A file format to store dwllve network data is the [dwllver-file-format](data-with-linked-list-version-extension-row-file.md).
