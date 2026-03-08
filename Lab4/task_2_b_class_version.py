"""Lag et Python-program som simulerer flere omganger med terningkast.
Programmet skal be brukeren taste inn hvor mange terningkast som skal gjøres i hver
omgang og hvor mange omganger som skal gjøres.
Programmet skal så simulere disse terningkastene og summere hvor mange øyne
terningen viser i hver omgang, og skal også regne ut gjennomsnittet av antall øyne i
hver omgang.
Programmet skal så tegne et histogram med 30 søyler som viser disse
gjennomsnittene.
Kjør programmet med en del ulike tall, både små tall, store tall og veldig store tall.
Tips:
For å generere tilfeldige heltall mellom 1 og 6, kan man bruke
random.randint(1,6)
men da må man først importere pakken random fra Pythons standardbibliotek ved å
skrive import random
Når man skal holde styr på totalt antall øyne i de ulike omgangene, kan man for
eksempel definere et array med N elementer initialisert med bare 0-er ved hjelp av
numpy.zeros(N)"""

# I have decided to make a class version of this program. I will do this to make it 
# easier to extend. 

import random
import numpy as np
import matplotlib.pyplot as plt


class DiceSimulation:
    def __init__ (self, num_throws, number_of_rounds):
        self.num_throws = num_throws
        self.number_of_rounds = number_of_rounds
        self._total_number_of_eyes = np.zeros(number_of_rounds)
        self._average_number_of_eyes = np.zeros(number_of_rounds)    

    @property
    def total_number_of_eyes(self):
        return self._total_number_of_eyes
    
    @property
    def average_number_of_eyes(self):
        return self._average_number_of_eyes
    
    def run(self) -> None:
        for round in range(self.number_of_rounds):
            for throw in range(self.num_throws):
                self._total_number_of_eyes[round] += random.randint(1, 6)
            self._average_number_of_eyes[round] = self._total_number_of_eyes[round] / self.num_throws
    
    def plot_histogram(self) -> None:
        # Plotting the histogram:
        plt.hist(self.average_number_of_eyes, bins=30, edgecolor='black')

        # Lables and title:
        plt.title("Histogram of Average Number of Eyes per Round")
        plt.xlabel("Average Number of Eyes")
        plt.ylabel("Frequency")

        # Grid for better visibility:
        plt.grid(axis='y', alpha=0.75)

        # Show the plot:
        plt.show()

def main() -> None:
    num_throws = int(input("Enter the number of dice throws per round: "))
    number_of_rounds = int(input("Enter the number of rounds: "))

    simulator = DiceSimulation(num_throws, number_of_rounds)
    simulator.run()


    print(f"Average number of eyes per round: {simulator.average_number_of_eyes}")
    print(f"Total number of eyes per round: {simulator.total_number_of_eyes}")
    simulator.plot_histogram()

if __name__ == "__main__":
    main()