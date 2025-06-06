# Data with linked list version extension row file

The `.dwllver`file format is an extended version of the [dwllr file format](data-with-link-list-rows-file.md) that allows to store [dwllve network data](data-with-link-list-version-extension-network.md).

The basic structure of the dwllver file format is the same as the structure of the dwllr file format. It consists of a number of node entries that are separated by triple newline characters which in turn consist of the node id, the link list, the number of byte content bytes and the byte content each separated by double newlines.

The node ids of a `.dwllver` file have to fulfill some additional requirements compared to the node ids of a `.dwllr`file: They must not contain any `?`and `=`characters and they have to respect the special meaning of the [version-marker-id](../adresses/version-marker-id.md) which is a string consisting only of the asterix symbol `*`.

Whenever the version marker id occurs in the first index of the link list of a node entry this means that the respective node is a [versioned-dwllve-node](versioned-dwllve-node.md). In this case the second entry of the link list is the node id of the [original-dwllve-node](original-dwllve-node.md) that this versioned dwllve node belongs to. The remaining links in the nodes link list are then the links of the original dwllve node as they are anticipated by the particular version of the versioned dwllve node. In this case the byte data content of the node represents the byte data content of the respective original dwllve node as anticipated by this particular version.

When the id at the first index of the node entries link list is not the version marker id the respective node is a original dwllve node and the byte data content and the link list are defined as described in the original [dwllr file format](data-with-link-list-rows-file.md).

The node entry link lists of both versioned dwllve nodes and original dwllve nodes allow for two types of links: original links and versioned links. The original links consist of the node id  of the nodes without further modifications. The versioned links consist of three parts that are concatenated together into a single string: 
1) The node id of the versioned node
2) The middlepart that consists of four chars: `?vo=` where `vo` stands for version of
3) The node id of the original node that the versioned node belongs to

When an original dwllve node has an unknown contend as it is allowed within a dwllve network this means that this node has no node entry. However it can be referenced as a link by other nodes.



## Example

```
mynodeid1/statement1/version1

*
mynodeid2/statement1
mynodeid3/inserttexttype
mynodeid4/word/tree
mynodeid5/word/hill

21

The {1} is on the {2}



mynodeid6/statement1/version2

*
nodeid2/statement1
nodeid3/inserttexttype
nodeid5/word/hill
nodeid4/word/tree

25

The {1} is behind the {2}



nodeid7/versioncomment1

nodeid8/versioncommenttype
nodeid1/statement/version1?vo=nodeid2/statement1

34

In this version the tree is higher



nodeid9/versioncomment2

nodeid8/versioncommenttype
nodeid6/statement/version2?vo=nodeid2statement1

33

In this version the tree is lower




```

This example consists of four node entries with two of them describing original dwllve nodes with the node ids `nodeid7/versioncomment1`and `nodeid9/versioncomment2` and two of them describing versioned dwllve nodes with the node ids `mynodeid1/statement1/version1`and `mynodeid6/statement1/version2`. The two versioned dwllve nodes are versions of the original dwllve node with the id `nodeid2/statement1` which has an unknown content because it has no node entry.

At the first index of the link list of the first two node entries is the version marker id which indicates that the nodes are versioned dwllve nodes. At the second index of their link list is the id of the original dwllve node that the versions  belong to. In this case this is the id `nodeid2/statement1`. The last three entries of the link list are actual content of the versioned dwllve nodes link list. The first of these three links shows that the versioned dwllve nodes have a type with the id `nodeid3/inserttexttype`. How to interpret the remaining two links is not defined by the dwllver file format. In this case they are the ordered insertions that belong into the `{1}` and `{2}`placeholders of the versioned dwllve nodes byte content.

The last two node entries of this example have a link list that does not start with the version marker id which means that they define original dwllve nodes that adopt their link list without changes. The first entry of the link list specifies the type of the original dwllve nodes which has the id `nodeid8/versioncommenttype`.  The second entry of the 