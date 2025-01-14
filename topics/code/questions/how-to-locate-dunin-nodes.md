# How to locate dunin nodes

An open question is how to efficiently locate [dunin nodes](../../graph/organizing/dunin-node.md) in a decentralized network of [dunin agents](../architecture/dunin-agent.md).

When some entity has a given [dunin-id](../../data/adresses/dunin-id.md) and wants to know what data content belongs to it it can request this information by calling the [dunin-http-interface](../interfaces/dunin-http-interface.md) of a dunin agent. However it first needs to know which dunin agent stores this information. It makes sense to first ask the dunin agent that was responsible for creating the dunin node. This dunin agent can easily be identified by extracting the [dunin-agent-locator](../../data/adresses/dunin-agent-locator.md) from the beginning of the dunin ID.

But it can not be taken for granted that this dunin agent still stores the dunin node. Each dunin agent has the right to forget the dunin nodes that it has created. The same problem occurs when the dunin agent who originally has created the node is no longer online. In both cases it is possible that some other dunin agent has copied the dunin node. But how can the entity with the dunin ID know the URL of the dunin agent who has copied the dunin node?

An idea each dunin agent can tell all parties which dunin nodes they store is by using some external distributed database that keeps track of the pairs of dunin IDs and the according dunin agent locators. A possible interface for such a distributed database is described [here](../interfaces/simple-community-database-interface.md).