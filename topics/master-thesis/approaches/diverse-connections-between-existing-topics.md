# Diverse connections between existing topics

The goal of this approach is to create semantic connections between the terms of the [dataset-of-1038-physic-terms](../evaluation/dataset-of-1038-physic-terms.md).

The following are the steps to be taken:
* Select a term from the list
* Find other terms that are related to the first term by selecting a random subset of terms from the list and asking the LLM which of these terms is most related to the content of the first term. Repeat this until you have a small number of related terms.
	* **Edit**: The related terms can be found by selecting the neighboring leafs of the [subtopic trees](../evaluation/subtopic-tree-comparison.md)  
* Ask the LLM to find a predicate that connects the first term with one of the related terms. Give some examples how a predicate that connects two terms might look like.
* For evaluation check if the LLM can identify the connected term out of the list of related terms only by knowing the connection.