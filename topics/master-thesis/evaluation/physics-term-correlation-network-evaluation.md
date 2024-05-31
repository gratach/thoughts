A network of correlated physics terms was created in the following way by the [master-adapted-subtopic-tree-generation](../../code/projects/master-adapted-subtopic-tree-generation.md) project:

The correlation network ```tree_cor``` was created by connecting all terms from the [dataset-of-1038-physic-terms](dataset-of-1038-physic-terms.md) that are neighboring leafs in one of the six subtopic trees ```[subd, fr_as_ex, fr_as_rsb_15, fr_as_rsb_16, fr_as_sb_10, fr_as_sb_15]``` of the [subtopic-tree-comparison](subtopic-tree-comparison.md). 

The graph has ==10061 edges== an ==average degree of 19.39== a maximal degree of 39 and a minimal degree of 3. It forms one connected unit and has an ==average path length== between two randomly selected terms of ==3.18==.

Using this graph as a foundation the ```tree_cor_mi``` network was created by asking ```gpt-3.5-turbo``` for the 5 strongest connections per term. Therefore the selection of connections to choose from was expanded to include some random connections where necessary.

This graph has ==3234 edges== an ==average degree of 6.23== a maximal degree of 15 and a minimal degree of 1. It forms one connected unit and has an ==average path length== between two randomly selected terms of ==4.95==.

The minimal degree of 1 is a result of multiple errors in the answers of ```gpt-3.5-turbo```. To correct this an other graph ```tree_cor_mi_man``` was created by adding a small number of connections manually.

The resulting graph has ==3247 edges== an ==average degree of 6.26== a maximal degree of 15 and a minimal degree of 5. It forms one connected unit and has an ==average path length== between two randomly selected terms of ==4.94==.

The five most connected terms within this graph are:

| term                    | number of connections |
| ----------------------- | --------------------- |
| Magnetic fields         | 15                    |
| Quark                   | 15                    |
| Ferromagnetism          | 14                    |
| Internal energy         | 13                    |
| Volume (thermodynamics) | 13                    |

Here are tree randomly selected terms with their connected terms:

Geophysics
* Earth's magnetic field
* Outgassing
* Magnetosphere
* Van Allen radiation belt
* Solar wind
* Physical oceanography
* Proca action

Amorphous solid
* Crystal
* Crystallography
* Solid-state physics
* Lattice model (physics)
* Nucleation
* Phase (matter)
* Ductility

Gamma-ray astronomy
* Fermi Gamma-ray Space Telescope
* Compton Gamma Ray Observatory
* Gamma ray astronomy
* Gamma ray burst
* Synchrotron emission
* Supernova