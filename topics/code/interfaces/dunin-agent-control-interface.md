# Dunin agent control interface

This is a list of functions that should be implemented by an interface that can be used to control a [dunin-agent](../architecture/dunin-agent.md).

**createNewNode** (content, links) -> internalDuninID

Creates a new dunin node that is identified by a new internal and an external dunin id. Uses the given content and links to create the node. Returns the internal dunin ID.

**reserveNewNode** () -> externalDuninID

Reserves a new dunin ID that can later be used to create a dunin node at that place. Returns this dunin ID.

**setReservedNode** (externalDuninID, content, links) -> internalDuninID

Sets a dunin node at the place of an earlier reserved duninID. Uses the given content and links to create the node. Returns the internal dunin ID of the new created node.

**getNodeStatus** (duninID) -> string

Returns the [dunin node status code string](../architecture/dunin-node-status.md) of the duninID

**getNodeContent** (duninID) -> (content, links)

Returns a tuple of the content and the links of the dunin node with the given dunin ID. When the ID is external it returns the version that is officially accepted by the dunin agent. When it is internal it returns only the according version.

**getNodeByteContent** (duninID) -> content

Returns the byte content of the dunin node with the given internal dunin ID. (External/internal see getNode Content)

**getNodeLinks** (duninID) -> links

Returns the inks of the dunin node with the given internal dunin ID.  (External/internal see getNode Content)

**importNode** (externalDuninID, content, links) -> internalDuninID

Imports a foreign dunin node with a given dunin id, content and links. Creates a new internalDuninID for this node if necessary and returns it.

**getExternalID** (internalDuninID) -> duninID

Returns the dunin ID that belongs to an internal dunin ID

**getMainInternalID** (externalDuninID) -> internalDuninID

Returns the internal dunin ID that represents the version of the dunin node that is officially accepted by the dunin agent.

**setMainInternalID** (internalDuninID) -> _

Sets the version of the dunin Node that is officially accepted by the dunin agent. This only makes sense when there are multiple versions (each with its own internal dunin ID) of the same dunin node (which has an external dunin ID).

**getInternalIDs** (externalDuninID) -> internalDuninIDArray

Get a list of all the internal dunin IDs of a given external dunin ID. Each of them represents one version of the dunin node.

**isExternalID** (duninID) -> bool

Returns true if the duninID is external and false if it is internal

**getReferencingNodes** (duninID) -> internalDuninIDArray

Returns all saved nodes that are referencing the duninID in their link list. If the dunin ID is external it returns those nodes who reference the external ID or the officially accepted internal ID. If the ID is internal it returns nodes that reference either this particular internal or the according external ID.

**getInternallyReferencingNodes** (internalDuninID) -> internalDuninIDArray

Returns all saved nodes that are referencing the internal dunin ID.

**getExternallyReferencingNodes** (externalDuninID) -> internalDuninIDArray

Returns all saved nodes that are referencing the external dunin ID.

**deleteNode** (duninID) -> bool

Deletes the node with the given dunin ID from the memory of the dunin agent. If the dunin ID is external it deletes all versions of the node. If the ID is internal it deletes only this version of the node (and also the external dunin ID if it is the only version). The deletion process is abbordet with an error if the any other node references the internal dunin ID of the node that should be deleted.

**deleteNodeWithAllInternallyDependingNodes** (duninID) -> _

Deletes the node with the given dunin ID from the memory of the dunin agent. If the dunin ID is external it deletes all versions of the node. If the ID is internal it deletes only this version of the node (and also the external dunin ID if it is the only version). This deletion triggers a chain reaction and deletes all nodes that reference an internal dunin ID of any node that is deleted in this process.


This interface can be implemented as a [dunin-agent-control-protocol](../architecture/dunin-agent-control-protocol.md) that connects a client with a server.