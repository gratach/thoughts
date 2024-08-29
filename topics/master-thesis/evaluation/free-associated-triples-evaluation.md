The [false-choices-per-correct-choice-compared-to-random](../equations/false-choices-per-correct-choice-compared-to-random.md) metric that  [was previously applied](correlated-triples-evaluation.md) to the correlated triples was now also applied to the free associated triples.
Therefore `gpt-3.5-turbo`was asked to generate triples that have a subject from the list of the [dataset-of-1038-physic-terms](dataset-of-1038-physic-terms.md). For each term from this list `gpt-3.5-turbo`was prompted to generate a list of 5 triples that have this term as subject. From this 5 triples one was selected and the model was asked to identify its object from the selection of the objects of all 5 triples.

This evaluation was calculated for a total of 500 physics terms. The calculated number for the ==false object guesses per correct guess in relation to random guessing== is ==0.429±0.040==. This is lower than the same quantity that was calculated for the correlated triples (0.630±0.063). Therefore one can estimate that the meaningfulness of the freely associated triples is higher than the meaningfulness of the correlated triples.

For the 500 selected triples the most used predicates are "involves" with 15 occurrences, "is" with 11 occurrences and "describes" with 9 occurrences.

[Code](https://github.com/gratach/master-experimental/blob/5bbf1c990226d6becabb7745106fdb28792ee87c/evaluate_free_associated_triple_ambiguity.ipynb)
[Data](https://github.com/gratach/master-database-files/tree/abf2a8bbe921a69a0343d6c50af4d6b899538344/master-experimental/evaluate_free_associated_triple_ambiguity/object-identifying-tests/freeAssTr)
