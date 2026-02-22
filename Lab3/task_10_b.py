from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def likelihood_for_higher_weight(weight):
    mu = 760
    sigma = 10
    likelihood = 1 - norm.cdf(weight, mu, sigma)
    #P(X > weight) = 1 - P(X <= weight) = 1 - CDF(weight) 
    # = 1 F(weight)
    return likelihood

# Task b)
weight = float(input("Enter a weight in grams: "))

likelihood = likelihood_for_higher_weight(weight)
print(f"The likelihood of a weight being higher than {weight} grams is {likelihood:.4f}")
print(f"Or {likelihood * 100:.2f}%")