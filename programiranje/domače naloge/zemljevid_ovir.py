from itertools import groupby
zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

zemljevid_potem = [
    ".##.#.",
    "..##.#",
    ".##.#.",
    "##.###",
    "###.##",
]

vrstica = ".##.####...##."

def dolzina_ovir(vrstica):
    return vrstica.count("#")

def stevilo_ovir(vrstica):
    return sum(1 for k,g in groupby(vrstica) if(k=='#'))

def najsirsa_ovira(vrstica):
    return max(len(list(g)) for k,g in groupby(vrstica))

def pretvori_vrstico(vrstica):
    rez = []
    i = 1
    for k,g in groupby(vrstica):
        dolzina = len(list(g))
        if k == "#":
            rez.append((i,i+dolzina-1))
        i += dolzina
    return rez

def pretvori_zemljevid(vrstice):
    rez = []
    for i,vrstica in enumerate(vrstice):
        rez.extend([el + (i+1,) for el in pretvori_vrstico(vrstica)])
    return rez

def izboljsave(prej, potem):
    for (k_prej,g_prej), (k_potem,g_potem) in zip(groupby(prej),groupby(potem)):
        if(k_potem == "#" and g_prej != g_potem):


print(dolzina_ovir(vrstica))
print(stevilo_ovir(vrstica))
print(najsirsa_ovira(vrstica))
print(pretvori_vrstico(vrstica))
print(pretvori_zemljevid(zemljevid))
print(izboljsave(prej, potem))
