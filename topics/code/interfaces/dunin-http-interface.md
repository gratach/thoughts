# Dunin HTTP interface

The [dunin](../../graph/organizing/dwll-url-node-identification-namespace.md) HTTP interface is used to receive information about [dunin nodes](../../graph/organizing/dunin-node.md) from a [dunin-agent](../architecture/dunin-agent.md) with a URL [dunin-agent-locator](../../data/adresses/dunin-agent-locator.md).

The interface can be accessed by sending a http request to a url that contains information about the dunin agent, the dunin id and the format in which the information should be returned. The following lists different ways how such urls can be constructed. In all these cases the `http://` at the beginning of the url can also replaced by a `https://`.

A human readable html page that contains information about the dunin node and how to access its data gets returned when one of the following urls are called:

`<dunin ID>`
`<dunin agent locator>?id=<dunin ID>`

The first URL can only be used to receive data from the dunin IDs that belong to the dunin agent that is queried. A dunin agent can also store information about foreign dunin nodes with IDs that do not start with its dunin agent locator. To receive information about such foreign dunin nodes the second URL has to be used.

The following URLs specify a specific format string.

`<dunin ID>?format=<format string>`
`<dunin agent locator>?id=<dunin ID>&format=<format string>

Again the second URL has to be used for getting information about foreign dunin IDs from dunin agents.

The format string defines what type of data should be returned:

| format string | Content Type             | returned data                                                                                                                                                                                  |
| ------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data          | application/octet-stream | The byte data of the dunin node                                                                                                                                                                |
| links         | text/plain               | The newline separated link list of the dunin node                                                                                                                                              |
| dwll          | application/octet-stream | The data (byte data + link list) of the dunin node formatted in the [dwllr format](../../data/graph/data-with-link-list-rows-file.md) together with dunin source information of the dunin node |
| status        | text/plain               | One of the [dunin node status code](../../code/architecture/dunin-node-status.md) strings                                                                                                      |

