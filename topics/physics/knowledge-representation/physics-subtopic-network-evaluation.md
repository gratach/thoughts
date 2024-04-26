# Physics subtopic network evaluation

With the [master-simple-relations](../../code/projects/master-simple-relations.md) project a subtopic tree was generated.

Here is the particle physics branch of the subtopic tree

```
Physics
  Classical Mechanics
  Quantum Mechanics
  Thermodynamics
  Electromagnetism
  Optics
  Relativity
  Particle Physics
    Quantum Field Theory
      Quantum Electrodynamics
        Quantum Field Theory -> *
        Particle Physics -> *
        Renormalization
        Feynman Diagrams
        Quantum Mechanics -> *
      Quantum Chromodynamics
        Quark Confinement
        Asymptotic Freedom
        Color Charge
        Gluons
        Lattice QCD
      Quantum Field Theory in Curved Spacetime
      Renormalization -> *
      Perturbation Theory
      Path Integrals
      Gauge Symmetry
      Symmetry Breaking
      Anomalies
    Standard Model
      Elementary Particles
        Quantum Field Theory -> *
        Particle Physics -> *
        Standard Model -> *
        Fermions
          Quantum mechanics
          Particle physics
          Spin
          Quantum field theory
          Quantum statistics
        Bosons
        Leptons
        Quarks
        Electroweak Interaction
        Strong Interaction
        Higgs Boson
      Quantum Field Theory -> *
      Particle Physics -> *
      Quantum Chromodynamics -> *
      Electroweak Interaction -> *
    Quantum Chromodynamics -> *
    Electroweak Theory
      Higgs boson
      Gauge symmetries
      Weak force
      Electromagnetic force
      Quantum field theory -> *
    Higgs Mechanism
      Electroweak Symmetry Breaking
      Standard Model of Particle Physics
      Spontaneous Symmetry Breaking
      Elementary Particle Physics
      Quantum Field Theory -> *
  Astrophysics
  Nuclear Physics
  ```

In general the subtopics within this graph are accurate and involve no hallucination.
In many cases subtopics are referenced that do already appear in other places within this graph. They are marked by the ```-> *``` symbol. This also includes situations where the subtopic tree has a subtopic that is more general than its topic. For example "Quantum Electrodynamics" has the two subtopics "Particle Physics" and "Quantum Mechanics".

There is also an example of a duplicate topic that is registered twice within the database: "Quantum Mechanics" exists with two different spellings (the M written big and small). This is due to the fact that there is no mechanism to ensure that for each concept exists only one natural language term (see [one-natural-language-term-for-each-concept-approach](../../data/knowledge/one-natural-language-term-for-each-concept-approach.md))

Some metric to measure the quality of a subtopic network could also be implemented by a subtopic search for specific keywords