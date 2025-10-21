import matplotlib.pyplot as plt
from math import *

dolzina = int(input("Vnesi dolzino poti: "))

x = []
y = []

def racunanje_poti(dolzina,st_let = 0,pot_10_let = 0, vsota=0):
    if dolzina <= 0:
        return st_let, pot_10_let
    pot_to_leto = ceil(float(dolzina / 3))
    print(pot_to_leto)
    if st_let < 10:
        pot_10_let += pot_to_leto
    y.append(vsota + pot_to_leto)
    x.append(st_let)
    return racunanje_poti(dolzina - pot_to_leto, st_let+1,pot_10_let,vsota+pot_to_leto)

st_let,pot_10_let = racunanje_poti(dolzina)

"""
while(dolzina > 0):
    pot_to_leto = ceil(float(dolzina / 3))
    if(st_let < 10):
        prvih_10_let += pot_to_leto
    dolzina -= pot_to_leto
    print(pot_to_leto)
    st_let += 1
"""

print(f"Pot bo koncana v {st_let} letih.")
print(f"V prvih 10 letih bo asfaltiranih {pot_10_let} metrov poti")

plt.plot(x,y,marker='o')
plt.ylabel("Leto Gradnje")
plt.xlabel("Pot končana [m]")
plt.title("Del poti, končan vsako leto gradnje")
plt.show()