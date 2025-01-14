# Internal dunin ID

A internal dunin ID is a modified version of a [dunin-id](dunin-id.md) that is used to internally reference the data content of a dunin ID within a [dunin-agent](../../code/architecture/dunin-agent.md).

It is constructed by appending `?v=`and some alphanumeric version code to a dunin ID.

Example:

Dunin ID:
`http://my.domain.com/dunin/agent/locator///data/resource/locator`

Internal dunin ID:
`http://my.domain.com/dunin/agent/locator///data/resource/locator?v=1`

