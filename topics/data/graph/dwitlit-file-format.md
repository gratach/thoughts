# dwitlit file format

The dwitlit (data with two link types) file format can be used to store an interlinked network of data nodes.

## Properties of the network

Each data node consists of a dwitlit-id, a link list and a data content. These three properties are sufficient for identifying a unique data node.

- **dwitlit-id**
	A string of ASCII characters that must not contain any line breaks and space characters. The string must contain at least one character. It is possible that multiple data nodes use the same dwitlit-id. 
- **link list**
	A ordered list of links to other data nodes. Each link in the list has one of two types:
	- **general links**
		These links are only referring to a dwitlit-id but do not specify the content of the referred nodes. These links are pointing to all nodes that share the specified id. It is also possible that there are not (yet) any data nodes defined in the network that use the according dwitlit-id.
	- **specific links**
		These links are referring to a specific data node that can be identified by its three properties (dwitlit-id, link list and a data content). It must not be possible to reach the original data node by only following specific links. Any nodes that are introducing closed loops of specific links are invalid. The target of a specific link must always exist within the same network.
- **data content**
	A byte list of arbitrary length. An empty list is also allowed. There are no excluded byte characters.

## File format

The file consist of a sequence of **node entries** which contain the information that is necessary to construct a single data node. The node entries are separated by double new line characters `"\n\n"`.

An individual node entry is made of four parts in the following order: A node entry header, a link list, the length of the data content and the data content.
These four parts are separated by three character delimiters made of the a vertical bar enclosed by line breaks `"\n|\n"`.

- **node entry header**
	The header of any node entry consist of one to three parts in the following order: a manditorry dwitlit-id, an optional version tag and an optional confirmation tag. These parts are separated by space delimeters `" "`.
	- **dwilit-id**
		The dwillit-id of the respective node.
	- **version tag**
		The dwitlit-file format uses version tags to distinguish between different data nodes with the same dwitlit-id. These version tags are ASCII strings with at least one character that must not contain any line breaks, space characters and `"+"`characters. Version tags are not part of the represented data structures but are only used for the correct assignment of the specific links within the file. They can be therefore chosen arbitrarily. However every combination of dwitlit-id with respective version tag can only occur in one node entry header per file.
	- **confirmation flag**
		A confirmation flag is a single `"+"`character that gives the author of the dwitlit-file the possibility to confirm that the statement of the respective node is true. This information is not part of the node itself but reflects the knowledge that the author has about the respective node.
- **link list**
	A list of the nodes links that are separated by new line characters `"\n"`. The link format depends on the type of the link.
	- **general link**
		These links only consists of the dunin-id of the target nodes. It is not mandatory for any target nodes to be in the same file.
	- **specific links**
		These links consist of the dunin-id of the target node followed by a space delimiter `" "` and the version tag of the target node. The target node of an specific link has to be contained in the same dwitlit-file.
- **length of data content**
	The byte length of the data content is encoded as a decimal number.
- **data content**
	The byte content of the node.

## Example

This example shows four nodes (one with the id `space`, two with the id `star` and one with the id `earth`). They all have a little text as byte content except for the `space`node which has an empty byte content. The first two nodes have no links. The third node `star 1` has two general links to the ids `star`and `earth`. The last node `earth`has a three links. A general link to the id `planet` that has no respective nodes within the file, a specific link to `star 1`and a general link to `space`.

```
space
|
|
0
|


star 0
|
|
32
|
There are many stars in the sky.

star 1 +
|
star
earth
|
48
|
The sun is the closest {link 0} to our {link 1}.

earth +
|
planet
star 1
space
|
57
|
Our {link 0} circles around the {link 1} in the {link 2}.
```

## See also

This file format is an improved version of the [dwllver file format](data-with-linked-list-version-extension-row-file.md) and an improved and extended version of the [dwll file format](data-with-link-list-rows-file.md).