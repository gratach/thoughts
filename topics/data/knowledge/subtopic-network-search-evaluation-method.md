# Subtopic search evaluation method

Metric to measure the quality of a subtopic network:

* Obtain a list of terms that belong to the topic area of the root topic of the subtopic network.
* For each term start at the root topic and ask the question: 'Which of the following topics \<list of subtopics\> is most likely to contain the keyword \<search term\>?'  
* Navigate to the chosen subtopic and repeat this step until the wanted term has been found or a number of N iterations have been surpassed
* The fraction of the successful searches against the total searches is an indicator for the quality of the subtopic network.

This subtopic search has been implemented in [master-subtopic-network-search](../../code/projects/master-subtopic-network-search.md)
