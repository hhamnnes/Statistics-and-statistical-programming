import scipy.stats as stats

t_value = 3.5358
df = 9

p_value = 1 - stats.t.cdf(t_value, df)

print(f"P-value equals: {p_value:.5f}")