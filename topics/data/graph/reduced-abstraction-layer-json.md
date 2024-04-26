# Reduced Abstraction Layer JSON (RALJ)

RALJ is a format to store semantic network data of the [reduced-abstraction-layer-framework](reduced-abstraction-layer-framework.md). It is saved in a json scheme like the following example:

```
[
	# Constructed abstraction block
	{
		1 : [
			[0, 3, 4],
			[0, 5, 6]
			...
		],
		2 : [
			[0, 0, 1],
			...
		]
		...
	},
	# Direct data abstraction block
	{
		"dataformat 1" : {
			3 : "data content 1.1",
			4 : "data content 1.2",
			5 : "data content 1.3",
			...
		},
		"dataformat 2" : {
			6 : "data content 2.1",
			7 : "data content 2.2",
			...
		}
		...
	},
	# Direct abstraction block
	{
		8 : 1,
		9 : 6,
		...
	},
	# Inverse direct abstraction block
	{
		10 : 2,
		...
	}
]
```

The file format uses the numbers ```1, 2, 3, ...``` as references for the abstract concepts. The number ```0``` is reserved for self references in the definition of constructed abstractions and can not be used to define new concept references.

The file contains an json list that can have up to four entries. Those entries are the following data blocks in order:
- Constructed abstraction block
- Direct data abstraction block
- Direct abstraction block
- Inverse direct abstraction block
Each of that data blocks is a json dictionaries. If the list is shorter than four, the remaining data blocks are left to be empty dictionaries.

A loader and saver for ralj files that uses the neo4j database can be found [here](https://github.com/gratach/consemnet-navigator/blob/8f725cac458cafe70a5ebe72989bb041af89e1dd/consemnet_navigator/ralj_loader.py)