# Automated prove checking

Next we want to investigate the question wehter it is possible to perform an automated proof checking algorithm on the semantic network of equations. This can be done by using a large language model like ```gpt-4-turbo```. Testing the ability of large language models to solve mathematical equations is beyond the scope of this master thesis but there is already research on this topic. [^fang] Because these models are not perfectly reliable, one cannot completely trust their assessment of the correctness of derivations. However, the method can be used to find potential errors in the derivation.

The network of equations from above was tested for correctness by the model `gpt-4-turbo`. For comparison an other slightly altered version of the network was tested with the same method. The equations of the second network were changed in a way, that the reasoning of the derivation is no longer correct.

From the five slightly altered reasoning steps `gpt-4-turbo`correctly identified all as false.
From the five original reasoning steps of the derivation `gpt-4-turbo`identified all except for one as correct. This one reasoning step is that a sum of solutions to the Schrödinger equation is also solution which is derived from the linearity of the Schrödinger equation.

This is due to the fact that the following notation is not completely clear because it does not explain, that the $\psi_n$ must be also solutions to the Schrödinger equation.
$$
i\hbar\frac{\partial}{\partial t}\psi(x,t) = -\frac{\hbar^2}{2m}\Delta\psi(x,t)+V(x)\psi(x,t) \Rightarrow \psi(x,t) = \sum_n \psi_n(x, t)
$$
This is an information, that is encoded in the symbol explanations which where not included in the evaluation process.

[Code](https://github.com/gratach/master-experimental/blob/fd3e8a4b4e1fe2e469d651de5969380344317070/checking_derivations.ipynb)

[^fang]:```
@misc
{fang2024mathodysseybenchmarkingmathematicalproblemsolving,
      title={MathOdyssey: Benchmarking Mathematical Problem-Solving Skills in Large Language Models Using Odyssey Math Data}, 
      author={Meng Fang and Xiangpeng Wan and Fei Lu and Fei Xing and Kai Zou},
      year={2024},
      eprint={2406.18321},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.18321}, 
} 