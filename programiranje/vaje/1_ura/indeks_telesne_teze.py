from math import *

h = float(input("Višina [cm]: "))
m = float(input("Masa [kg]: "))
print(f"BMI je {float(m/((h/100)**2))}")
