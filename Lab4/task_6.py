
"""Oppgave 6
Denne oppgaven skal løses ved hjelp av Python.
Lag et Python-program som beregner et konfidensintervall for sannsynligheten p i en
binomisk fordeling. Programmet skal fungere slik:
Programmet skal be brukeren taste inn utvalgets størrelse og andelen av utvalget som er i
favør av det man skal sjekke. (Hvis du skulle brukt dette programmet på forrige oppgave, ville
disse tallene altså vært henholdsvis 600 og 60). Programmet skal også be brukeren angi
konfidensintervallet i prosent.
Basert på disse tallene som brukeren har tastet inn, skal programmet sjekke om tallene
oppfyller kravene til en tilnærmet normalfordeling (se regel 6.12 side 252 i boka), og skrive ut
en beskjed om resultatet av denne sjekken.
Uansett om tilnærmingen er god eller ikke, skal programmet regne ut et konfidensintervall for
p og skrive ut dette med en passende ledetekst.
Sjekk at programmet virker som det skal ved å kjøre det med de tallene du fant i forrige
oppgave."""

import numpy as np 
import matplotlib.pyplot as plt
from fractions import Fraction

class ConfidenceIntervalOfLikelyhood():
    def __init__ (self):
        self.sample_size = None
        self.proportion_in_favor = None
        self.confidence_level = None
        self.left_bound = None
        self.right_bound = None
        self.z_table = {
            0.1: 1.282,
            0.05: 1.645,
            0.025: 1.96,
            0.01: 2.326,
            0.005: 2.576,
            0.001: 3.291
        }

    def get_data(self):
        self.sample_size = int(input("Enter the sample size(n): "))
        self.proportion_in_favor = input("Enter the proportion in favor: ")
        try:
            self.proportion_in_favor = float(self.proportion_in_favor)
        except ValueError:
            self.proportion_in_favor = float(Fraction(self.proportion_in_favor))
        
        self.confidence_level = input("Enter the confidence level in percentage:")
        try:
            self.confidence_level = float(self.confidence_level)
            if self.confidence_level > 1:
                self.confidence_level = self.confidence_level / 100

        except ValueError:
            self.confidence_level = float(Fraction(self.confidence_level))
            if self.confidence_level > 1:
                self.confidence_level = self.confidence_level / 100

        try:
            self.check_normal_prerequisites()

        except ValueError as e:
            print(e)

        self.left_bound, self.right_bound = self.calculate_confidence_interval()
        print(f"The confidence interval for the likelyhood is: [{self.left_bound:.4f}, {self.right_bound:.4f}]")


    def check_normal_prerequisites(self):
        n = self.sample_size
        p = self.proportion_in_favor
        if n * p * (1 - p) < 5:
            raise ValueError("The normal approximation is not valid for these parameters. \
                             The product n*p(1-p) must be at least 5, is currently: " + str(n * p * (1 - p)))
        
    def calculate_confidence_interval(self):
        p = self.proportion_in_favor
        n = self.sample_size
        confidence_level = self.confidence_level
        alpha = 1 - confidence_level
        alpha = round(alpha, 4)

        print("Alpha is :", alpha)
        z = self.z_table.get(alpha / 2)

        print("Z is :", z )

        if z is None:
            raise ValueError("Confidence level not supported. Please choose from the following: 90%, 95%, 97.5%, 99%, 99.5%, 99.9%")
        
        right_bound = p + z * np.sqrt(p*(1-p)/n)
        left_bound = p - z * np.sqrt(p*(1-p)/n)

        return left_bound, right_bound
    
def main():
    confidence_interval_calculator = ConfidenceIntervalOfLikelyhood()
    confidence_interval_calculator.get_data()

if __name__ == "__main__":    
    main()




        
        

        
