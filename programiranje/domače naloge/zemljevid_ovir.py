from itertools import groupby,zip_longest
zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

zemljevid_potem = [
    ".##.#.",
    ".....#",
    ".##.#.",
    "##....",
    "....##",
]

vrstica = ".##.####...##."

def dolzina_ovir(vrstica):
    return vrstica.count("#")

def stevilo_ovir(vrstica):
    return sum(1 for k,g in groupby(vrstica) if(k=='#'))

def najsirsa_ovira(vrstica):
    return max(len(list(g)) for k,g in groupby(vrstica) if k == "#")

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
    pretvorjeno_prej = pretvori_zemljevid(prej)
    return [el for el in pretvori_zemljevid(potem) if el not in pretvorjeno_prej]

def huligani(prej, potem):
    return izboljsave(prej,potem),izboljsave(potem,prej)

print(dolzina_ovir(vrstica))
print(stevilo_ovir(vrstica))
print(najsirsa_ovira("...#..."))
print(pretvori_vrstico(vrstica))
print(pretvori_zemljevid(zemljevid))
print(izboljsave(zemljevid, zemljevid_potem))
print(huligani(zemljevid, zemljevid_potem))
