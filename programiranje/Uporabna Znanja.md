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

## Regex

Regex se uporablja za iskanje točno določenih struktur v stringih.
**Funkcije**:
- search - poišče en ustrezen element in se ustavi
- findall - poišče vse ustrezne elemente
**Format**:
Vse zapišemo kot "raw" string (r"..."), ker lahko v nasprotnem primeru python "požre" "\\"

```python
import re

s = "sdsds(13)sdsdsd"
vse = re.search(r"\((\d+)\)",s) # (13)
st = re.search(r"\((\d+)\)",s).group(1) # 13
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
```python
beseda = "Holly Fujton"  
print(list(enumerate(beseda)))

[(0, 'H'), (1, 'o'), (2, 'l'), (3, 'l'), (4, 'y'), (5, ' '), (6, 'F'), (7, 'u'), (8, 'j'), (9, 't'), (10, 'o'), (11, 'n')]
```
Enumerate vrne pare indeksov in elementov seznama. Precej enostavno, a izredno uporabno.

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