import matplotlib.pyplot as plt
import math
import random
from scipy.stats.qmc import Sobol

# -------------------------------------------------
# Reusing the convergence function for clearer code (could have imported it)
def convergence(points):
    estimates = []
    inside = 0
    for i, (x, y) in enumerate(points, start=1):
        if x*x + y*y <= 1:
            inside += 1
        estimates.append(4 * inside / i)
    return estimates

# -------------------------------------------------
# normal monte carlo point generator (random)
def generate_random_points(n_points):
    return [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n_points)]

# qmc point generator

def generate_sobol_points(n_points):

    base = Sobol(d=2, scramble=True)
    samples = base.random(n_points)

    sq_points = [(2*a - 1, 2*b - 1) for a,b in samples]

    return sq_points

# -------------------------------------------------

# comparision plots

def compare_mc_qmc(n_points):
    # Generate points for mc and qmc
    mc_points = generate_random_points(n_points)
    qmc_points = generate_sobol_points(n_points)

    # convergences of estimates for mc and qmcc
    mc_estimates = convergence(mc_points)
    qmc_estimates = convergence(qmc_points)

    fig, axs = plt.subplots(1,2, figsize=(12,5))

    # mc
    
    axs[0].plot(range(1, n_points+1), mc_estimates, label="MC")
    axs[0].axhline(math.pi, color="black", linestyle="--", label="π")
    axs[0].set_title("Monte Carlo Convergence")
    axs[0].set_xlabel("Number of points")
    axs[0].set_ylabel("π estimate")
    

    # qmc
    
    axs[1].plot(range(1, n_points+1), qmc_estimates, label="QMC (Sobol)")
    axs[1].axhline(math.pi, color="black", linestyle="--", label="π")
    axs[1].set_title("Quasi-Monte Carlo Convergence (Sobol)")
    axs[1].set_xlabel("Number of points")
    axs[1].set_ylabel("π estimate")
    
    plt.tight_layout()
    plt.show()

# --------------------------------

# execution

if __name__ == "__main__":
   n = 850
   compare_mc_qmc(n)

