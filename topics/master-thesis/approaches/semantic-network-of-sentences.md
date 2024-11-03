# Semantic network of sentences

Natural language is a complex and expressive construct that is able to represent even detailed and complicated information. This pushes the representation possibilities of a semantic network that consists only of triplets to its limits. Some sentences can not be expressed in a nice way by purely using semantic triples. An example is the sentence:

```A electron is thought to be elementary particles because it has no known components or substructure.```

This can be disassembled into the triples ```["Electron", "is thought to be", "Elementary particle"]``` and ```["Electron", "has no known", "Substructure"]``` but the causality between those two statements can not be expressed within the scope of this semantic semantic network design.

A solution for this problem is to use a semantic network design, that is more adapted to the structure of natural language. This design for a semantic network of sentences uses a more complex structure for representing physics knowledge. The graphic below illustrates how the sentence from above would be depicted in such network.

![](./images/electron_sentences_detail.svg)This network consists of four terms, illustrated by blue ellipses and four sentence fragments, depicted by red diamond shapes followed by a tail of orange arrows. The terms correspond to the subjects and objects of the network of semantic triples and represent concepts that stand by themselves. The example network uses the terms "Electron", "Elementary particle", "Components", and "Substructure". The sentence fragments are sequences of content placeholders and linking words that can be read like a natural language sentence in the order indicated by the orange arrows. The content placeholders are depicted by the little orange circles. For each content placeholder, a thin grey arrow shows which content has to be inserted at that place. For example, terms like "Electron" or "Elementary particle" can be inserted into the content placeholders. The linking words are depicted by the yellow boxes. Their role is to connect the concepts similar to the predicates in the network of semantic triples. The leftmost sentence fragment in the graphic represents the sub-sentence, "An electron is thought to be an elementary particle." It connects the concepts "Electron" and "Elementary particle" with the linking words "is thought to be". In this case, the content of the sentence fragment is a statement. A sentence fragment can also describe a concept. For example, the rightmost sentence fragment in the graphic represents the concept of "Known components or substructure". The content placeholders can not only be a placeholder for the terms but also for the content of other sentence fragments. In this case, the grey arrow points from the red diamond shape of the sentence fragment that should be inserted into the content placeholder to the content placeholder. For example, the topmost sentence fragment in the graphic represents the sentence "Electron has no known components or substructure" by inserting the leftmost sentence fragment into its second content placeholder. The bottommost sentence fragment finally connects the leftmost and topmost sentence fragments and creates a causality between them. 

The graphic below shows the first paragraph of the Wikipedia article about electrons converted into a sentence network. The highly connected node in the center is the concept "Electron". The conversion from the plain text to the sentence network was done manually.

![](./images/electron_sentences_overview.png)

The resulting network is able to store most nuances of the used text. It also extracts all concepts that occur in the text and links them with each other. The approach is scalable but requires a lot of curation work. The main challenge is it to link cross references between sentences and disassemble the sentences in their atomic parts.

[code](https://github.com/gratach/master-experimental/blob/fe292da66c71d86032288a259a474089b8d28ce7/sentence_networks.ipynb)
[data](https://github.com/gratach/master-database-files/tree/85923aa26df2e6c154b7bab7f9418bb798bd3916/master-experimental/sentence_networks)
### Automating the construction of the sentence network

After doing the creation of the semantic sentence network manually, an attempt was made to automate the process of converting a given text into this format. For this purpose a pipeline was built that starts with the plain text and splits it into sentences using the natural language toolkit Python package. Next, the coreferences within the sentences get resolved by asking the LLM to replace all occurrences of references like "it" or "this"  by the actual words that are referenced by them. Finally the LLM is asked to mark the concepts within the resolved sentences, which are than isolated from the rest of the sentences by using a python algorithm. This information is then used to build the sentence network.

For testing this approach the same paragraph was used that was also used for the manual creation. The resulting graph that is shown below is not completely connected. This is due to the algorithm distinguishing between the concepts "Electron" and "Electrons"

![](./images/electron_sentences_overview_automated.png)

There are also some limitations of the chosen conversion algorithm. While the manual construction of the sentence network units of meanings could be identified and isolated also within sentences, such fine grained resolution is not possible with the automated approach. Instead every sentence produces exactly one word structure. Also this algorithm does match concepts as equal when they are represented by the same string. Synonyms or identical words that describe different things will not be taken into account accordingly.

[data](https://github.com/gratach/master-database-files/tree/0aa58c96d11212d5dcdfb46d77e70daec90a97ab/master-experimental/split_sentences)
[code](https://github.com/gratach/master-experimental/blob/b2d45c4ab16e058091a868f2539ff3e02c6bec27/split_senteces.ipynb)

