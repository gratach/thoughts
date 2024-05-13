# Prompts for tree sorted semantic network

Here are some queries with the appropriate answers to test possibilities of building a tree sorted semantic network as discussed in [navigate-infinitely-large-semantic-network-by-choices](navigate-infinitely-large-semantic-network-by-choices.md)

### General creation of semantic triples
```
USER: Semantic triples such as ["Star", "emits", "Light"] and ["Rocket", "can bring cargo to", "Space"] consists of a subject, a predicate, and an object. Give me five examples of semantic triples that contain "Electron" as subject and return them in an array formatted like [["sub1", "pred1", "obj1"], ["sub2", "pred2", "obj2"], ...]. Return nothing but the array without explanation.

SYSTEM: [\n    ["Electron", "is", "a subatomic particle"],\n    ["Electron", "has", "a negative charge"],\n    ["Electron", "revolves around", "the nucleus of an atom"],\n    ["Electron", "is involved in", "chemical bonding"],\n    ["Electron", "can flow in", "an electric current"]\n]
```
### Creation of semantic triples with specified subtopic
```
USER: Semantic triples such as ["Star", "emits", "Light"] and ["Rocket", "can bring cargo to", "Space"] consists of a subject, a predicate, and an object. Give me five examples of semantic triples that contain "Electron" as subject and return them in an array formatted like [["sub1", "pred1", "obj1"], ["sub2", "pred2", "obj2"], ...]. The topic of the semantic triples should be "Electrons in particle accelerators". Return nothing but the array without explanation.

SYSTEM: [["Electron", "accelerates in", "particle accelerator"], ["Electron", "collides with", "proton"], ["Electron", "produces", "synchrotron radiation"], ["Electron", "loses energy by", "radiating photons"], ["Electron", "deflects in", "magnetic field"]]
```

### Finding categories for the predicates

```
USER: Divide all aspects of the topic "Electron" into 5 topic areas. Return the result formatted as ["topic area 1", "topic area 2", ...]. Return nothing but the array without explanation.

SYSTEM: ["Properties of Electrons", "Behavior of Electrons in Atoms", "Electron Configurations", "Electron Charge and Mass", "Applications of Electrons"]


USER: Divide the topic "Applications of Electrons" which is subtopic of the topic "Electron" into 5 subtopic areas that cover all aspects. Return the result formatted as ["topic area 1", "topic area 2", ...]. Return nothing but the array without explanation.

SYSTEM: [\n    "Electron Microscopy",\n    "Electron Beam Welding",\n    "Electron Beam Lithography",\n    "Electron Beam Heating",\n    "Electron Beam Sterilization"\n]
```

### Navigation in the semantic network

```
USER: A semantic network is made of semantic triples which are made of a subject, a predicate and an object. You are trying to find the semantic triple ["Moon", "orbits", "Earth"] by navigating step by step through a semantic network. You are currently at the position of the triple ["Electron", "accelerates in", "particle accelerator"]. Your navigation options are: 1) Continue with "Electron" as subject. 2) Continue with "Electron" as object. 3) Continue with "particle accelerator" as subject. 4) Continue with "particle accelerator" as object. Return nothing but the index of your selection without explanation.

SYSTEM: 3


USER: Compare the terms A : "Electron" and B "particle accelerator" with the terms X : "Moon" and Y : "Earth". Which pairs of terms are most similar to each other? 1 : A and X. 2 : A and Y. 3 : B and X. 4 : B and Y. Return only the number of your answer as a single character without explanation.

SYSTEM: 2
```

### Comparison of triples

```
USER: A semantic triple consists of a subject, a predicate and an object. How similar are the semantic triples ["Moon", "orbits", "Earth"] and ["Moon", "orbits around", "Planet"]? 1: They make exactly the same statement. 2: The subjects are equal. 3: The objects are equal. 4: They are different. Return only the number of your answer as a single character without explanation.

SYSTEM: 4


USER: The semantic triple ["Moon", "orbits", "Earth"] consists of a subject, a predicate and an object. Can the predicate be substituted by "orbits around" without chancing the content of the semantic triple? Return y or n without further explanation.

SYSTEM y
```
The semantic triple ["Moon", "orbits", "Earth"] consists of a subject, a predicate and an object. Can the predicate be substituted by "orbits around" without chancing the statement of the semantic triple? Return y or n without further explanation.

