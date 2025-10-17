from time import *
from random import *

a = float(input("Vnesi prvo stevilo: "))
b = float(input("Vnesi drugo stevilo: "))

sleep(randint(0,round((a*b)/10)))

print(a*b)