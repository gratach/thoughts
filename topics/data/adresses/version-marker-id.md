# Version marker id

The version marker id is a string only containing a single asterix symbol `*`

It is used to mark [versioned-dwllve-nodes](../graph/versioned-dwllve-node.md) in the [dwllver file format](../graph/data-with-linked-list-version-extension-row-file.md). 

They are marked by using a link list like in the following example:

```
1: *
2: <node id of the respective original dwllve node>
3: <all the links>
4: <of the original dwllve nodes>
5: <as they are anticipated by this particular version>
...
```
The strings enclosed by pointy brackets should be replaced by the respective node ids