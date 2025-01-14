# Dunin ID

A [dunin](../../graph/organizing/dwll-url-node-identification-namespace.md) ID is an string that references a [dunin-node](../../graph/organizing/dunin-node.md).

There are two types of dunin IDs:
* URL dunin IDs
* Cryptographic dunin IDs

A dunin ID contains of two parts:
* A [dunin-agent-locator](dunin-agent-locator.md)
* A data resource locator

As a whole a dunin ID is a uri that has a triple slash in the path section and must not contain any "?", "=", "&" or "\#" characters. Except for the double slash after the [uri scheme](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) (`http` or `crypt`) and the triple slash `///` all other slashes that occur in the dunin ID are single ones

Example for a URL dunin ID:

`http://my.domain.com/dunin/agent/locator///data/resource/locator`

The first part of the dunin ID up to the first two slashes of the triple slash is the [dunin-agent-locator](dunin-agent-locator.md)

`http://my.domain.com/dunin/agent/locator//`

The second path of the url starting with the last slash of the triple slash is the data resource locator

`/data/resource/locator`


A dunin ID is also sometimes called an external dunin ID in contrast to the [internal-dunin-id](internal-dunin-id.md).

A dunin ID does not always have to be assigned to a dunin node right away. It is also possible to [reserve dunin IDs](../../code/architecture/reserved-dunin-id.md).

The data that is assigned to a dunin ID can be accessed via the [dunin-http-interface](../../code/interfaces/dunin-http-interface.md). A question that still remains is [how to efficiently locate the content of dunin IDs](../../code/questions/how-to-locate-dunin-nodes.md).