"""
Oppgave 12
Lag et Python-program som ber brukeren taste inn forventningsverdien λt i en
poissonfordeling samt en øvre grense for den stokastiske variabelen X som sannsynligheten
skal beregnes for. Programmet skal så tegne poisson-fordelingen basert på disse
opplysningene.
Kjør programmet med en del ulike verdier for λt, og legg merke til hvordan
poissonfordelingen begynner å ligne en normalfordeling når verdien til forventningsverdien λt
øker.
"""
from scipy.stats import poisson
import time
import numpy as np
import matplotlib.pyplot as plt

# I did this first. But i want a better way.
def plot_poisson_distribution(lambda_t, upper_limit):
    x = np.arange(0, upper_limit + 1)
    y = poisson.pmf(x, lambda_t)
    plt.bar(x, y, label=f"λt = {lambda_t}")
    plt.title("Poissonfordeling")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
    time.sleep(1)
    plt.close()


# Task 12
#for lambda_t in [1, 5, 10, 20, 50]:
#    plot_poisson_distribution(lambda_t, 100)

def plot_poisson_distribution_interactive(lambda_t, upper_limit):
    plt.ion()
    x = np.arange(0, upper_limit + 1)
    pmf = poisson.pmf(x, lambda_t)

    plt.clf()

    plt.bar(x, pmf, color='lightblue', edgecolor='blue', label=f"λt = {lambda_t}", alpha=0.7)
    plt.plot(x, pmf, color='green', marker='o', linestyle= 'dashed', alpha = 0.5)


    plt.title("Poissonfordeling")
    plt.xlabel("x")
    plt.ylabel("Sannsynlighet P(X=x)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.draw()
    plt.pause(0.1)

def different_lambda_t_values():
    lambda_t_values = [1, 5, 10, 20, 50, 100, 150]
    

    for lambda_t in lambda_t_values:
        plot_poisson_distribution_interactive(lambda_t, lambda_t * 3)
        time.sleep(1)

different_lambda_t_values()



    