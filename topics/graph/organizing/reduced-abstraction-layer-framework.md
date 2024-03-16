# Reduced Abstraction Layer Framework

The reduced abstraction layer framework is using only a small subset of the [abstract concepts](abstract-concept.md) of a conceptlogic: It only contains the following two types of concepts:
1) [direct abstractions](direct-abstraction.md) of [data concepts](../../data/graph/data-concept.md)
2) [constructed abstractions](constructed-abstraction.md)
The reduction to these two types of concepts brings the advantage that the implementation of a program that loads and saves data that is part of the reduced abstraction layer framework is not dependent on the data itself.