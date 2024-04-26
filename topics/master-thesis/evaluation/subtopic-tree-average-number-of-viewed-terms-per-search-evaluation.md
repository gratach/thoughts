# Subtopic tree average number of viewed terms per search evaluation

This is the proposed solution for the problem that there needs to be a good metric for evaluating the quality of a subtopic network in which several terms are classified. The metric should output a high quality if the single terms are easy to find within the subtopic network.

The proposed evaluation method is to calculate the ==average number of topics that have to be viewed to find the desired term==. For this, we assume that the entity that is searching the subtopic for a wanted term starts at the root note and looks at all available branches. Then it chooses one based on the word that it is searching for and repeats the process until it reaches the end of its search. ==If the search is terminated without success, it starts again at the root node== without remembering its previous choices. This is repeated so many times until it finds the wanted word. The quality of the subtopic tree is measured by counting the total number of choices that were offered to the entity during this process. This value could also be divided by the total number of leaf terms in the subtopic tree to get the performance improvement compared to just being offered a long list of all available words directly at the root node.

The average number of viewed terms $T_{view}$  is calculated in the following way:

$$
T_{view} = (N_{rep} - 1)T_{fail} + T_{suc} = (\frac{1}{P_{suc}} - 1)T_{fail} + T_{suc}
$$
Where $T_{suc}$ and $T_{fail}$ are the average number of viewed terms in a successful and failed search run and $N_{rep}$ is the average number of search run repetitions that is necessary to find the wanted term. $N_{rep}$ is equal to the inverse of $P_{suc}$ which is the probability that a search run is successful. The calculation uses the ==assumption that all terms are equally hard to find== which is a simplified model.

An other metric that penalizes longer term names is the total viewed bytes $B_{view}$ which is calculated analogously. 

A good impression of the quality of a subtopic tree is obtained if you calculate the ratio between $T_{view}$ and the total number of leaf terms within the subtopic tree or the ration between $B_{view}$ and the total number of bytes of the leaf terms. If this number is close to zero the classification is efficient. If the number is close to one or higher the classification is inefficient.
