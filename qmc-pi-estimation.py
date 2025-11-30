import matplotlib.pyplot as plt
import math
from scipy.stats.qmc import Sobol

# ---------------------------------------

# generating <n> random points in 2x2 square

def generate_points(n_points):

    base = Sobol(d=2, scramble=True)
    samples = base.random(n_points)

    sq_points = [(2*a - 1, 2*b - 1) for a,b in samples]

    return sq_points


# checks how many of those <n> points fall inside the circle inscribed in the square

def points_in_circle(points):

    inside_points = []
    outside_points = []

    for (x,y) in points:
        if x*x + y*y <= 1: # using the equation of a circle
            inside_points.append((x, y))
        else:
            outside_points.append((x, y))

    inside_count = len(inside_points)
    
    return inside_points, outside_points, inside_count

# the actual computation of the estimate

def estimate(points):

    _, _, inside = points_in_circle(points)

    pi = 4 * inside / len(points)

    return pi

# convergence of the estimations

def convergence(points):
    
    estimates = []
    inside = 0

    for i, (x, y) in enumerate(points, start=1):
       
        if x*x + y*y <= 1:
            inside += 1

        pi_estimate = 4 * inside/i
        estimates.append(pi_estimate)
    
    return estimates

# ---------------------------------------

# plotting the random <n> points to visualize the square and the circle 

def plot_points(inside, outside):

    plt.figure(figsize=(6,6))

    if inside:
        x_in, y_in = zip(*inside)
        plt.scatter(x_in, y_in, s=1)
    if outside:
        x_out, y_out = zip(*outside)
        plt.scatter(x_out, y_out, s=1)

    plt.gca().set_aspect("equal")
    plt.title("Monte Carlo π Estimation")
    plt.show()

def both_plots(points):

    inside, outside, _ = points_in_circle(points)
    estimates = convergence(points)

    fig, axs = plt.subplots(1,2, figsize=(12,5))

    # scatter plot
    if inside:
        xs_in, ys_in = zip(*inside)
        axs[0].scatter(xs_in, ys_in, s=2)
    if outside:
        xs_out, ys_out = zip(*outside)
        axs[0].scatter(xs_out, ys_out, s=2)

    axs[0].set_aspect("equal")
    axs[0].set_title("Random Points")

    # convergence plot
    axs[1].plot(estimates)
    axs[1].axhline(math.pi, linestyle="--", color="red")
    axs[1].set_title("Convergence of Monte Carlo π estimation")
    axs[1].set_xlabel("Number of points used")
    axs[1].set_ylabel("Estimate")

    plt.tight_layout()
    plt.show()


# ---------------------------------------

# example usage

if __name__ == "__main":

    n = 850
    number_of_points = generate_points(n)
    both_plots(number_of_points)