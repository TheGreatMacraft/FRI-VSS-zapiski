'''
Napiši program za izračun dolžine strela s topom
(ki brez trenja izstreljuje točkaste krogle v brezzračnem prostoru nad Zemljo, ki ni okrogla, a pustimo trivialne predpostavke).
Program od uporabnika ali uporabnice zahteva, da mu ta vpiše hitrost izstrelka in kot, pod katerim je izstreljena (krogla, ne uporabnica)
Program izračuna in izpiše, kako daleč bo letela krogla.
'''

from math import *

hitrost = float(input("Vnesi hitrost: "))
kot = float(input("Vnesi kot: "))

kot *= pi / 180

print ((hitrost**2 * sin(2*kot))/9.807)