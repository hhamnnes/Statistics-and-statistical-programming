import pandas as pd
import matplotlib.pyplot as plt
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
            with open(r"C:\Users\hhamn\OneDrive\Dokumenter\GitHub\Statistics-and-statistical-programming\Lab6\katters_vekt.csv",
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
        plt.scatter(self.x, self.y)
        

    def find_regline(self):
        self.regl_line = st.linregress(self.x, self.y)
        self.standard_deviation = self.regl_line.stderr
        self.point_of_intersectioin = self.regl_line.intercept
        self.slope = self.regl_line.slope

        print(f"Standard deviation of the regression line is: {self.standard_deviation:.5f}")

        print("The regline is:")
        print(f"Y = {self.point_of_intersectioin} + {self.slope}x")
        


def main():
    task_1 = Task_1()
    task_1.retrive_data()
    #task_1.print_values()
    task_1.plot_data()
    task_1.find_regline()
    plt.show()

if __name__ == "__main__":
    main()

    
        

