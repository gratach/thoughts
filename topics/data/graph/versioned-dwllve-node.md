# Versioned dwllve node

A versioned dwllve node is one of the two node types of a [dwllve-network](data-with-link-list-version-extension-network.md). It represents a specific version of a [[original-dwllve-node]] (which is the other node type). The byte data and link list of the versioned dwllve node is always defined.

A versioned dwllve node is always completely defined by its byte content, its link list and the original node it belongs to. Within a dwllve network there must not exist two distinct versioned nodes that have identical values for these three properties.