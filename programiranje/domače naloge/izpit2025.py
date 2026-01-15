import re

# 1.

from collections import Counter
from itertools import pairwise

def povezave(pot):
    return set(pairwise(pot.split("-")))

def popularni(poti,k):
    s = Counter()
    for pot in poti:
        s.update(povezave(pot))
    return {popularne for popularne, _ in s.most_common(k)}

# 2.

def casi(pot):
    poti = re.split(r"(-+)",pot)
    return {(a,b) : len(c) for a,b,c in zip(poti[::2],poti[2::2],poti[1::2])}

# 3.

def krozenje(pot):
    st = 0
    pot = pot.split("-")
    for i,el in enumerate(pot[1:]):
        if el == pot[0]:
            st = i+1
            break

    poti = [pot[i:i+st] for i in range(0,len(pot),st)]

    for el in poti[1:]:
        st = 0
        for c in range(len(el)):
            if el[c] != poti[0][c]:
                st = st + 1
        if (st > 1):
            return False

    return True

# 4.

def detektiv(odkod, kam, povezave, obiskani):
    if kam in povezave[odkod]:
        return True

    if odkod in obiskani:
        return False

    obiskani.add(odkod)

    for naslednji in povezave.get(odkod,set()):
        if detektiv(naslednji,kam,povezave,obiskani):
            return True

    return False


povezave = {
"Ana": {"Berta"},
"Berta": {"Dani", "Cilka", "Franci"},
"Cilka": {"Ema", "Franci", "Iva", "Ana"},
"Dani": {"Cilka", "Ana"},
"Ema": {"Iva", "Helga"},
"Franci": {"Greta", "Iva", "Dani"},
"Greta": {"Franci"},
"Jana": {"Klara"},
"Klara": {"Jana"}
}

print(detektiv("Greta", "Ana",povezave,set()))