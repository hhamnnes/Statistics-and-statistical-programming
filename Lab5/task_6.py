

import scipy.stats as stats

class CalcualtePearsonsCorrellationCoeffisient:
    def __init__(self):
        self.x = []
        self.y = []
        self.r = None
        self.p = None
    
    def retrive_data(self):
        try:
            with open(r"C:\Users\hhamn\OneDrive\Dokumenter\GitHub\Statistics-and-statistical-programming\Lab5\katters_vekt.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()

                for line in lines[1:]:
                    if line.strip():
                        parts = line.replace('"', '').split(',')
                        Bwt = float(parts[2])
                        Hwt = float(parts[3])
                        self.x.append(Bwt)
                        self.y.append(Hwt)
                

        
        except FileNotFoundError:
            print("Fant ikke filen")

    def calculate_pearson_correlation_coefficient(self):
        self.r, self.p = stats.pearsonr(self.x, self.y)

        print(self.r)
         
def main():
    calcualte_pearsons_correllation_coeffisient = CalcualtePearsonsCorrellationCoeffisient()
    calcualte_pearsons_correllation_coeffisient.retrive_data()
    calcualte_pearsons_correllation_coeffisient.calculate_pearson_correlation_coefficient()
    

    
if __name__ == "__main__":    
    main()
