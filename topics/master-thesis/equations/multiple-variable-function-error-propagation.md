# Multiple variable function error propagation

When we have $x_n$ with uncertainties $\delta_{x_n}$ the error of $f(x_1, ... , x_n)$ can be approximated by:

$$
\delta_f = \sqrt{(\frac{\partial f}{\partial x_1}\delta_{x_1})^2 + ... + (\frac{\partial f}{\partial x_n}\delta_{x_n})^2}
$$
Source: [https://courses.washington.edu/phys431/propagation_errors_UCh.pdf](https://courses.washington.edu/phys431/propagation_errors_UCh.pdf)