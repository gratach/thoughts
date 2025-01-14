# HTTP dunin agent

This is a project with the goal to build a [dunin-agent](../architecture/dunin-agent.md) that serves its content over http.

The following features should be implemented:

* A private client api that makes it possible to define nodes
* An authentication mechanism to recognize that the client is authorized
* A possibility to copy nodes from one dunin agent to an other agent
* A [postresql](../../data/database-software/postresql.md) database to store the data
* A mechanism to keep track of the source evidence

