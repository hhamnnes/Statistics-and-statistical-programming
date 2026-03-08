"""Utvid programmet i spørsmål b slik at det tar alle gjennomsnittene som du beregner,
og finner og skriver ut gjennomsnittet av disse og utvalgsstandardavviket for disse.
Legg merke til at utvalgsstandardavviket som beregnes av programmet blir i nærheten
av 𝝈
√𝒏 hvor 𝝈 er standardavviket du fant i spørsmål a, og n er antall kast i hver
omgang."""

import random
import numpy as np 
import matplotlib.pyplot as plt
from task_2_b_class_version import DiceSimulation

class TotalAverageAndStdDev(DiceSimulation):
    def __init__(self, num_throws, number_of_rounds):
        super().__init__(num_throws, number_of_rounds)
        self.run()  # Kjør simuleringen først
        self._total_average = self.calculate_total_average()
        self._std_dev = self.calculate_std_dev()
        self._variance = 0.0
    
    @property
    def total_average(self):
        return self._total_average
    
    @property
    def std_dev(self):
        return self._std_dev

    # Calculate μ^​ = (1/n) * Σ(X_i) = (1/n) * (X1 + X2 + ... + Xn)
    def calculate_total_average(self) -> float:
        self._total_average = 0.0
        for average in self.average_number_of_eyes:
            self._total_average += average
        self._total_average /= self.number_of_rounds
        return self._total_average
    
    # Calculate sample standard deviation s = sqrt((1/(n-1)) * Σ(X_i - μ^​)^2)
    def calculate_std_dev(self) -> float:
        self._variance = 0.0
        for average in self.average_number_of_eyes:
            self._variance += (average - self.total_average) ** 2
        self._variance /= (self.number_of_rounds - 1)
        self._std_dev = np.sqrt(self._variance)
        return self._std_dev


def main() -> None:
    num_throws = int(input("Enter the number of dice throws per round: "))
    number_of_rounds = int(input("Enter the number of rounds: "))
    
    simulator = TotalAverageAndStdDev(num_throws, number_of_rounds)
    
    print(f"Total average: {simulator.total_average:.4f}")
    print(f"Standard deviation: {simulator.std_dev:.4f}")
    
    simulator.plot_histogram()


if __name__ == "__main__":
    main()


        
        