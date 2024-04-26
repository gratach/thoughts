# Base Connections

A base connections object is used to define [constructed concepts](constructed-concept.md) of a [conceptlogic](conceptlogic.md). It consists of an set of base connection objects which are triples consisting of a subject predicate and object. Each of the three values is thereby ether ```None``` or a concepts of the conceptlogic. At least one of the three entries of the triple has to have the value ```None```.  The ```None``` value indicates, that at this place the new defined concept could be substituted.

## Example:

```
{
	(None, isInstanceOf, listConcept),
	(None, hasListEntryOne, someValue),
	(None, hasListEntryTwo, someOtherValue),
	(None, hasListLength, two)
}
```

In this example a base connections object is used to define a list concept containing the two entries ```someValue``` and ```someOtherValue```.