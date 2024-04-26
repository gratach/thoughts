# How to obtain a list of the most important terms of some topic?

One could try to extract them from a text. Therefore one could use an keyword extraction software tool like the python spacy library to get all terms from a text and than use some other selection method to pick the important ones.

The quality of the [extraction result](https://github.com/gratach/master-keyword-extraction/blob/main/print_paricle_physics_entities.py) from spacy is not very high. When extracting the most important terms from the introduction of the [wikipedia page "Particle Physics"](https://en.wikipedia.org/wiki/Particle_physics) the result is:
```
(three, first, first, three, Quarks, Hadrons, Two, Mesons, only a few hundredths, Mesons, the Standard Model, the Large Hadron Collider, two, Higgs)
```
It should be something like:
```
(fundamental particles, forces, matter, radiation, protons, neutrons, nuclear physics, universe, Standard Model, fermions, bosons, up quark, down quark, electorn neutrino, electormagnetism, weak interaction, strong interaction, hadrons, baryons, mesons, microsecond, cosmic rays, cyclotrons, particle accelerators, antiparticles, mass, electric charges, electron, positron, antimatter, photon, elementary particles, quantum field, reconcilliation of gravity, loop quantum gravity, string theory, supersymmetry theory, radioactive, large hadron collider, cosmology, quantum theory, higgs boson)
```
Within the Wikipedia article these relevant terms are mainly those who are marked as a link. So one could write an [extraction algorithm](https://github.com/gratach/master-keyword-extraction/blob/main/get_wikipedia_technical_terms.py) that gets all the titles of the linked wikipedia articles and filters them for physics related topics by using a large language model.
