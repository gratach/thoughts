# Master thesis structure

This is a structure tree of the master thesis. The topics are selected from [master-thesis-topic-list](master-thesis-topic-list.md).
The length of the master thesis should be ~60 pages

* Introduction (7 Pages)
	* (???) [Brief introduction into the history of knowledge representation in physics](../writing/the-importance-of-knowledge-representation-for-scientific-progress-in-physics.md)
	* What is a semantic network
	* What is an ontology
	* Types of semantic networks
	* How is physics knowledge structured
	* [Goal of the master thesis](goal-of-the-master-thesis.md)
	* Overview
* Building a citation graph (3 Pages)
	* What is a cite graph 
	* How to obtain citation data
	* How to handle the data
* Creating a specified semantic network (4 Pages)
	* Introduction to the topic area of top tagging
	* Creating a physics ontology
	* Extracting the R30 values
	* Inserting them into the ontology
* Creating a subtopic tree (11 Pages)
	* What is a subtopic tree
	* The subdivision algorithm
	* The free association algorithm
	* [Subtopic tree evaluation methods](subtopic-tree-average-number-of-viewed-terms-per-search-evaluation.md)
* Generating semantic triples of natural language (16 Pages)
	* What are the criteria for well formed triples ([see evaluation process validness](../evaluation/manual-triple-evaluation.md))
	* Triple generation using Stanford open IE
		* Paper content extraction
		* Quality evaluation
	* Triple generation with LLMs
		* Correlated triple generation
		* Freely associated triples
	* [Evaluation metric](false-choices-per-correct-choice-compared-to-random.md) for the correlated triples
	* [Manual triple evaluation](../evaluation/manual-triple-evaluation.md)
	* [Navigating the triples](../approaches/navigate-semantic-triples-by-finite-choices.md)
	* [Displaying the triples in a 2D plane](../approaches/mapping-a-high-degree-graph-to-a-2D-area.md)
* Collecting physics terms (4 Pages)
	* Using the Wikipedia page titles
	* Manual selection
	* [Physics term generation using LLMs](../approaches/create-a-list-of-physics-terms-using-llms.md)
* Creating a semantic network of equations (5 Pages)
	* [Technical realization](../approaches/network-of-equations.md)
	* [Generating the network of equation with LLMs](../approaches/network-of-equations.md)
	* Combining [multiple equations](../approaches/network-of-multiple-equations.md) into one network
* Creating a semantic network of sentences (5 Pages)
	* [Manual creation](../approaches/semantic-network-of-sentences.md) of a semantic network of sentences
	* [Automated creation](../approaches/semantic-network-of-sentences.md) of a semantic network of sentences
* (???) Creating a semantic network of questions and answers (???)
* (???) Combining different types of semantic networks (???)
* Summary and outlook (6 Pages)
	* Summary (1 Page)
	* [Possible applications](possible-applications-of-physics-knowledge-graphs.md) (4 Pages)
	* Conclusion (1 Page)

