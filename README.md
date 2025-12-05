# qmc-pi-estimation

## Overview
The Quasi-Mone Carlo π estimation algorithm is a set of tools based on
the Monte Carlo method. The program runs Quasi (QMC) and ”normal” Monte
Carlo (MC) simulations, plots their convergence rates and graphs the scatter
plot of points used in the QMC. 

This project is designed to highlight the differences between random and de-
terministic sampling approaches. At the same time, it helps further develop my
Python programming skills and lays the foundation for more complex, statistic-
heavy topics.

## Features


- Sobol QMC (deterministic version of MC, which chooses evenly spaced
points using the Sobol sequence)
- Classic MC (helper, used in convergence plots)
- QMC and MC convergence plots
- Scatter plot, a visualization of samples picked by Sobol’s QMC

The estimations are based on the ratio of areas of a circle and a square, where the circle is inscribed in the square. Using the Law of Large Numbers, this ratio can be transformed into the ratio of sampled points: points inside the circle vs points outside. 
Exact methodology, explanation and formulas can be found in the second "readme" file (pdf).

## Usage

Run in your terminal:

```bash
pi_estimate_main.py
```
Input the desired number of samples on which the simulation will run. 
All the graph will appear (scatter plot and three convergence graphs in total)


Install dependencies if needed:

```bash
pip install matplotlib
pip install scikitlearn
```

## Future Work
- explore the differences in convergence rates of QMC and MC more
- explore how Sobol QMC performs vs MC in higher dimensions
- add "live" pi value estimation counter


## License

MIT License

