
"""Oppgave 3
Denne oppgaven skal løses ved hjelp av Python.
På den greske øya Kripos kryr det av villkatter.
Myndighetene har plukket ut noen katter som de av ulike grunner har undersøkt, og blant
annet funnet vekten av kattene og vekten av deres hjerter. Resultatet av målingene finner du i
følgende fil:
https://it.hiof.no/statok/katters_vekt.csv
De fire feltene i filen er: løpenummer, kjønn, kattens vekt i kg og hjertets vekt i gram (dette er
altså en fil jeg har funnet på nettet med faktiske målinger av vekten til katter – ikke tenk for
mye på hvordan de har klart å veie hjertet …).
Vi ønsker å sjekke om det er rimelig å anta at vekten av kattene og vekten av deres hjerter
begge er normalfordelte.
Statistikk og statistisk programmering, oving 4 Side 3
Lag et Python-program som leser inn data fra fila og lager et normaltestplott (QQ-plott) først
for kattenes vekt og så for hjertenes vekt.
Tips:
For å lese inn data fra fil, kan man bruke numpy.genfromtxt.
For å lage et normaltestplott kan man gjøre følgende import:
from statsmodels.graphics.gofplots import qqplot
og så bruke qqplot på sine data."""

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm

class NormalityTest:
    def __init__ (self, file_path):
        self.file_path = file_path
        self.cat_gender = np.array([])
        self.cat_weights = np.array([])
        self.heart_weights = np.array([])
    
    def read_data(self) -> None:
        data = np.genfromtxt(self.file_path, delimiter=',', skip_header=1)
        self.cat_gender = data[:, 1]
        self.cat_weights = data[:, 2]
        self.heart_weights = data[:, 3]
    
    def plot_qq_plots(self) -> None:
        # Plotting the QQ-plot for cat weights:
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        qqplot(self.cat_weights, line='s', ax=plt.gca())
        plt.title("QQ-plot for Cat Weights")

        #Plotting the QQ-plot for heart weights:
        plt.subplot(1, 2, 2)
        qqplot(self.heart_weights, line='s', ax=plt.gca())
        plt.title("QQ-plot for Heart Weights")
        plt.tight_layout()
        plt.show()

    # I have added this just to compare the histograms with the QQ-plots.
    def plot_histograms(self) -> None:

        # Plotting the histogram for cat weights:
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.hist(self.cat_weights, bins=30, edgecolor='black')
        plt.title("Histogram of Cat Weights")
        plt.xlabel("Weight (kg)")
        plt.ylabel("Frequency")

        # Plotting the histogram for heart weights:
        plt.subplot(1, 2, 2)
        plt.hist(self.heart_weights, bins=30, edgecolor='black')
        plt.title("Histogram of Heart Weights")
        plt.xlabel("Weight (g)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

def main() -> None:
    file_path = "https://it.hiof.no/statok/katters_vekt.csv"

    #I have also testet with a dataset that is not nomal distributed, just to see the difference:
    #file_path = r"C:\Users\hhamn\Downloads\skjeve_kattevekter.csv"
    
    normality_test = NormalityTest(file_path)
    normality_test.read_data()
    normality_test.plot_qq_plots()
    normality_test.plot_histograms()

if __name__ == "__main__":
    main()
