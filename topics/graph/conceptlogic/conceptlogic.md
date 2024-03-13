# Definition:

We want to establish a simple model in which logical concepts can be defined as mathematical objects. 
In this model, a logical concept should also be able to represent a type of relationship that can exist between two other concepts.

A set of concepts should have the following properties:

When elements from the set of concepts are substituted for variables A, B, and C, a unique truth value should be assigned to this triplet. 
This value indicates whether concept A is in a relationship with concept C as described by concept B.

Next, a mechanism should be described that allows the definition of new concepts based on a set of existing concepts. 
The definition of a new concept should be done by specifying, for a subset of all possible triplets that can be formed from the existing concepts and the new concept, whether they are in the corresponding relationship or not.

For each attempt to define a new concept in this way, the mechanism should provide one of the following four results:

1. The definition is contradictory and cannot be used.
2. The definition is not contradictory, but the new concept is not well-defined.
3. The definition is not contradictory, the new concept is well-defined, but it is identical to one of the existing concepts. 
    In this case, the mechanism must specify which existing concept it is and ensure that the truth values of the triplets containing the existing concept do not contradict the definition of the new concept.
4. The definition is not contradictory, the new concept is well-defined, and it is not identical to any of the existing concepts. 
    In this case, the mechanism must specify, for all remaining triplets that can be formed from the new concept and the existing concepts, whether they are in the corresponding relationship or not.

In this way, the mechanism should be used to add new elements to the set of known concepts starting from a set of basic concepts over several iterations.

Additionally, the mechanism must satisfy the following criteria:

1. The order in which the new concepts are defined should not affect the result. 
    So, if concepts A and B can each be defined based on a set M of known concepts, then the truth values of all triplets in which both A and B appear must be the same regardless of whether A or B is defined first.
2. If a concept can be uniquely defined by describing its connections to other concepts, then it should be excluded that a second concept can be created that is not identical to the first but also exhibits the described connections.

A mechanism that satisfies these criteria, along with a set of basic concepts on which the mechanism is defined, shall be referred to as 'Concept Logic'.

# Further definitions:

A concept logic whose concepts can be defined by listing only triplets with positive truth values shall be referred to as 'positively defined'.

A concept logic shall be referred to as "concept logic with separate vertices and edges" if it
1. divides all its concepts into one of the two categories 'vertices' and 'edges'
2. assigns the truth value 'false' to all triplets that do not contain an edge as the middle concept and vertices as the remaining concepts.

A concept logic shall be referred to as "concept logic with fixed edges" if it
1. is a concept logic with separate vertices and edges
2. does not contain any concepts that are edges and do not belong to the basic concepts


# Example of a positively defined concept logic with fixed edges:

From the four basic concepts (1), (first argument of the sum of), (second argument of the sum of) and (results in), all natural numbers and all sums of two natural numbers can be defined as concepts by an appropriate concept logic so that the following applies:
1. The triplet X (first argument of the sum of) Y is true if and only if X is a natural number, Y is a sum of two natural numbers, and X is the first argument of this sum.
2. The triplet X (second argument of the sum of) Y is true if and only if X is a natural number, Y is a sum of two natural numbers, and X is the second argument of this sum.
3. The triplet X (results in) Y is true if and only if X is a sum of two natural numbers and Y is the sum of these two numbers.
4. All other triplets are false.

In this way, the concept (1 + 0) could be defined from the basic concepts by defining the following triplets as true:
1. (1) (first argument of the sum of) (1 + 0)
2. (1 + 0) (results in) (1)

In the next step, the concept (0) could be defined by defining the following triplet as true:
1. (0) (second argument of the sum of) (1 + 0)


# Questions:

What criteria must the definition of a concept logic satisfy in order to be fully defined and not contradictory?
What could be a general procedure for defining a concept logic?
Is it possible to define a concept logic with a finite number of basic concepts that can represent all possible concept logics with a finite number of basic concepts by concepts?