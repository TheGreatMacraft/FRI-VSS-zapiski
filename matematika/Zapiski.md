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
# Zaporedja

## Rešitev računanja ničel polinoma: Zaporedja
- iskanje ničel funkcije je lahko v praksi precej zapleteno. Generiramo zaporedje približkov $x_0, x_1, x_2$, ..., ki se čedalje bolj približuje iskani rešitvi (ničli funkcije)

# Vrste
- seštevamo elemente zaporedja, da dobimo dovolj dober približek iskanega števila (funkcije, ploščine, ...)
- Vsako "lepo" funkcijo lahko zelo dobro aproksimiramo s polinomom v neki okolici:
$f(x) = f(a) +  \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3$

# Funkcije
- opis, kako se izhodni podatki "zvezno" spreminjajo glede na vhodne
- Npr: gibanje cene delnice, povprečna višina ljudi v odvisnosti od starosti, spremljanje temperature v 3D prostoru, ...

# Odvod
- opisuje lokalne značilnosti funkcije
- iskanje ekstremov funkcije
- reševanje diferencialnih enačb
# Integral
- povprečje podatkov
- ploščine telesa
- težišče telesa
- verjetnost (pričakovana vrednost)
- FEM/BEM za numerične simulacije
# Vektorji
- opis koordinat gibanja telesa
- računanje kotov med stranicama

# Matrike
- opisovanje linearnih sprememb količin
- iskanje spletnih strani (pafe rank)
- določanje najbolj problematičnih lastnih frekvenc
- rekonstrukcija površine iz danih točk v prostoru
- simulacija gibanja tekočin

$\begin{bmatrix} 1 & 0 & 1 & 0 \\ 3 & -1 & 3 & -1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 2 & 0 \end{bmatrix}$

---

# Številske množice
## Naravna števila
- števila za seštevanje in množenje - ostale operacije lahko vodijo do rezultatov, ki ne spadajo v množico naravnih števil
$\mathbb{N} = \{0,1,2,3 ...,n, ...\}$

## Cela števila
- lahko jih seštevamo, množimo in odštevamo
$\mathbb{Z} = \{ ...,-n,...,-3,-2,-1,0,1,2,3,...,n,...\}$
$\mathbb{Z} = \mathbb{N} U \mathbb{N}^-$
$\mathbb{N} = \{-n | n \in \mathbb{N}\}$ -> vzamemo negativno vrednost n, če je n element množice naravnih števil.

## Racionalna števila
$\mathbb{Q} = \{\frac{n}{m} |$ kjer $n,m \in \mathbb{Z}$ in $m \ne 0\}$
- vsako racionalno število lahko predstavimo kot okrajšan ulomek $\frac{x}{y}$, kjer $x \in \mathbb{Z}, y \in \mathbb{N}, y \ne 0$ in x in y nimata skupnih deljiteljev
- lahko seštevamo, odštevamo, delimo in množino, razen **NE DELIMO Z 0**
- $\sqrt{2}$ ni racionalno število (ne moremo zapisati kot ulomek) dokaz:
$\sqrt{2}+1 = \frac{p}{q}$ (okrajšan)
$(\sqrt{2}+1)(\sqrt{2}-1) = 2-1 = 1$
Torej $\sqrt{2}-1 = \frac{q}{p}$ (ker je $\frac{p}{q} * \frac{q}{p} = 1$) 
Razlika med $\sqrt2+1$ je celo število
Ampak če se dve racionalno števili seštejeta ali odštejeta v celo število, morata imeti isti imenovalec.
Torej p=q, sledi $\sqrt2+1 = 1$
Torej $\sqrt2$ ni racionalno št.

## Realna števila
$R = Q \cup \{..., \sqrt{2},\sqrt{3},\pi,...\}$
- Realna števila = racionalna + iracionalna
- lahko seštevamo, odštevamo, množimo in delimo razen deljenje z 0
- lahko jih predstavimo kot točke na *številski premici*
- zapišemo jih kot *neskončna decimalna števila*
- lahko jih zapišemo tudi z ulomki ($\frac{\sqrt2}{2}$)
- različna decimalna števila lahko predstavljajo isto realno število:
$1 = 0.\bar9 = 0.999 ...$

