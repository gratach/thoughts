# Referenced Abstraction

A referenced abstraction is an [abstract-concept](abstract-concept.md), that is defined by a unique reference pointing to it. The unique reference can be realized by an [unique-shared-memory-address](../../data/adresses/unique-shared-memory-address.md) (USMA) that is used to identify a concept across different namespaces.

A referenced abstraction "```myReferencedAbstraction```" can be defined by using a [constructed-abstraction](constructed-abstraction.md) in the following way:

```
hasReference = constructedAbstraction(
	(None, None, hasReferenceUSMA)
)
myReferencedAbstraction = constructedAbstraction(
	(None, hasReference, myUSMA)
)
```
Where ```myUSMA``` is the USMA of ```myReferencedAbstraction``` and ```hasReferenceUSMA``` is the USMA that is used for identifying the ```hasReference``` concept.

When used in that way. Referenced Abstractions are a subset of constructed abstractions.