# importing qmc point generating function, scatter + qmc convergence plots and mc vs qmc comparision plots

from qmc_pi_estimation import generate_points, both_plots
from qmc_vs_mc import compare_mc_qmc

# execution

if __name__ == "__main__":

  n = int(input("Input the number of points you want to run the simulation on "))
  points = generate_points(n)
  both_plots(points)
  compare_mc_qmc(n)


