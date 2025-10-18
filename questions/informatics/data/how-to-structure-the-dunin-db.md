# How to structure the dunin db

How to structure the [dunin database](../../../topics/data/database-software/dunin-db.md) that stores the [dunin nodes](../../../topics/graph/organizing/dunin-node.md)?

## Brainstorming

**Nodes Table**

| Local ID | Dunin ID                  | Version ID     | Active | Link Count | Link IDs | Byte Content                                         |
| -------- | ------------------------- | -------------- | ------ | ---------- | -------- | ---------------------------------------------------- |
| 0        | debablo.de/_sun           | myserver.com/_ | False  | 3          | 0,1,2    | `Sun shines at [day](0) and is hidden at [night](1)` |
| 1        | myserver.com/_sunRecieved | Null           | True   | 2          | 3,4      | Some Content                                         |

**Links Table**

| Link ID | Local Node ID | Link Index | Destination           | Local Destination ID |
| ------- | ------------- | ---------- | --------------------- | -------------------- |
| 0       | 0             | 0          | debablo.de/_/wiki     | None                 |
| 1       | 0             | 1          | debablo.de/_/day      | None                 |
| 2       | 0             | 2          | debablo.de/_/night    | None                 |
| 3       | 1             | 0          | debablo.de/_/recieved | None                 |
| 4       | 1             | 1          | debablo.de/_sun       | 0                    |


