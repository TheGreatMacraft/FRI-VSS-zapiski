vsota = 0
st = 0
while(True):
    cena = float(input("Vnesi ceno: "))
    if(cena == 0):
        break
    st += 1
    vsota += cena
print(f"Vsota: {vsota}")
print(f"Povprecna cena: {float(vsota/st)}")