def capitalise(imena):
    return [el.replace(el[0],el[0].upper()) for el in imena]
def icapitalise(imena):
    imena [:]=capitalise(imena)
def zamenjano(s, menjave):
    return [menjave[el] if (el in menjave) else el for el in s]
def zamenjaj(s, menjave):
    s [:]=zamenjano(s,menjave)
def alterniraj(seznam):
    seznam[:]= [seznam[0]] + [el for i,el in enumerate(seznam) if (abs(el+seznam[i-1]) < abs(el) + abs(seznam[i-1]))]
def dodaj_isti(s):
    s.extend(s[:])
def dodaj_enaki(s):
    s.extend(list(el) for el in s[:])
def poenoti(s):
    for i,tmp in enumerate(s):
        for j,el in enumerate(s[i:]):
            if tmp == el:
                s[i+j] = tmp
def razenoti(s):
    for i,tmp in enumerate(s):
        for j,el in enumerate(s[i:]):
            if tmp == el:
                s[i+j] = list(tmp)
