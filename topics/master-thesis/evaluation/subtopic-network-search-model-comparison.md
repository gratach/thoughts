A comparison of the ability of different models to generate a subtopic tree in which different keywords should be found

| Model               | Found   | Iterations | Subtopics  | Stability |
| ------------------- | ------- | ---------- | ---------- | --------- |
| gpt-4-turbo         | 71±4.5% | 3.30±0.19  | 10.37±0.17 | 86±4.9%   |
| mistral_7b_instruct | 63±4.8% | 3.24±0.23  | 9.34±0.14  | 78±5.9%   |
| gpt-3.5-turbo       | 56±5.0% | 3.25±0.25  | 6.68±0.11  | 80±5.7%   |
| cosmosage           | 48±5.0% | 3.92±0.35  | 14.97±0.52 | 64±6.7%   |

The columns have the following meaning:
- **Found** : The percentage of the keywords that are found in the subtopic network
- **Iterations** : The average iterations after which the successfully found keywords can be located
- **Subtopics** : The average number of subtopics that are generated for each topic within the subtopic tree
- **Stability** : The percentage of keywords that achieve the same result in two independent runs

The search is performed using the gpt-3.5-turbo model which is iteratively choosing the subtopic in wich the keyword is most likely to occur. The search process is getting interrupted after 10 unsuccessful iterations for each keyword.

For the search a [dataset of 50 physics terms](dataset-of-50-physic-terms.md) is used twice so that a total of 100 independent keyword searches are performed per model.

A keyword is considered as found if it occurs within the string of the selected subtopic. Upper and lower case letters are being ignored

The errors are calculated based on [error-of-binary-event-probability](../formula/error-of-binary-event-probability.md)