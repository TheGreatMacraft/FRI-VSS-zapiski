
def vrstice(ovire):
    return [a for a,b,c in ovire]

def ovirane_vrstice(ovire):
    return sorted(vrstice(ovire))

def ovirane_vrstice_uni(ovire):
    return list(set(ovirane_vrstice(ovire)))

def ovire_v_vrstici(ovire, vrstica):
    return set([(b,c) for a,b,c in ovire if a == vrstica])

def stevilo_ovir(ovire, vrstica):
    return ovire_v_vrstici(ovire,vrstica).__len__()

def dolzina_ovir(ovire):
    return sum([(c-b+1) for a,b,c in ovire])

def prosta_pot(ovire, stolpec):
    return not any(b <= stolpec <= c for a, b, c in ovire)


ovire = [(1, 3, 6),
 (1, 8, 10),
 (2, 1, 4),
 (3, 5, 8),
 (2, 7, 9),
 (7, 10, 10),
 (7, 12, 13),
 (5, 8, 10),
 (5, 1, 3),
 (2, 15, 19)]

print(vrstice(ovire))
print(ovirane_vrstice(ovire))
print(ovirane_vrstice_uni(ovire))
print(ovire_v_vrstici(ovire,2))
print(stevilo_ovir(ovire,2))
print(dolzina_ovir(ovire))
print(prosta_pot(ovire,20))