# Physics ontology introduction

## (German)

In der bisherigen Arbeit haben wir untersucht wie physikalisches Wissen aus vielen verschieden Bereichen als semantisches Netz dargestellt werden kann. Dabei haben wir die Struktur des semantischen Netzes möglichst allgemein gehalten, sodass ein breites Spektrum an unterschiedlichen Informationen dadurch abgebildet werden kann. Eine große Flexibilität bei der Strukturierung der Daten bedeutet jedoch, dass eine Vereinheitlichung der Informationen zur automatischen Auswertung erschwert werden. Eindeutige Vorgaben bezüglich der Struktur des semantischen Netzwerkes können hingegen zu einer klareren inhaltlichen Strukturierung des knowledge graphs führen und eine zielgerichtete Verarbeitung und Auswertung der physikalischen Daten ermöglichen, die hierfür jedoch auf ein kleineres Wissensgebiet eingeschränkt werden. Solch eine klarere Struktur eines semantischen Netzwerkes kann mit Hilfe einer Ontologie erreicht werden. Wie bereits im Abschnitt [[what-is-a-ontology]] gezeigt wurde definiert eine Ontologie Regeln welche Art von Konzept Klassen erlaubt sind und welche Art von Verbindungen zwischen den Konzepten der verschiedenen Klassen existieren können.
Die Fragestellung wie man physikalische Forschungsdaten mit Hilfe einer Ontologie in ein maschinenlesbares und verstehbares Format bringen kann wurde bereits wissenschaftlich in einem Paper untersucht [^say2020semantic]. In dieser Veröffentlichung schlagen die Autoren die Ontologie "Physci" vor, die sich auf verschiedene Aspekte der Forschung im Bereich der Physik konzentriert. Diese OWL Ontologie, die unter der Creative Commons Lizens veröffentlicht wurde demonstriert, dass es möglich ist physikalisches Wissen nach einem vorgegebenen Schema zu organisieren. Sie verwendet dazu OWL Klassen wie "ScientificProblem", "physicalLaw" und "ScientificArgument" 

Es soll nun untersucht werden welche Möglichkeiten zur Einführung von Ontologien in der Physik bestehen und wie die geschaffenen Ontologien mit Daten gefüllt werden können.

## (English)

In our previous work, we have investigated how physical knowledge from many different areas can be represented as a semantic network. We have kept the structure of the semantic network as general as possible so that a wide range of different information can be represented. However, great flexibility in structuring the data means that standardizing the information for automatic evaluation is more difficult. Clear specifications regarding the structure of the semantic network, on the other hand, can lead to a clearer content structuring of the knowledge graph and enable targeted processing and evaluation of the physical data, which is, however, restricted to a smaller area of ​​knowledge. Such a clearer structure of a semantic network can be achieved with the help of an ontology. As already shown in the section [[what-is-a-ontology]], an ontology defines rules about which type of concept classes are allowed and which type of connections can exist between the concepts of the different classes. The question of how to use an ontology to bring physical research data into a machine-readable and understandable format has already been scientifically investigated in a paper [^say2020semantic]. In this publication, the authors propose the ontology "Physci", which focuses on various aspects of research in the field of physics. This OWL ontology, which was published under the Creative Commons license, demonstrates that it is possible to organize physical knowledge according to a given scheme. It uses OWL classes such as "ScientificProblem", "physicalLaw" and "ScientificArgument" We will now investigate what options there are for introducing ontologies in physics and how the created ontologies can be filled with data.


[Physics models ttl data](https://github.com/gratach/master-thesis/blob/a5009d508233c47519090b0ef771ff2b3e7dbc35/owl_ontology/physics_models.ttl)

[^say2020semantic]: ```@book{say2020semantic,
  title={Semantic representation of physics research data},
  author={Say, Aysegul and Fathalla, Said and Vahdati, Sahar and Lehmann, Jens and Auer, S{\"o}ren},
  volume={2},
  year={2020},
  publisher={[Set{\'u}bal]: SCITEPRESS-Science and Technology Publications, Lda.}
}```