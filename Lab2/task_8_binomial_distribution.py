import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
from scipy.stats import binom as bi

n = int(input("Tast inn antall forsøk: "))
san = input("Tast inn sannsynligheten: ")

#I like to have the possibility to write the probability in a fraction:
try:
    p = float(san)
except:
    p = float(Fraction(san))


x = np.arange(n+1)

pmf = bi.pmf(x, n, p)
cdf = bi.cdf(x, n, p)

plt.figure()
plt.plot(x, pmf, label="Punktsannsynlighet")
plt.plot(x, cdf, label="Fordelingsfunksjonen")

plt.title(f"Binomisk fordeling for verdiene n={n} og p={p}")
plt.xlabel("Punkt P(X=x)")
plt.ylabel("Sannsynlighet")
plt.legend()
plt.grid(True)

plt.show()