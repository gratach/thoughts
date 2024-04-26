# Error of binary event probability

When you know that some event has two possible outcomes, one positive with the probability $p$ and one negative with the probability $1 - p$, and you calculate $p$ based on $N$ measurements of the event - what is the error of this calculation?

$p$ can be calculated in the following way:

$$
p = \frac{N_{+}}{N}
$$
where $N_{+}$ is the number of positive outcomes of the experiments.

Given that $p$ has the value that was calculated in this way, what is the average error $\delta_{N_+}$ of $N_{+}$?

$$
\delta_{N_+} = \sqrt{\sum_{k = 1}^{N}\binom{N}{k}p^k(1-p)^{N - k}(k - N_+)^{2}}
$$
The error $\delta_p$ of $p$ if calculated a second time would then be

$$
\delta_p = \frac{\delta_{N_+}}{N}
$$
(See also [Wikipedia](https://de.wikipedia.org/wiki/Binomialverteilung#M%C3%BCnzwurf))