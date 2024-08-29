# Hepml citation graph

The hepml citation graph consists of papers that where extracted from the [HEPML Living Review](https://iml-wg.github.io/HEPML-LivingReview/) web page and from the search on [inspirehep](https://inspirehep.net/) for the terms ("machine learning" or "deep learning" or "neural") and (hep-ex or hep-ph or hep-th) via the [api](https://github.com/inspirehep/rest-api-doc)

[Code (HEPML Living review extraction)](https://github.com/gratach/master-thesis/blob/a5009d508233c47519090b0ef771ff2b3e7dbc35/semantic_paper/scripts/extract_hepml_papers.py) 
[Code (Inspirehep search)](https://github.com/gratach/master-thesis/blob/a5009d508233c47519090b0ef771ff2b3e7dbc35/semantic_paper/run.py) (commented out)
### General properties

Total number of papers: 2429
Database entries of papers with error: 57
Total number of citations: 14730
Papers from “HEP ML Living Review”: 856
Papers from the Inspire search: 2266
Intersection of both: 698
Average references per paper: 6.2
Two papers that are connected within the citation graph have an average distance of 3.6 citations

### Most cited papers within dataset

 1) Jet-images - deep learning edition (171)
 2) Jet substructure at the Large Hadron Collider: A review of recent    advances in theory and machine learning (137)
3) Deep learning in color: towards automated quark/gluon jet discrimination (133)

### Papers citing most other papers within the dataset

1) A Living Review of Machine Learning for Particle Physics (385)
 2) Machine learning in the search for new fundamental physics (145)
 3) A guide for deploying Deep Learning in LHC searches: How to achieve optimality and account for uncertainty (118)
### The dataset in JSON Format

Converted the citation graph from the neo4j database into json format
The database seems to be not exactly the same version as the version that was used for the evaluation above.

[Code](https://github.com/gratach/master-experimental/blob/46b9ac4a21f213a4d9c7195b5759e352242c9ebe/neo4j_citing_data_conversion.ipynb)
[Data](https://github.com/gratach/master-database-files/blob/d4ef97fe1f6fe5a4e50b307143ba962404859eb0/master-experimental/neo4j_citing_data_conversion/papers.json)
