"""
Oppgave 7
Denne oppgaven skal løses ved hjelp av Python.
Lag et Python-program som beregner et punktestimat og et konfidensintervall for
standardavviket σ til målinger som er hentet fra en normalfordeling.
Målingene kan du legge i en kommaseparert fil som leses inn av programmet.
Programmet skal be brukeren taste inn et konfidensintervall i prosent.
Basert på dette skal programmet regne ut et punktestimat og et konfidensintervall for σ, og
skrive disse ut avrundet til én desimal og med passende ledetekster.
Som en test for å sjekke at programmet virker som det skal, kan du bruke data som er gitt i
eksempel 6.10 på side 250 i læreboka om antall tilfeller av salmonella i Norge i perioden
2002–2010. Disse er:
1495, 1537, 1545, 1488, 1805, 1649, 1942, 1234, 1367
Korrekte svar for disse er:
Punktestimat for standardavvik: 214.3
90 % konfidensintervall: [153.9, 366.7]
95 % konfidensintervall: [144.8, 410.6]
99 % konfidensintervall: [129.4, 522.8]
Bruk til slutt programmet til å beregne et 92 % konfidensintervall for standardavviket til antall
salmonellatilfeller, og legg ved resultatet du finner.
"""

import numpy as np
import scipy.stats as st

class PointEstimateAndConfidenceInterval:
    def __init__ (self, data_file_path, confidence_level):
        if data_file_path:
            self.data = np.genfromtxt(data_file_path, delimiter=',')
        else:
            self.data = np.array([1495, 1537, 1545, 1488, 1805, 1649, 1942, 1234, 1367])

        self.confidence_level = confidence_level
        self.aprox_average = self.aproximation_of_average()
        self.delta_degrees_of_freedom = np.size(self.data) - 1
        self.standard_deviation = self.calculate_sample_standard_devation()
        self.confidence_interval = self.calculate_confidence_interval()

    def aproximation_of_average(self):
        sum = 0
        for element in self.data:
            sum += element

        return sum / np.size(self.data)

    def calculate_sample_standard_devation(self):
        sigma = 0
        for element in self.data:
            sigma += (element - self.aprox_average)**2

        s = np.sqrt(sigma / self.delta_degrees_of_freedom)

        return s

    def calculate_confidence_interval(self):
        alpha = 1 - (self.confidence_level / 100.0)
        
    
        chi2_lower = st.chi2.ppf(1 - alpha / 2, self.delta_degrees_of_freedom )
        chi2_upper = st.chi2.ppf(alpha / 2, self.delta_degrees_of_freedom )

        variance = self.standard_deviation**2
        lower_bound = np.sqrt((self.delta_degrees_of_freedom * variance) / chi2_lower)
        upper_bound = np.sqrt((self.delta_degrees_of_freedom  * variance) / chi2_upper)
        
        return [lower_bound, upper_bound]
    
if __name__ == "__main__":
    try:
        user_input = input("Enter a confidence interval in percent (e.g., 90, 95, 99, or 92): ")
        confidence_pct = float(user_input)
        
        calc = PointEstimateAndConfidenceInterval(None, confidence_pct)
        
        print(f"\nPoint estimate for standard deviation: {calc.standard_deviation:.1f}")
        print(f"{confidence_pct:g} % confidence interval: [{calc.confidence_interval[0]:.1f}, {calc.confidence_interval[1]:.1f}]")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")