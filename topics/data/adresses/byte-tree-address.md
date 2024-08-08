# Byte tree address

A byte tree address is a reference to a node in the [byte tree graph](byte-tree-graph.md). It describes the location of the node by describing the path to it starting from a [byte tree cone](byte-tree-cone.md). It therefore contains one bit of information that tells if the referenced node is in the direction of the byte tree cone. Additionally it contains a sequence of numbers (from 0 to 254) that define the the way that should be taken for each junction.

The standard notation to write an byte tree address is `[<direction>, <path>]`where 
* `<direction>`is
	* `"+"`if the first bit is set to indicate that the address is in the direction of the byte tree cone
	* `"-"`if the first bit is not set to indicate that the address is in the opposite direction of the byte tree cone
* `<path>`is 
	* An array that writes all numbers coma separated and enclosed by square brackets
Example:
`["+", [42, 254, 0]]`

If the byte tree cone that is the starting point for the byte tree address is the [[usma-root-byte-tree-cone]] the byte tree address is an absolute address. Otherwise it is a relative address.