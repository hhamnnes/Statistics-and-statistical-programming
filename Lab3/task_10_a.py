from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def normalized_distribution(mu, sigma, start, stop, label):
    x = np.linspace(start, stop, 1000)
    y = norm.pdf(x, mu, sigma)
    plt.plot(x, y, label=label)
    plt.title("Normalfordeling")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

# Task a)
normalized_distribution(760, 10, 720, 800, "a) μ=760, σ=10")

