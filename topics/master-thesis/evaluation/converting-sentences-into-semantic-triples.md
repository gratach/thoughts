# Converting sentences into semantic triples

Next it should be tested if sentences about physics can be converted into semantic triples and back without loosing information. This was tested for the [Wikipedia article about electrons](https://en.wikipedia.org/wiki/Electron). The text was extracted from the website and split into sentences using the natural language toolkit. Then, the dataset of sentences was filtered by the large language model to only include sentences that stand by them self and do not contain any references to the context. The resulting dataset contains 231 sentences. In the next step `gpt-3.5-turbo`was used to convert the sentences into semantic triples using the following prompt:
```
The sentence "The Earth orbits the sun at a distance of 1 AU." can be converted to the semantic triples:
[["Earth", "orbits", "Sun"],
["Earth", "has a distance from the sun of", "1 AU"]]
What are the semantic triples for the sentence: "<sentence>"?
Return nothing but the semantic triples in the format above.
```
As a result an average of 2.99 $\pm$ 0.11 triples were generated per sentence. Of the 690 triples, 84 contain the words electron or electrons as subject while 25 contain one of those words as object. The most frequently used predicates are "is", "is a" and "are" that together are used 41 times. The predicates "has" and "have" is used 37 times. The  predicate "include" is used 27 times.

While the triples mostly contain the most important elements of the sentences some nuances of the sentence content are getting lost during the transformation. For example the sentence "Laboratory instruments are capable of trapping individual electrons as well as electron plasma by the use of electromagnetic fields." is converted into the triples "Laboratory instruments" "are capable of trapping""individual electrons", "Laboratory instruments" "are capable of trapping" "electron plasma" and "Laboratory instruments" "use" "electromagnetic fields". Thereby the information is lost that the trapping of the electrons and the plasma works by using electromagnetic fields.

In order to test how much information was lost by transforming the sentences into triples the triples were transformed back into sentences which were then compared to the original sentences. The back transformed version of the triples from the previous example is "Laboratory instruments are capable of trapping individual electrons, electron plasma, and use electromagnetic fields.". The length of the back transformed versions of the sentences is in average 10.6 $\pm$ 1.6% shorter then the length of the original sentences. This indicates that approximately 10% of the information was lost during the transformation. 

To analyze what kind of information was lost it was calculated which were the most common words that appeared in the original text but were missing in the transformed text. Among those words are terms like "when" (left out 10 times), "by" (left out 10 times) and "because" (left out 9 times). These terms are linking different parts of the sentences and create causalities between them. They are important to construct more complex statements that can not be expressed purely by the more compact semantic triples. This missing expressiveness illustrates the limitations of the approach to represent knowledge as semantic triples.

[Code](https://github.com/gratach/master-experimental/blob/61718ce7f00a060edae178395bbe254bbab9169e/convert_sentences_to_triples.ipynb)
[Data](https://github.com/gratach/master-database-files/tree/9669cfa7b56bec8cf7507d7b9d9bbc5fd3a16cd4/master-experimental/convert_sentences_to_triples)
