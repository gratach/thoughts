# Constructed Abstraction

A constructed abstraction is an [abstract-concept](abstract-concept.md) that stores the information in which way the concept that it represents is connected to other concepts. It therefore contains a [semantic-connections-object](../conceptlogic/semantic-connections-object.md) that links the constructed concept to other abstract concepts.

A definition of an constructed abstraction could look like this:

```
constructedAbstraction({
	(None, someAbstractConcept1, someAbstractConcept2),
	(None, someAbstractConcept3, someAbstractConcept4),
	(someAbstractConcept5, None, someAbstractConcept6),
	(None, someAbstractConcept7, None),
	...
})
```

When ever the concept ```someAbstractConcept``` in this definition is not an abstract concept but an normal concept the corresponding [direct-abstraction](direct-abstraction.md) would be substituted. This is just an abbreviation that makes it possible to write
```
constructedAbstraction({
	(None, myLink, myConcept)
})
```
instead of
```
constructedAbstraction({
	(None, directAbstraction(myLink), directAbstraction(myConcept))
})
```

## Example

if ```"hallo"``` and ```1``` are both concepts and ```directAbstraction("hallo")```
and ```directAbstraction(1)``` are both direct abstractions of ```"hallo"``` and ```1``` then the concept ```{"hallo"}``` which is a set containing only ```"hallo"``` would be a [constructed-concept](../conceptlogic/constructed-concept.md) build from this semantic connections object:
```
{
	(None, hasSetEntry, "hallo"),
	(None, hasSetLength, 1)
}
```
One now could create a constructed abstraction:
```
constructedAbstraction({
	(None, directAbstraction(hasSetEntry), directAbstraction("hallo")),
	(None, directAbstraction(hasSetLength), directAbstraction(1))
})
```
The resulting constructed abstraction would have an equivalent expressiveness as ```directAbstraction({"hallo"})```. They would both represent nothing but the concept ```{"hallo"}```.

But one could also create a constructed abstraction using the following definition:

```
constructedAbstraction({
	(None, directAbstraction(hasSetLength), directAbstraction(1))
})
```
This would then be an ambiguous constructed abstraction which could represent any set concept that has just one entry.