# Rules for using dunin IDs

Here are the rules how to define and use addresses in the [dwll-url-node-identification-namespace](../../graph/organizing/dwll-url-node-identification-namespace.md):

Every domain owner can create [dunin nodes](../../graph/organizing/dunin-node.md) by assigning a data content (byte data + link list) to a [dunin ID](dunin-id.md) that belongs to the domain. The responsibility for the definition of the dunin nodes has a virtual entity that is called [dunin agent](../../code/architecture/dunin-agent.md). Each dunin agent is identified by a [dunin-agent-locator](dunin-agent-locator.md) and responsible for the definition of all dunin nodes that have a dunin ID that starts with this particular dunin agent locator.

A dunin node is officially defined in the moment when the dunin agent tells any third party what the data content (byte data + link list) is that belongs to a dunin ID. Once a dunin node is defined it **must never change its content**. It is the responsibility of the dunin agent to make sure that it never assigns the same dunin ID to multiple data contents.

A dunin agent has the possibility to [reserve dunin IDs](../../code/architecture/reserved-dunin-id.md). This means that it can already use the dunin ID (for example as a reference in the link list of other dunin nodes) without having the content of the dunin ID defined. 

Once a dunin node is defined it can be stored by any dunin agent. Not only the one that defined it.