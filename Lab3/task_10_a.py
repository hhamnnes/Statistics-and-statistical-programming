"""
Oppgave 10
a) Lag et Python-program som tegner normalfordelingen som benyttes i oppgave 9, altså
N(760, 10). Tegn fordelingen for verdier mellom 720 og 800.
Angi «Normalfordeling» som tittel på plottet, og med angivelse av x og f(x) på
aksene, altså omtrent som dette:
"""

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

