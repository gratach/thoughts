# What software can be used to monitor website setups

When I have a network of multiple websites that can span different domains. What software solutions are available that can check if everything is set up correctly?

I would like to have features like this:

- The software can be started with a list of domain names that should be checked
- It then opens the index.html websites of all these domains and collects a list of all files that are available under these domains by crawling through the content.
- It checks for broken links (also to external websites) and reports them
- It checks if all the certificates are set up correctly.
- It scans the Javascript code for Websocket connections and checks if it can make a connection
- It collects the hashes of all file and remembers them. If started a second time it lists all files that have changed since the last time. (As well as all new files and all files that have been deleted).
- It checks if all servers are available with ipv4 and ipv6

## Answers

For example [Linkinator](../../../topics/code/web-development/linkinator.md)

