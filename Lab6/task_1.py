import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats as st


class Task_1:
    def __init__(self):
        self.data = None
        self.bwt = None
        self.hwt = None
        self.x = []
        self.y = []
        self.lines = None
        self.standard_deviation = None
        self.regl_line = None
        self.point_of_intersectioin = None
        self.slope = None

    def retrive_data(self):
        try:
            with open(r"Lab6\katters_vekt.csv",
                      "r", encoding="utf-8") as file:
                self.lines = file.readlines()

                for line in self.lines[1:]:
                    if line.strip():
                        parts = line.replace('"', '').split(',')
                        self.bwt = float(parts[2])
                        self.hwt = float(parts[3])
                        self.x.append(self.bwt)
                        self.y.append(self.hwt)
                        
        except FileNotFoundError:
            print("Did not find the file")

    def print_values(self):
        for i in self.x:
            print(i)
        
        for i in self.y:
            print(i)

    def plot_data(self):
        plt.scatter(self.x, self.y, label='Cats')

        corelation = self.regl_line.rvalue
        y_line = [(self.point_of_intersectioin + self.slope * xi) for xi in self.x]
        plt.plot(self.x, y_line, color='red', label=f'Regline (r = {corelation:.3f})')

        plt.xlabel('Body weight in Kg')
        plt.ylabel('Heart weight in g')

        plt.legend()
        

    def find_regline(self):
        self.regl_line = st.linregress(self.x, self.y)
        self.standard_deviation = self.regl_line.stderr
        self.point_of_intersectioin = self.regl_line.intercept
        self.slope = self.regl_line.slope

        print(f"Standard deviation of the regression line is: {self.standard_deviation:.5f}")

        print("The regline is:")
        print(f"Y = {self.point_of_intersectioin} + {self.slope}x")
    
    def find_confidence_interval(self):
        cat_weight = float(input("Enter the cat weight in kilograms: "))

        #Y=α+βx
        point_estimate = self.point_of_intersectioin + self.slope*cat_weight

        #y^​0​±tα/2,n−2​⋅s⋅n1​+∑(xi​−xˉ)2(x0​−xˉ)2​​ 

        #Steg 1: Grunnleggende verdier (n og xˉ)
        n = len(self.x)
        x_mean = sum(self.x) / n

        #Steg 2: Summen av kvadratavvikene for x (∑(xi​−xˉ)2)
        sxx = sum([(xi - x_mean)**2 for xi in self.x])
        se_beta = self.regl_line.stderr

        #Steg 3: Steg 3: Residualstandardavviket (s)
        s = self.regl_line.stderr * math.sqrt(sxx)

        #Steg 4: t-verdien (tα/2,n−2​)
        t_value = st.t.ppf(0.975, n-2)

        #Steg 5: Regne ut hele feilmarginen og intervallet!
        margin_of_error = t_value * s * math.sqrt((1/n) + ((cat_weight-x_mean)/(s/se_beta))**2)
        lower_bound = point_estimate - margin_of_error
        upper_bound = point_estimate + margin_of_error

        print(f"95% Konfidensintervall for hjertevekt ved {cat_weight} kg:")
        print(f"[{lower_bound:.1f}, {upper_bound:.1f}] gram")
    
    def find_prediction_interval(self):
        print("\n--- Oppgave 1e: Prediksjonsintervall ---")
        cat_weight = float(input("Enter the cat weight in kilograms: "))

        # Y = α + βx (Punktestimatet er nøyaktig det samme)
        point_estimate = self.point_of_intersectioin + self.slope * cat_weight

        # Steg 1: Grunnleggende verdier
        n = len(self.x)
        x_mean = sum(self.x) / n

        # Steg 2: Summen av kvadratavvikene for x
        sxx = sum([(xi - x_mean)**2 for xi in self.x])
        se_beta = self.regl_line.stderr

        # Steg 3: Residualstandardavviket (s)
        s = self.regl_line.stderr * math.sqrt(sxx)

        # Steg 4: t-verdien
        """ Ok, skjønner. Tja jeg skjønte ikke helt hvor vi fikk tallet 0.975 fra når vi skulle regne ut t-verdien i sta

            Det er et utrolig godt og veldig vanlig spørsmål! Det er en av de tingene som kan virke litt som "magi" i statistikk helt til man tegner det opp.

            For å forstå hvor 0.975 kommer fra, må vi se på hvordan Python (og statistikk generelt) tenker på en fordeling (den berømte "bjellekurven").

            Når vi ber om et 95% konfidensintervall, skjer følgende regnestykke i bakgrunnen:

            Målet vårt: Vi vil fange opp de 95% mest sannsynlige utfallene i midten av kurven.

            Resten (kalt α): Siden hele kurven er 100%, betyr det at vi har 5% "usikkerhet" til overs (100%−95%=5%). I desimaltall er dette α=0.05.

            To haler: Et intervall har alltid to grenser (en nedre og en øvre). Vi kan bomme ved at verdien er for lav, eller vi kan bomme ved at den er for høy. Derfor må vi dele de 5% med usikkerhet likt på begge sider av kurven.

                    5%/2=2.5% usikkerhet på venstre side.

                    5%/2=2.5% usikkerhet på høyre side.

                Hvordan Python tenker: Funksjonen du brukte, st.t.ppf(), er programmert til å alltid regne fra venstre mot høyre. Den spør deg egentlig: "Hvor stort areal av hele kurven ligger til venstre for det punktet du prøver å finne?"

            For å finne den øvre t-verdien, må Python gå forbi hele den venstre halen på 2.5%, pluss hele midtpartiet på 95%.
            2.5%+95%=97.5%

            Gjør vi 97.5% om til desimaltall (deler på 100), får vi nøyaktig 0.975!"""
        t_value = st.t.ppf(0.975, n-2)

        # Steg 5: Regne ut feilmargin med ekstra usikkerhet (1 + ...)
        margin_of_error = t_value * s * math.sqrt(1 + (1/n) + ((cat_weight-x_mean)/(s/se_beta))**2)
        
        lower_bound = point_estimate - margin_of_error
        upper_bound = point_estimate + margin_of_error

        print(f"95% Prediksjonsintervall for hjertevekt til én katt på {cat_weight} kg:")
        print(f"[{lower_bound:.1f}, {upper_bound:.1f}] gram")














        


def main():
    task_1 = Task_1()
    task_1.retrive_data()
    #task_1.print_values()
    task_1.find_regline()
    task_1.plot_data()
    plt.show()
    task_1.find_confidence_interval()
    task_1.find_prediction_interval()

if __name__ == "__main__":
    main()

    
        

