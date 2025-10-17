vsota = 0
stevec = 0
while (vsota < 100 and stevec < 10):
    cena = float(input("Vnesi ceno izdelka: "))
    if(cena == 0):
        break
    vsota += cena
    stevec += 1

print(f"Porabili boste {vsota} evrov, za {stevec} stvari.")