"""
Statistikk og statistisk programmering, oving 4 Side 2
b) Lag et Python-program som simulerer flere omganger med terningkast.
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

import random
import numpy as np
import matplotlib.pyplot as plt

def throw_dice(num_throws, number_of_rounds):
    total_number_of_eyes = np.zeros(number_of_rounds)
    average_number_of_eyes = np.zeros(number_of_rounds)
    for round in range(number_of_rounds):
        for throw in range(num_throws):
            total_number_of_eyes[round] += random.randint(1, 6)
        average_number_of_eyes[round] = total_number_of_eyes[round] / num_throws

    return average_number_of_eyes, total_number_of_eyes

def plot_30_bars_histogram(average_number_of_eyes):

    # Plotting the histogram:
    plt.hist(average_number_of_eyes, bins=30, edgecolor='black')

    # Lables and title:
    plt.title("Histogram of Average Number of Eyes per Round")
    plt.xlabel("Average Number of Eyes")
    plt.ylabel("Frequency")

    # Grid for better visibility:
    plt.grid(axis='y', alpha=0.75)

    # Show the plot:
    plt.show()

def main():
    num_throws = int(input("Enter the number of dice throws per round: "))
    number_of_rounds = int(input("Enter the number of rounds: "))
    average_number_of_eyes, total_number_of_eyes = throw_dice(num_throws, number_of_rounds)
    print(f"Average number of eyes per round: {average_number_of_eyes}")
    print(f"Total number of eyes per round: {total_number_of_eyes}")
    plot_30_bars_histogram(average_number_of_eyes)


main()