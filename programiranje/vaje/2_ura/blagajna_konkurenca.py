st_izd = int(input("Vnesi število izdelkov: "))

vsota = 0
stevec = 1
while(stevec <= st_izd):
    vsota += float(input(f"Vnesi ceno artikla {stevec}:"))
    stevec += 1

print(f"Vsota: {vsota}")