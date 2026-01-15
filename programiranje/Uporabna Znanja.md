Čeprav sem mislil, da že marsikaj znam, sem ugotovil da v resnici nimam pojma. Zato je tukaj moja osebna, subjektivna zbirka uporabnih orodji in korektnih načinov uporabe teh orodji v tako čudnem jeziku kot je Fujton.

```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

WHAT IS A TOUPLE?? why cant i change them?
# Stringi

## Funkcije

### Split

Vrne seznam elementov, ki so v stringu ločeni z znakom.

```python
s = "one-two-three"

arr = s.split("-")
print(arr)

['one', 'two', 'three']
```

## Regex

Regex se uporablja za iskanje točno določenih struktur v stringih.
**Funkcije**:
- search - poišče en ustrezen element in se ustavi
- findall - poišče vse ustrezne elemente
- split - razdeli niz v seznam, glede na podan izsek niza

**Format**:
Vse zapišemo kot "raw" string (r"..."), ker lahko v nasprotnem primeru python "požre" "\\"

```python
import re

s = "sdsds(13)sdsdsd"

vse = re.search(r"\((\d+)\)",s) # (13)
st = re.search(r"\((\d+)\)",s).group(1) # 13
```

**Split**:
- Razdeli string, tako da iz elementov naredi seznam. Mesto kjer naj niz "preseka" na dva dela definiramo z regex zapisom.
- Če želimo, da v seznam shrani tudi "prelomni" niz med elementi, ga moramo dati v oklepaje.

```python
import re

s = "A---B--C-----D"

print(re.split(r"-+"),s) # brez minusov
print(re.split(r"(-+)"),s) # z minusi
```

Output:

```
['A','B','C','D']
['A','---','B','--','C','-----','D']
```
# Seznami (Lists)

## Append vs Extend

```python
seznam = [1,2,3]  
seznam.extend([4,5,6])  
seznam.append([7,8,9])  
print(seznam)

[1, 2, 3, 4, 5, 6, [7, 8, 9]]
```
Kot je moč videti, funkcija extend prejme nov element in vse podelemente tega elementa (če jih ima) doda seznamu **posamično**.

Funkcija append pa element, ki ga prejme enostavno doda na konec seznama, kot en zaključen element.

## Enumerate
Vrne pare indeksa elementa v seznamu in elementa samega.

```python
beseda = "Holly Fujton"  
print(list(enumerate(beseda)))
```

Output:
```
[(0, 'H'), (1, 'o'), (2, 'l'), (3, 'l'), (4, 'y'), (5, ' '), (6, 'F'), (7, 'u'), (8, 'j'), (9, 't'), (10, 'o'), (11, 'n')]
```
## Zip
```python
a = [[1,"a"],[2,"b"],[3,"c"]]  
b = [4,5,6]  
print(list(zip(a,b)))

[([1, 'a'], 4), ([2, 'b'], 5), ([3, 'c'], 6)]
```
Zip združi elemente seznamov, ki ležijo na istih indeksih in vrne njihov iterator.

## "Odštevanje" Seznamov
```python
a = [1,2,3]
b = [1,2,3,4,5,6]

c = a - b #NE DELUJE, ZATO NAREDIMO:

c = [el for el in b if el not in a] #TO PA SUPER DELUJE
print(c)

[4,5,6]
```

## Odstranjevanje podvojenih elementov

```python
a = [1, 2, 2, 3, 1]
b = list(dict.fromkeys(a))
print(b)

[1, 2, 3]
```
## GroupBy
```python
from itertools import groupby

beseda = "..###..##...#.#.#####."
for k,g in groupby(beseda):
	print(k,list(g))

. ['.', '.']
# ['#', '#', '#']
. ['.', '.']
# ['#', '#']
. ['.', '.', '.']
# ['#']
. ['.']
# ['#']
. ['.']
# ['#', '#', '#', '#', '#']
. ['.']
```
Groupby združi elemente seznama v key in group, tako da je key vrednost (v zgornjem primeru "." ali "#"), group pa je seznam te vrednosti, ponovljene tolikokrat, kot se je na tistem mestu pojavila v originalnem seznamu. Če ti tudi po tej razlagi stvar ni še čisto jasna, mi lahko pišeš [tu](https://chatgpt.com/).

# Množice (Set)



# Funkcije

## Vračanje **Večih** Seznamov
```python
def funkcija():
	a = [1,2,3]
	b = [4,5,6]
	return a,b

c,d = funkcija()
print(c,d)

[1, 2, 3] [4, 5, 6]
```

# Ostalo

## Range
Range poda seznam števil od števila a, do števila b, s korakom c.

```python
print(list(range(0,100,3)))
```

Output:
```
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
```

## Itertools

### Pairwise

Vrne *iterator tuple-ov* **trenutnega** elementa in **naslednjega** elementa.

```python
from itertools import pairwise

data = [1, 2, 3, 4]

for a, b in pairwise(data):
    print(a, b)
```

Output:
```
1 2
2 3
3 4
```

## Collections

### Counter

Counter je podoben *slovarju*, kjer so ključi podani *elementi*, vrednosti pa so števila, ki povejo *kolikokrat se element pojavi v slovarju*.

```python
from collections import Counter

c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(c)

c.update(['a','c']) # Dodamo elemente v counter
print(c)

print(c.most_common(3)) # Povemo koliko najbolj pogostih tuplov (element,št.) bi zeleli

print(c.most_common()) # Dobimo seznam tuplov (element,št.), sortiran padajoče po številu
```

Output:

```
Counter({'a': 3, 'b': 2, 'c': 1})

Counter({'a': 4, 'b': 2, 'c': 2})

[('a', 4), ('b', 2), ('c', 2)]
```
