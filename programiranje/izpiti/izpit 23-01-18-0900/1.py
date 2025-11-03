def skupne_povezave(pot1,pot2):
    st = 0
    krajsi = pot1 if pot1 < pot2 else pot2
    for i in range(len(krajsi)):
        if(pot1[i:i+2]==pot2[i:i+2]):
            st += 1
    return st

print(skupne_povezave("ASAIMWGVIEMHEUTUMVIVHIV","OIMIMAWAREMMPBTUMGIBTIOWE"))