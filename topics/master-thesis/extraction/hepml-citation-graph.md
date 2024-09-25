# Hepml citation graph

The hepml citation graph consists of papers that where extracted from the [HEPML Living Review](https://iml-wg.github.io/HEPML-LivingReview/) web page and from the search on [inspirehep](https://inspirehep.net/) for the terms ("machine learning" or "deep learning" or "neural") and (hep-ex or hep-ph or hep-th) via the [api](https://github.com/inspirehep/rest-api-doc)

[Code (HEPML Living review extraction)](https://github.com/gratach/master-thesis/blob/a5009d508233c47519090b0ef771ff2b3e7dbc35/semantic_paper/scripts/extract_hepml_papers.py) 
[Code (Inspirehep search)](https://github.com/gratach/master-thesis/blob/a5009d508233c47519090b0ef771ff2b3e7dbc35/semantic_paper/run.py) (commented out)
### General properties

Number of papers: 2409
Number of citations: 14928
Papers from “HEP ML Living Review”: 912
Papers from the Inspire search: 2223
Intersection of both: 726
Average references per paper: 6.22
Two papers that are connected within the citation graph have an average distance of 3.64 citations
Papers that could not be included because of errors: 53

### Most cited papers within dataset

 1) Jet-images - deep learning edition (175)
 2) Jet substructure at the Large Hadron Collider: A review of recent    advances in theory and machine learning (140)
3) Deep learning in color: towards automated quark/gluon jet discrimination (133)

### Papers citing most other papers within the dataset

1) A Living Review of Machine Learning for Particle Physics (385)
 2) Machine learning in the search for new fundamental physics (145)
 3) A guide for deploying Deep Learning in LHC searches: How to achieve optimality and account for uncertainty (118)
### The dataset in JSON Format

Converted the citation graph from the neo4j database into json format

[Code](https://github.com/gratach/master-experimental/blob/2eaafd9ceab3bc51526ca31211d39bc1091da15d/neo4j_citing_data_conversion.ipynb)
[Data](https://github.com/gratach/master-database-files/blob/b83870acf803a3ab10fa36fb1525221d6d94159a/master-experimental/neo4j_citing_data_conversion/papers.json)
