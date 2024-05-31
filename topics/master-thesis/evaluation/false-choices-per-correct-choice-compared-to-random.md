# False choices per correct choice compared to random

For the evaluation of the semantic triple predicates that are generated for a given subject and a given object the following approach is used:

For each pair of predicate and subject a large language model has to guess which object belongs to the triple. The quality of the generated predicate is better the better the LLM is at choosing correct object. However the difficulty of choosing the right object is also higher if there are more options provided to choose from. This variable should be excluded from the evaluation of the predicate.

To accomplish this the following approach is used:

A metric for the quality of the predicates $Q_{pred}$ is the false choices per correct choices fraction $\frac{FC}{CC}$ divided by the fraction of false choices per correct choices when guessing randomly $\frac{FC_{rand}}{CC_{rand}}$. 

$$Q_{pred} = \frac{\frac{FC}{CC}}{\frac{FC_{rand}}{CC_{rand}}}$$

The following applies:

$$\frac{FC}{CC} = \frac{FP}{1 - {FP}}$$

Where  $FP =  \frac{FC}{FC + CC}$ is the proportion of the false choices out of the total choices. The error $\delta_{FP}$ of $FP$ can be calculated as described in [error-of-binary-event-probability](../formula/error-of-binary-event-probability.md). Following the [error propagation rules](../formula/multiple-variable-function-error-propagation.md) the error $\delta_{Q_{pred}}$ of  $Q_{pred}$ is:

$$\delta_{Q_{pred}} = \frac{\delta_{FP}}{{(1 - {FP})^2}\frac{FC_{rand}}{CC_{rand}}}$$
