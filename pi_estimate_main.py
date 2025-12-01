from qmc-pi-estimation import generate_points, both_plots
from qmc_vs_mc import compare_mc_qmc

n = 850
points = generate_points(n)
both_plots(points)
compare_mc_qmc(points)
