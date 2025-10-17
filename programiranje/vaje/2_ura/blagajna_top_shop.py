vsota = 0
while(True):
    cena = float(input("Vnesi ceno: "))
    if(cena == 0):
        break
    vsota += cena
print(f"Vsota: {vsota}")