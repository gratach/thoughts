# Dunin agent

A dunin agent is the virtual entity that is responsible for the assignment of [dunin](../../graph/organizing/dwll-url-node-identification-namespace.md) addresses. It is identified by an dunin agent locator which is a url string that ends with a double slash.

Example of a dunin agent locator:
`http://my.domain.com/dunin/agent/locator//`

A dunin agent can be controlled via an [dunin-agent-control-interface](../interfaces/dunin-agent-control-interface.md).
Dunin agents handle [dunin IDs](../../data/adresses/dunin-id.md) according to the [[rules-for-using-dunin-ids]].
A possible realization of an dunin agent is the [[http-dunin-agent]].