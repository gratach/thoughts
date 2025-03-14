# Internal dunin ID

A internal dunin ID is a modified version of a [dunin-id](dunin-id.md) that is used to internally reference the data content of a dunin ID within a [dunin-agent](../../code/architecture/dunin-agent.md).

It is constructed by appending `?v=`and some alphanumeric version code to a dunin ID.

Example:

(External) dunin ID:
`http://my.domain.com/dunin/agent/locator///data/resource/locator`

Internal dunin ID:
`http://my.domain.com/dunin/agent/locator///data/resource/locator?v=1`

This internal dunin ID plays a key role when [handling altered versions of dunin nodes](how-to-handle-altered-versions-of-dunin-nodes.md): When the dunin agent has contradictory information about the content of a [dunin node](../../graph/organizing/dunin-node.md) from different sources internal dunin IDs make it possible that any of those versions of the same node can be referenced separately. 

Because a internal dunin ID is only used for data stored within a single dunin agent it can not be used to globally reference data across multiple dunin agents. In fact the same internal dunin ID string could reference different versions of a dunin node for different dunin agents. 