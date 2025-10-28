def skupne_povezave(pot1,pot2):
    a = list(pot1)
    b = list(pot2)
    rezultat = []

    for i in range(0,len(a)):
        if(a[i] == b[i]):
            j = i
            tmp = []
            while j < range(0,len(a)):
                if(a[j] != b[j]):
                    i = j
                    break
                tmp.append(a[j])
            if(len(tmp) > 1):
                rezultat.append(tmp)
    return rezultat
print(skupne_povezave("ASAIMWGVIEMHEUTUMVIVHIV"," OIMIMAWAREMMPBTUMGIBTIOWE"))