![[Pasted image 20251002104845.png]]

## Številska premica in intervali
- vsa števila lahko napišemo na številski premici
- posebej pomembne množice števil so intervali
- Omejeni intervali ali daljice na številski premici:
	- $(a,b) = \{x \in \mathbb{R} |a < x < b \}$ odprti interval
	- $[a,b] = \{x \in \mathbb{R} |a \le x \le b \}$ zaprti interval
	- $(a,b] = \{x \in \mathbb{R} |a < x \le b \}$ polodprti/polzaprti interval
	- $[a,b) = \{x \in \mathbb{R} |a \le x < b \}$ polodprti/polzaprti interval
- Neomejeni intervali ali poltraki na številski premici:
	- $(a,\infty) = \{x \in \mathbb{R}|a < x\}$ odprt navzgor neomejen interval
	- $(-\infty,b) = \{x \in \mathbb{R}|x < b\}$ odprt navzdol neomejen interval
	- $[a,\infty) = \{x \in \mathbb{R}|a \le x\}$ zaprt navzgor neomejen interval
	- $(-\infty, b] = \{x \in \mathbb{R}|x \le b\}$zaprt navzdol neomejen interval
- $\infty$ ni število...

## Odstotki - procenti
- Delež $\frac{p}{100}$ neke celote, lahko izrazimo kot p% dane celote.
- Če se originalna vrednost O poveča za p%, je nova vrednost: $O * \frac{p}{100}$
- **Obrestovalni faktor**, pri podražitvi je $r = 1+\frac{p}{100}$, pri pocenitvi pa $r = 1-\frac{p}{100}$. 

## Absolutna vrednost
- **Absolutna vrednost $|x|$ števila $x \in \mathbb{R}$ je razdalja števila x od števila 0 na številski premici in je enaka
$|x| =\begin{cases}x & ; & x \ge 0 \\ -x, & ; & x < 0\end{cases}$

- **Razdalja med številoma x in y je enaka |x-y|**.
- Osnovne lastnosti:
	- $|x| \ge 0$ za vsak $x \in \mathbb{R}$
	- $|xy| = |x||y|$
	- trikotniška neenakost: $|x+y| \le |x| + |y|$
### Geometrijsko
Določimo množico realnih števil x, za katere velja $|x-3| \le 2$.
1. Način: To so vsa števila, ki so od 3 oddaljena za manj ali enako 2. Če si to narišemo na številsko premico, je očitno da je $x \in [1,5]$.
2. Način: Zaporedoma obravnavamo skice grafov $y=x-3, y=|x-3|$ in ugotovimo, da je $|x-3 \le 2$ za $x \in [1,5]$

## Kompleksna števila
- **Kompleksna števila** so "kompleksna" števila ali tudi "dvodimenzionalna števila" s katerimi lahko uspešno računamo v ravnini.
- Na $\mathbb{R}$ osi velja: 1 = 1 * $(-1)^0$ in -1 = 1 * $(-1)^1$, pri čemer nam potenca šteje kolikokrat smo število 1 zavrteli okrog izhodišča za 180$^\circ$ v pozitivni smeri. Tudi pomen dvakratnega vrtenja okrog izhodišča za $180^o$ v pozitivni smeri se ujema s preprosto enačbo: $1 = 1*(-1)^2$ in enako velja za vse cele potence 1. $(-1)^n$.
- Če $1-(-1)^\frac{1}{2}$ interpretiramo kot rotacijo števila 1 za polovico od $180^o$, torej $90^o$ okrog izhodišča v pozitivni smeri in to število označimo kot **imaginarno enoto**: $i = \sqrt{-1} = (-1)^\frac{1}{2} \implies i^2 = -1$, dobimo novo in zelo uporabno teorijo kompleksnih števil, ki omogoča računanje v ravnini.
- Kompleksno število $z = x +yi$, $x,y \in \mathbb{R}$, ima:
	- x = Re (z) **realni del**
	- y = Im (z) **imaginarni del**

![[Drawing 2025-10-09 10.36.50.excalidraw]]
