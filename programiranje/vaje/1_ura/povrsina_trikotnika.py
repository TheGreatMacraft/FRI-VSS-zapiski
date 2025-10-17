from math import *

a = float(input("Dolžina stranice a: "))
b = float(input("Dolžina stranice b: "))
c = float(input("Dolžina stranice c: "))

s = (a+b+c)/2
P = sqrt(s*(s-a)*(s-b)*(s-c))

print(f"Površina trikotnika: {float(P)}")
print(f"Površina včrtanega kroga: {float(pi*((P/s)**2))}")
print(f"Površina očrtanega kroga: {float(pi*(((a*b*c)/(4*P))**2))}")