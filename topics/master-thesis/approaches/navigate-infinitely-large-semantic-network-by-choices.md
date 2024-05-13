# Navigate a infinitely large semantic network by choices

A semantic network consisting of semantic triples that are made of a subject a predicate and an object can be navigated in multiple ways. One way would be to find specific nodes by searching for the content via a text search. In contrast to this a navigation mechanism can be also build in a way that it enables one to change position within the semantic network by making a finite number of decisions of choosing from a finite number of content related options.

This approach places high demands on the structure of the network of choices. Only if its quality is very high it becomes possible to efficiently find some specific knowledge within the network by using this method. This means also that the quality of the semantic network of choices can be measured by the ability of an llm agent to find a specific semantic triple.

### How could such semantic network of choices look like?

A semantic network can be navigated by jumping from one concept to the next by following the connections between the pairs of concepts that are linked by a predicate. The problem with infinitely large semantic networks is that there is potentially an infinitely large number of semantic triples to choose from. A navigation of finite choices could be achieved by organizing those semantic triples into a tree structure.