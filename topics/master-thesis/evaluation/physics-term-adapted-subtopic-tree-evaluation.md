# Physics term adapted subtopic tree evaluation

Evaluation of the subtopic tree generated from the [master-adapted-subtopic-tree-generation](../../code/projects/master-adapted-subtopic-tree-generation.md) project and the [technical terms](https://github.com/gratach/master-database-files/blob/bcf75729e024abb289219e831c339a6292d6eb82/master-keyword-extraction/technical_terms.txt). The json data of the subtopic tree is [here](https://github.com/gratach/master-database-files/blob/468c729f480d6d775fe96fde7a50dfda08dc1a6d/master-adapted-subtopic-tree-generation/subtopic_tree.json).

## General properties

The subtopic tree contains ==1038 leafs== and 211 junction nodes. In average each leaf has a ==depth of 5.36== within the subtopic tree. The distribution of the leaf depth looks as follows:

![](term-depth-plot.svg)
When an optimal number of 5 subbranches per junctions is aimed for and the leafs are evenly distributed across the subtopic tree there should be an optimal target depth between 4 and 5 for the list of 1038 technical terms. ($5^4 = 625 < 1028 < 3125 = 5^5$)
The present distribution shows that there nearly 50% of the leafs are deeper than 5 steps in the subtopic tree. This makes the search for them inefficient.

The following plot shows the number of junction nodes that have a given number of subbranches attached to them.

![](number-of-subbranches-plot.svg)
There is a peak at a number of 5 subbranches. This is due to the fact, that during the creation of the subtopic network the model was advised to divide the topics of oversized  junctions into 5 topic categories. This mechanism was triggered when there are more than 15 subtopics per junction. This explains why there is no higher number of subbranches than 15. In the ideal scenario that was aimed for during the creation of the subtopic network there should  be only junctions with 5 subbranches. Small numbers of subbranches like 0 and 1 make the subtopic network inefficient while large numbers of subbranches like numbers higher than 10 makes it hard to navigate and to understand intuitively.

## Content properties

The root of the subtopic tree includes a division into the main branches 

* Quantum Mechanics and Atomic Physics (419 Terms)
* Astrophysics and cosmology (252 Terms)
* Fundamental Physics (142 Terms), 
* Statistical Physics and Thermodynamics (142 Terms)
* Applied Physics and Interdisciplinary Physics (74 Terms)

The category **fundamental physics** is thereby not well suited for the categorization of the terms because it overlaps with the other categories and is not clearly defined. The same applies to the term **Applied Physics**.

The biggest branch **Quantum Mechanics and Atomic Physics** contains the following subbranches:

* Quantum Mechanics (240 Terms)
* Atomic Physics (127 Terms)
* Classical Mechanics - (32 Terms)
* Electromagnetism and Phenomena - (17 Terms)
* Instrumentation and Measurement (2 Terms)

The subcategory **Classical Mechanics** is not correctly classified here. Also the category **Electromagnetism and Phenomena** is not a suited subbranch at this place.

The second biggest branch of the root junction **Astrophysics and cosmology** has only one subbranch **Astrophysics**. This is an example for an inefficient structuring of the subtopic tree.

Here are some randomly chosen examples of physic terms from the used dataset together with their paths in the subtopic tree:

```
Electromagnetics: ['Physics', 'Fundamental Physics', 'Classical Physics', 'Electromagnetism', 'Electromagnetics']

Bargmann–Wigner equations: ['Physics', 'Quantum Mechanics and Atomic Physics', 'Quantum Mechanics', 'Quantum theories and phenomena', 'Quantum Computing and Information', 'Quantum Field Theory and Particle Physics', 'Bargmann–Wigner equations']

Special theory of relativity: ['Physics', 'Astrophysics and Cosmology', 'Astrophysics', 'Gravitational Physics', 'Gravitational Physics', 'Cosmological and astrophysical features', 'Special theory of relativity']

Wave function collapse: ['Physics', 'Quantum Mechanics and Atomic Physics', 'Quantum Mechanics', 'Quantum theories and phenomena', 'Foundations of Quantum Mechanics', 'Core principles and formulations', 'Quantum Interpretations and Theories', 'Wave function collapse']

Ising model: ['Physics', 'Statistical Physics and Thermodynamics', 'Thermodynamics', 'Properties of Matter', 'Magnetic Properties', 'Ising model']
```

In principle the classification of the mentioned examples is understandable and makes sense. There are a few flaws though: 
* As mentioned earlier **Fundamental Physics** is no good category for **Electromagnetics** because it is to general . 
* The **Special theory of relativity** does not only occur in **Astrophysics and Cosmology** but also in high energy physics.
* The **Bargmann–Wigner equations** are classified as part of **Quantum Computing and Information**, even if these equations are not directly related to this field. 
* In the path of **Special theory of relativity** the category **Gravitational Physics** occurs twice

To test the efficiency of the subtopic network the [average number of viewed terms per-search evaluation](subtopic-tree-average-number-of-viewed-terms-per-search-evaluation.md) was performed. The total number of viewed terms per search is:
$144 \pm 13$. This is ==13.8 ± 1.2%== of the total physics terms. The viewed bytes are ==17.5 ± 1.5%== of the total term byte information.