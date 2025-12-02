from qmc_pi_estimation import generate_points, both_plots
from qmc_vs_mc import compare_mc_qmc

# execution

n = 1024
points = generate_points(n)
both_plots(points)
compare_mc_qmc(n)
