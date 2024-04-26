# Byte tree address

A byte tree address is a reference to a node in the [byte tree graph](byte-tree-graph.md). It describes the location of the node by describing the path to it starting from a [byte tree cone](byte-tree-cone.md). It therefore contains one bit of information that tells if the referenced node is in the direction of the byte tree cone. Additionally it contains a sequence of numbers (from 0 to 254) that define the the way that should be taken for each junction.

If the byte tree cone that is the starting point for the byte tree address is the root byte tree cone the byte tree address is an absolute address. Otherwise it is a relative address.