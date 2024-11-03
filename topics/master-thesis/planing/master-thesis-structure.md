# Master thesis structure

This is a structure tree of the master thesis. The topics are selected from [master-thesis-topic-list](master-thesis-topic-list.md).
The length of the master thesis should be ~60 pages


## Alternative table of contents

[abstract](../writing/abstract.md)

* Introduction
	* (???) [The importance of knowledge representation for scientific progress in physics](../writing/the-importance-of-knowledge-representation-for-scientific-progress-in-physics.md)
	* [what-is-a-semantic-network](../writing/what-is-a-semantic-network.md)
	* What is an ontology
	* Types of semantic networks
	* How is physics knowledge structured
	* [Goal of the master thesis](goal-of-the-master-thesis.md)
	* Overview
* Structuring the different subject areas of physics
	* Collecting physics terms (4 Pages)
		* [most-important-terms-of-topic-question](../../data/knowledge/most-important-terms-of-topic-question.md)
		* Using the Wikipedia page titles 
		* Manual selection
		* [Physics term generation using LLMs](../approaches/create-a-list-of-physics-terms-using-llms.md)
	* Creating a subtopic tree (11 Pages)
		* What is a subtopic tree
		* [subtopic-tree-algorithms-description
		* [visualization-of-the-subtopic-trees](../visualizations/visualization-of-the-subtopic-trees.md)
		* [Subtopic tree evaluation methods](subtopic-tree-average-number-of-viewed-terms-per-search-evaluation.md)](../approaches/subtopic-tree-algorithms-description.md)
		* [physics-term-adapted-subtopic-tree-evaluation](../evaluation/physics-term-adapted-subtopic-tree-evaluation.md)
		* [physics-term-adapted-subtopic-tree-evaluation-free-association-algorithm](../evaluation/physics-term-adapted-subtopic-tree-evaluation-free-association-algorithm.md)
		* [subtopic-tree-comparison](../evaluation/subtopic-tree-comparison.md)  + [comparison-of-frAss-and-subd-for-different-parameters](../evaluation/comparison-of-frAss-and-subd-for-different-parameters.md)
		* [subtopic-network-search-model-comparison](../evaluation/subtopic-network-search-model-comparison.md)
* Representing physical knowledge as semantic triples
	* Generating semantic triples of natural language (16 Pages)
		* What are the criteria for well formed triples ([see evaluation process validness](../evaluation/manual-triple-evaluation.md))
		* [physics-term-correlation-network-evaluation](../evaluation/physics-term-correlation-network-evaluation.md)
		* Triple generation with LLMs
			* Correlated triple generation [correlated-triples-evaluation](../evaluation/correlated-triples-evaluation.md)
			* Freely associated triples [free-associated-triples-evaluation](../evaluation/free-associated-triples-evaluation.md)
			* [comparison-of-frAss-and-subd-for-different-parameters](../evaluation/comparison-of-frAss-and-subd-for-different-parameters.md)
		* [Evaluation metric](false-choices-per-correct-choice-compared-to-random.md) for the correlated triples
		* [Manual triple evaluation](../evaluation/manual-triple-evaluation.md)
		* [Displaying the triples in a 2D plane](../approaches/mapping-a-high-degree-graph-to-a-2D-area.md)
* Answering physical questions with semantic networks
	* Navigating the knowledge base
		* [Navigating the triples](../approaches/navigate-semantic-triples-by-finite-choices.md)
	*  [Creating a semantic network of questions and answers](../approaches/semantic-network-of-questions-and-answers.md) 
		* [generating-networks-of-questions-and-answers](../evaluation/generating-networks-of-questions-and-answers.md)
		*  [checking-the-knowledge-consistency-of-large-language-models](../evaluation/checking-the-knowledge-consistency-of-large-language-models.md)
* Extracting semantic data from scientific texts
	* Building a citation graph using the [semantic-scholar-api](../extraction/semantic-scholar-api.md)
	* (3 Pages) 
		* [hepml-citation-graph](../extraction/hepml-citation-graph.md)
	* Triple generation using Stanford open IE
		* Paper content extraction
		* Quality evaluation
	* [converting-sentences-into-semantic-triples](../evaluation/converting-sentences-into-semantic-triples.md)
	* Creating a semantic network of sentences (5 Pages)
		* [Manual creation](../approaches/semantic-network-of-sentences.md) of a semantic network of sentences
		* [Automated creation](../approaches/semantic-network-of-sentences.md) of a semantic network of sentences
* Creating a physics ontology
	* Creating a specified semantic network (4 Pages)
		* Introduction to the topic area of top tagging
		* Creating a physics ontology
		* [Extracting the R30 values](r30-value-extraction.md)
		* Inserting them into the ontology
	*  Creating a general physics ontology with the help of LLMs
		* [generating-a-physics-ontology](../approaches/generating-a-physics-ontology.md)
		* [generate-knowledge-graph-based-on-an-ontology](../approaches/generate-knowledge-graph-based-on-an-ontology.md)
	* (???) Combining different types of semantic networks (???)
* Handling equations with semantic networks
	* Creating a semantic network of equations (5 Pages)
		* [Technical realization](../approaches/network-of-equations.md)
		* [Generating the network of equation with LLMs](../approaches/network-of-equations.md)
		* Combining [multiple equations](../approaches/network-of-multiple-equations.md) into one network
	* [Representing a derivation as knowledge graph](../evaluation/represent-a-derivation-as-a-semantic-network.md)
* Summary and outlook
	* Summary (1 Page)
	* [Possible applications](possible-applications-of-physics-knowledge-graphs.md) (4 Pages)
	* Conclusion (1 Page)


[The old table of contents](master-thesis-structure-old.md)