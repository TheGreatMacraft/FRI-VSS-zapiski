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
# Indukcija

Indukcija je orodje za dokazovanje trditev "za vsa naravna števila".
## Primer: 
1 = 1 
1 + 3 = 4
1 + 3 + 5 = 9
1 + 3 + 5 + 7 = 16 
1 + 3 + 5 + 7 + 9 = 25
1 + 3 + 5 + 7 + 9 + 11 = 36

1+3+5+ ... + (2k-1) = $k^2$
Za vsako naravno število k velja, da je vsota najmanjših lihih naravnih števil enaka izrazu $k^2$

**Baza indukcije**: Trditev velja za najmanjše *ustrezno* naravno število. (Vsota nič (najmanjših) lihih števil je enaka $0^2$)

**Indukcijski korak**: Če trditev velja pri nekem naravnem številu n, potem velja tudi pri njegovem nasledniku n+1. (Če je vsota prvih n lihih števil enaka $n^2$, potem je vsota prvih n+1 lihih naravnih števil enaka $(n+1)^2$)

## Fibonaccijeva števila

Zaporedje Fibonaccijevih števil je definirano z začetnima členoma $f_0 = 0, f_1 = 1$ in rekurzivno zvezo $f_n = f_{n-1} + f_{n-2}$, ki velja za $n \ge 2$.

Naloga: Pokaži, da je Fibonaccijevo število $f_{3n}$ vedno sodo.

n=0: $f_{3*0} = f_0 = 0$ => je sodo
$f_{3(n+1)} = f_{3n+3} = f_{3n+2} + f_{3n+1}$
$= f_{3n+1}+f_{3n}+f_{3n+1}=$
$=2*f_{3n+1}+f_{3n}$

Za vsako naravno število $n$ so $f_{3n}, f_{3n+1}, f_{3n+2}$ sodo, liho in liho
Baza indukcije: $f_0 = 0, f_1 = 1, f_2 = 1$ so sodo, liho in liho

Indukcijski korak: $f_{3(n+1)}, f_{3(n+1)+1}, f_{3(n+1)+2}$ sodo, liho in liho, če verjamemo da so:
$f_{3n}, f_{3n+1}, f_{3n+2}$ soda, liho in liho

# Izjave

1. **Negacija** izjave $A, \neg A$, beremo kot "Ne A" in je resnična *natanko tedaj*, ko je A <u>neresnična</u>. $\neg$ je **enomestni** veznik

$\begin{array}{c|c}A & \neg A \\ \hline 0 & 1 \\ 1 & 0 \end{array}$

2. **Konjunkcija** izjav A in B ($A \land B$), beremo kot "A ali B" in je resnična *natanko tedaj*, ko je <u>vsaj ena</u> od izjav A ali B resnična