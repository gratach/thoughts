# Decision cost

To find out how efficient a [navigating agent](../approaches/navigate-semantic-triples-by-finite-choices.md) can find the answer to a question within a knowledge base one should count the amount of navigation decisions that the agent has made. Thereby not all decisions should be counted the same because some decisions are made based on a wider range of options and should therefore be given greater weight. 
During a successful triple search, the navigating agent makes a total of $N_{dec}$ decisions. Thereby for the decision with the index $i$ he selects option number $s_i$ from a selection of $c_i$ choices.
$$
s_i \in \{1, ..., c_i\}
$$
The important quantity to be calculated is the number of distinguishable decision paths $N_{path}$ that would have been possible. This number is equal to the product of the numbers of all possible options of all decisions.
$$
N_{path} = \prod_{i = 1}^{N_{dec}}c_i
$$
For convenience, we use an additive quantity that represents this number. Therefore we choose the logarithm of $N_{path}$.
$$
\log_{10}(N_{path}) = \sum_{i = 1}^{N_{dec}}\log_{10}(c_i)
$$
We call this quantity the decision cost. We have produced a dataset of triple searches that contains searches that where interrupted after a specific number of unsuccessful iterations. This is due to practical reasons like computing costs. Now, we want to make an estimation for the average decision cost that we would have measured if the searches were not interrupted. Therefore we make the approximate assumption that the probability of a search success within the one iteration is constant across all searches. Analogous to [this calculations](getting-the-average-search-length-from-a-dataset-of-interrupted-searches.md) we calculate the average decision cost that would have occurred in a non interrupted experiment  $C_{average}$ from the average decision cost of unsuccessful searches within our dataset $C_{fail}$,  the average decision cost of successful searches within our dataset $C_{success}$ and the probability that a search of our dataset is successful $P_{success}$.

$$
C_{average} = (\frac{1}{P_{success}} - 1)C_{fail} + C_{success}
$$
