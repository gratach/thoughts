# Reduced Abstraction Layer JSON (RALJ)

RALJ is a format to store semantic network data of the [reduced-abstraction-layer-framework](../../graph/organizing/reduced-abstraction-layer-framework.md). It is saved in a json scheme like the following example:

```
[
	# Data concept block
	{
		"dataformat 1" : {
			1 : "data content 1.1",
			2 : "data content 1.2",
			3 : "data content 1.3",
			...
		},
		"dataformat 2" : {
			4 : "data content 2.1",
			5 : "data content 2.2",
			...
		}
		...
	},
	# Constructed concept block
	{
		6 : [
			[0, 1, 2],
			[0, 1, 3]
			...
		],
		7 : [
			[0, 0, 4],
			...
		]
		...
	}
]
```

The file is separated  into two blocks, that are stored in a json array
- the data concept block
- the constructed concept block
#### Data Concept Block
The data concept block containes