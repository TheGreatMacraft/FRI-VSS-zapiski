from itertools import chain
import re

def koordinate(s):
    odg = [(int(d),int(d)+len(minus)-1) for d,minus in re.findall(r"(\d+)(-+)",s)]
    return odg[0] if len(odg) == 1 else odg

def vrstica(s):
    s = s.replace(" ","")
    vrstica = int(re.search(r"\((\d+)\)",s).group(1))
    ks = koordinate(s[len(str(vrstica))+2:])
    ks = [ks] if isinstance(ks,tuple) else ks
    return [(el[0], el[1], vrstica) for el in ks]

def preberi(s):
    return sorted(list(chain.from_iterable([vrstica(str(a.strip())) for a in s.splitlines() if a != ""])),key=lambda x: (x[-1],x[0]))

def intervali(s):
    return  [f"{a}{"-"*(b-a+1)}" for a,b in s]

def zapisi_vrstico(y,xs):
    return f"({y}) " + " ".join(intervali(xs))

ovira = "5---"
vrstica_ovire = "(13) 90-----------   5---- 19---"
vse_ovire =""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""

ovire = [(6, 10), (12, 12), (20, 22), (98, 102)]

print(koordinate(ovira))
print(vrstica(vrstica_ovire))
print(preberi(vse_ovire))

print(intervali(ovire))
print(zapisi_vrstico(8,ovire))