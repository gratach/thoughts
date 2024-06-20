# Experiments in physics

Idea: Create a ontology of experiments, models, constants

An list of experiments (Not only physics) can be obtained from:
[Wiki data SPARQL service](https://query.wikidata.org/)
With the query:
```
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P31 wd:Q101965.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

