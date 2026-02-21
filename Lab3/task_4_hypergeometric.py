from scipy.stats import hypergeom, binom
import matplotlib.pyplot as plt

def hypergeometric_distribution(N, M, n, label):
    # N: totalt population size
    # M: number of units with a certain characteristic
    # n: number of draws
    # lablel: label for the plot

    #Hypergeometric distribution: X ~ Hypergeometric(N, M, n)
    hg = hypergeom(N, M, n)
    
    #Bionomial distribution: X ~ Binomial(n, p)
    p = M / N  # probability of success in each draw
    bi = binom(n, p)

    # P(X = 3) for Hypergeometric distribution
    p_eq3_hg = hg.pmf(3)
    p_le3_hg = hg.cdf(3)

    p_eq3_bn = bi.pmf(3)
    p_le3_bn = bi.cdf(3)

    print(f"=== {label} ===")
    print(f"N={N}, K={M}, n={n}, p=K/N={p:.6f}")
    print("Hypergeometric:")
    print(f"  P(=3)  = {p_eq3_hg:.10f}")
    print(f"  P(<=3) = {p_le3_hg:.10f}")
    print("Binomial:")
    print(f"  P(=3)  = {p_eq3_bn:.10f}")
    print(f"  P(<=3) = {p_le3_bn:.10f}")
    print()

# a) and b)
hypergeometric_distribution(N=64, M=14, n=8, label="Case 1 (64 mouse, 14 marked, 8 shot down)")

# c) and d)
hypergeometric_distribution(N=640, M=140, n=8, label="Case 2 (640 mouse, 140 marked, 8 shot down)")

# e) comparison between (a), b) and (c), d)
plt.figure(figsize=(12, 6))
x = range(0, 9)  # possible values of X (number of marked mice shot down)
p_hg_case1 = hypergeom.pmf(x, 64, 14, 8)
p_hg_case2 = hypergeom.pmf(x, 640, 140, 8)
p_bn_case1 = binom.pmf(x, 8, 14/64)
p_bn_case2 = binom.pmf(x, 8, 140/640)
plt.plot(x, p_hg_case1, label="Hypergeometric Case 1", marker='o')
plt.plot(x, p_hg_case2, label="Hypergeometric Case 2", marker='o')
plt.plot(x, p_bn_case1, label="Binomial Case 1", marker='x')
plt.plot(x, p_bn_case2, label="Binomial Case 2", marker='x')
plt.title("Probability Mass Function for Hypergeometric and Binomial Distributions")
plt.xlabel("Number of marked mose shot down (X)")
plt.ylabel("Probability")
plt.legend()
plt.grid()
plt.show()

# Histogram for F(X) - Cumulative Distribution Function
plt.figure(figsize=(12, 6))
x = range(0, 9)
cdf_hg_case1 = hypergeom.cdf(x, 64, 14, 8)
cdf_hg_case2 = hypergeom.cdf(x, 640, 140, 8)
cdf_bn_case1 = binom.cdf(x, 8, 14/64)
cdf_bn_case2 = binom.cdf(x, 8, 140/640)
plt.plot(x, cdf_hg_case1, label="Hypergeometric Case 1", marker='o')
plt.plot(x, cdf_hg_case2, label="Hypergeometric Case 2", marker='o')
plt.plot(x, cdf_bn_case1, label="Binomial Case 1", marker='x')
plt.plot(x, cdf_bn_case2, label="Binomial Case 2", marker='x')
plt.title("Cumulative Distribution Function for Hypergeometric and Binomial Distributions")
plt.xlabel("Number of marked mice shot down (X)")
plt.ylabel("Cumulative Probability F(X)")
plt.legend()
plt.grid()
plt.show()





