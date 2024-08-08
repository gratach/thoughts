# Generate knowledge graph based on an ontology

Next we want to investigate the question if we can also automate the process of creating a knowledge graph that is based on the ontology. To accomplish this we want to introduce an algorithmic approach that can generate individuals of the classes and connect them via the allowed relations. Once again we want to separate the process into two smaller steps that can be automated using the language model `gpt-4-turbo`. First a list of named individuals is generated for each class. The following query was used to generate the individuals:

```
I want to build a knowledge graph, that is based on an ontology.
Therefor I want to collect instances of the class <class name>.
I want to add <number of instances> new instances of this class.
The instances should have unique names that are written in camel case.
Return the names of the new instances in the format ["first instance name", "second instance name", ...].
Return nothing but this list.}
```

The generated individuals are then connected via the allowed relations. The following query was used to generate the connections:

```
I want to build a knowledge graph, that is based on an ontology.
Therefore I want to connect instances of the classes \textcolor{red}{<subject class>} and \textcolor{red}{<object class>} with the relation \textcolor{red}{<relation name>}.
The individuals of the domain class <subject class> are <list of subject class individuals>.
The individuals of the range class <object class> are <list of object class individuals>.
Which of these individuals should be connected with each other using the relation <relation name>?
Return the connections in the format [["first subject name", "first object name"], ["second subject name", "second object name"], ...].
If non of the listed instances should be connected, you can introduce new instance names to connect them with the already existing ones.
They should be written in camel case.
Return all possible connections.
Return nothing but this list.}
```
  
Using this approach a knowledge graph was generated that is based on the ontology that was created in the previous step. The knowledge graph contains 156 individuals and 254 connections between them. The content of the knowledge graph is not very meaningful because the individuals and connections were generated randomly. In some cases the naming of the individuals that is used by `gpt-4-turbo` is unconventional. For example the individuals of the class "PhysicalProperty" are named with the suffix "Measurement": "DensityMeasurement", "MassMeasurement", "PressureMeasurement" and so on. Also not all parts of the knowledge graph are completely physics related because some of the classes like "ScientificEquipment" or "ResearchArea" are not directly related to physics. Some relations provide a better way of connecting concepts in a meaningful way than others. While the object property "identifiedAsAstronomicalObject" that connects the "AstronomicalObject" class with itself is not very useful, the object property "requiresScientificEquipment" that connects the "PhysicalExperiment" class with the "ScientificEquipment" class can be used to model useful information about the required equipment for a specific experiment. In some cases `gpt-4-turbo` has chosen to connect all possible combinations of individuals of two classes with a given relation. This can lead to a large number of connections that are not meaningful. For example the object property "definesPhysicalProperty" connects all individuals of the "PhysicalConcept" class with all individuals of the "PhysicalProperty" class.

  

Even if the knowledge graph has some limitations, it also contains some useful information.
The following list shows examples for useful triples that are contained in the knowledge graph:

* ("SpecialRelativity", "basedOnPhysicalConcept", "LorentzInvariance")
* ("KeplersLaws", "describePhysicalPhenomenon", "OrbitalMotion")
* ("solarPanelInstallation", "involvesEnergyType", "SolarEnergy")
* ("QuantumMechanics", "involvesPhysicalConstant", "PlancksConstant")
* ("entanglement", "partOfPhysicalTheory", "QuantumMechanics")

These results demonstrate that it is possible to generate a knowledge graph that is based on an ontology using the language model `gpt-4-turbo`. The quality of the generated knowledge graph is not always perfect, but it could be potentially improved by refining the ontology and the process of generating the individuals and connections.

[Code](https://github.com/gratach/master-experimental/blob/6c076f2a032d05a5ad94179f383e377551fb5826/generate_individuals_based_on_ontology.ipynb)
[Data](https://github.com/gratach/master-database-files/blob/03184c8dc1b2e3d877b5200f6b75cc6c583be799/master-experimental/generated_ontology/researchAreaSeeded/knowledge_graph.ttl)

