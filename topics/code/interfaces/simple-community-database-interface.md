# Simple community database interface

Interface for a database that is implemented by a decentralized network of clients. Each client can store arbitrary data under arbitrary byte string addresses. The network keeps track which client provides data for which byte string address.

Each **SimpleCommunityDatabaseClient** class implements the following functions:

* **activate():** Let the client join the network
* **deactivate():** Let the client disconnect from the network
* **findData(address):** Returns a **DataEnumerator** object that enumerates all data that the clients of the network store under the given address
* **provideData(data, address):** Stores data under a given address and makes it available for other clients
* **removeData(address):** Undoes the process of providing data to the network

The **DataEnumerator** object provides the following function:

* **getNextData():** Returns ether the data of the next client of the network that provides it for the given address or none if there are no more clients which store data under the given address


One possible application of this database is the task of [locating dunin nodes](../questions/how-to-locate-dunin-nodes.md).