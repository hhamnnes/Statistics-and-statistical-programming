import scipy.stats as stats
import numpy as np

class HypotheisRightSidedTTest:
    def __init__ (self, significance_level=0.05):
        self.hypotheis_type = "Høyresidg t-test"
        self.hypotheis_text = None
        self.t = None
        self.p = None
        self.my_0 = None
        self.mean = None
        self.sd = None
        self.n = None
        self.cl = None
        self.sl = significance_level
        self.data = []
        
    #a)
    def define_hypotheisis(self):
        self.hypotheis_text = (
            "[Intro] H0: µ <= my_0 (Forventet vekt er uendret, 2.75 kg) \n"
            "[Intro] H1: µ > my_0 (Forventet vekt har økt) \n"
            "[Intro] Bevisbyrden ligger altså hos det å prøve å bevise at kattene har fått økt vekt."
        )

        print("Oppgave a)")
        print(self.hypotheis_text)
        
        try:
            with open(r"C:\Users\hhamn\OneDrive\Dokumenter\GitHub\Statistics-and-statistical-programming\Lab5\katters_vekt.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()

                for line in lines[1:]:
                    if line.strip():
                        parts = line.replace('"', '').split(',')
                        weight = float(parts[2])
                        self.data.append(weight)
                
                self.n = len(self.data)

                self.mean = np.mean(self.data)
                self.sd = np.std(self.data, ddof=1)

                print(f"\n[Info] Data lastet inn. Antall katter (n) = {self.n}")
                print(f"[Info] Gjennomsnittsvekten til kattene i utvalget er: {self.mean:.2f} kg")
                print(f"[Info] Utvalgets standardavvik er: {self.sd:.2f} kg")
        
        except FileNotFoundError:
            print("Fant ikke filen")

    #b)
    def hypothis_test(self):
        # Nå spør vi alltid brukeren siden vi tok vekk track_user
        self.sl = float(input("\nTast inn signifikansnivå (f.eks 0.05): "))
        self.my_0 = float(input("Tast inn forventningsverdien du ønsker å sjekke mot (f.eks 2.75): "))
        
        # Finner t-verdien og p-verdien. 
        res = stats.ttest_1samp(self.data, popmean=self.my_0, alternative='greater')
        self.t = res.statistic
        self.p = res.pvalue
        
        degrees_of_freedom = self.n - 1

        # Samme som når vi sjekker tabell E.5
        self.cl = stats.t.ppf(1 - self.sl, degrees_of_freedom)

        result_text = (
            f"\nResultatet av testen:"
            f"\n Testobservator (T): {self.t:.4f}"
            f"\n Kritisk verdi i t-fordelingen: {self.cl:.4f}"
        )

        print(result_text)

        if self.t > self.cl:
            print(f"Konklusjon: Siden {self.t:.4f} > {self.cl:.4f}, FORKASTER vi H0.")
        else:
            print(f"Konklusjon: Siden {self.t:.4f} <= {self.cl:.4f}, BEHOLDER vi H0.")

    #c)
    def find_p_value(self):
        """Finds the p-value which is an indicator of how likely it is
        to get these observed data or something more extreme given that
        H0 is True"""

        print("\nOppgave c)")
        print(f"Testens p-verdi er: {self.p:.6f}") # La til 'f' foran her

    #d)
    def find_break_point(self):
        print("\nOppgave d)")
        
        break_point = None
        # Rettet np.range til np.arange
        for alfa_test in np.arange(0.1, 0.0001, -0.001):
            self.cl = stats.t.ppf(1-alfa_test, self.n - 1)
            if self.t <= self.cl:
                break_point = alfa_test
                break
        
        if break_point is not None:
            print(f"Grensen (fra forkaste til å beholde) går ved signifikansnivå α ≈ {break_point:.4f} ")

    #e)
    def find_break_point_with_sl(self):
        print("\nOppgave e)")
        self.sl = 0.05
        for test_my in np.arange(2.60, 3, 0.001):
            res = stats.ttest_1samp(self.data, popmean=test_my, alternative='greater')
            p_verdi_test = res.pvalue

            if p_verdi_test > self.sl:
                print(f"Grensa for my_0 der vi går fra å forkaste til å beholde H0 er ved µ ≈ {test_my:.3f} kg")
                break

def main():
    confidence_interval_calculator = HypotheisRightSidedTTest()
    confidence_interval_calculator.define_hypotheisis()

    # Kjører testen én gang (ber om input)
    confidence_interval_calculator.hypothis_test()

    confidence_interval_calculator.find_p_value()
    confidence_interval_calculator.find_break_point()
    confidence_interval_calculator.find_break_point_with_sl()

if __name__ == "__main__":    
    main()