
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

**Absolutna vrednost** kompleksnega števila z je $|z| = \sqrt{x^2+y^2}$. Kot pri realnih številih pomeni razdaljo od izhodišča. Absolutna vrednost razlike dveh kompleksnih števil pomeni razdaljo med številoma. $\implies$ Enačbo $|z-\frac{1}{2}| = \frac{1}{4}$ rešijo vsa števila $z \in C$, ki ležijo na krožnici s središčem v $\frac{1}{2}$ in radijem $\frac{1}{4}$.

### Konjugiranje

- Konjugirano število dobimo tako, da spremenimo predznak imaginarnega dela.
- $\overline{x+yi}$ = $x-yi$ je **konjugirano število**. Primer: $\overline{3+2i} = 3-2i$
![[Pasted image 20251016081641.png]]
- Seštevanje & odštevanje: $(x+yi) + (u+vi) = (x+u) + (y+v)i$
	Primer: $(3+2i) + (1-i) = (3+1) + (2-1)i = 4+i$
- Množenje: $(x+yi)(u+vi)$ = $(xu-yv) + (xv + yu)i$
	Primer: $(3+2i)(1-i) = (3+2)+(-3+2)i = 5 - i$
- Deljenje: $\frac{z}{w} = \frac{z*\overline{w}}{w*w} = \frac{z*\overline{w}}{|x|^2}$

Kompleksni števili sta enaki, kadar imata enaka realna in imaginarna dela.
- $z = \overline{z}$
- $\overline{z+w} = \overline{z}+w$
- $\overline{z-w} = \overline{z}*\overline{w}$
- $z + \overline{z} = 2Re(z)$, $z - \overline{z} = 2Im(z)$
- $|\overline{z}| = |z|$
- $|z*w| = |z|*|w|$
- $|z+w| \le |z| + |w|$ **trikotniška neenakost**

### Polarni zapis kompleksnega števila

Zakaj so radiani boljši:
![[Drawing 2025-10-16 08.54.07.excalidraw]]

- $|z| = \sqrt{x^2+y^2}$
- $\gamma = \arctan{\frac{y}{w}}$
- $x = |z|\cos{\gamma}$ in $y=|z| \sin{\gamma}$
- **Polarni zapis** števila $z = x+yi$ je$|z| * (\cos{\gamma} + i\sin{\gamma}) = |z| * e^{i*\gamma}$
- **Eulerjeva identiteta**: ($e^{i\pi}+1=0$)
![[Drawing 2025-10-16 08.59.31.excalidraw]]
Kompleksno število z opišemo z dvema parametroma:
- dolžina od izhodišča (r)
- kot ($\gamma$)
*Slabost*: Kot ni enolično določen
z = 0 (r=0, $\gamma$ kar koli)
- $\gamma = Arg(z)$ imenujemo **polarni kot** ali **argument**. Argument je določen samo do mnogokratnika celega kota $2\pi^{rd} = 360^o$ natanko.

#### Množenje v polarni obliki

$z_1 = r(\cos\gamma + i \sin\gamma)$
$z_2 = q(\cos\psi + i \sin\psi)$

$z_1*z_2 = r*q[(\cos\gamma * \cos\psi - \sin\gamma * \sin\psi) + i(\cos\gamma * \sin\psi + \sin\gamma * \cos\psi)] =$$rq[\cos(\gamma + \psi) + i \sin(\gamma + \psi)]$  $\implies$ razdalja se zmnoži, kot pa se sešteje.

*Eulerjev zapis:* $e^{i\gamma} = \cos\gamma + i \sin\gamma$, polarni zapis se poenostavi $z=|z|*e^{i\gamma}$

Kaj se zgodi če množimo realna števila?
	
	$3*2 = 6$
	Polarno: $|3| * (\cos0 + \sin0) * |2| * (\cos0 + \sin0) = 6$
	Euler: $|3|*e^{i*0}*|2|*e^{i*0} = |6|*e^0 = 6$
	
	$(-3)(-2) = 6$
	Polarno: $|3|*(\cos\pi + \sin\pi) * |2| * (\cos\pi + \sin\pi) =$$|6| * (\cos(2\pi)+\sin(2\pi)) = |6| * (\cos0 + \sin0) = 6$

Množenje se poenostavi: $z_1z_2 = |z_1||z_2|e^{i(\gamma_1+\gamma_2)}$
-  množenje: absolutni vrednosti se zmnožita, argumenta se seštejeta
- potenciranje: $z = |z|e^{i\gamma} \implies z^n = |z|^ne^{i\gamma n}$ (*De Moivrova formula*)
- korenjenje: $z = |z|e^{i\gamma} \implies z^{\frac{1}{n}} = |z|^{\frac{1}{n}}e^{i\frac{\gamma}{n}}$ (*De Moivrova formula*)
Velja:


#### Zapišemo v polarni obliki
- $1 = |1|*e^{i*0}$
- $-1 = |-1|*e^{i\pi0}$
- $i = |i|*e^{i\frac{\pi}{2}}$
- $-i = |-i|*e^{i\frac{3\pi}{2}}$
- $1+i = \sqrt{2}e^{i\frac{\pi}{4}}$
- $-1-i = \sqrt{2}e^{i\frac{5\pi}{4}}$

Vse vrednosti, na enotski krožnici imajo absolutno vrednost 1.

Izračunajmo $(\frac{\sqrt{2}}{2}+\frac{1}{2}i)^{12}$
![[Drawing 2025-10-16 10.23.07.excalidraw]]

#### Koreni kompleksnega števila
**n-ti koreni** števila $a \in C$ so rešitve enačbe $z^n = a$.
- Enačbo zapišemo v polarni obliki: $a = |a|*e^{i\psi}$
- Dobimo n različnih rešitev: $z_k = \sqrt[n]{|a|}e^{i\frac{\psi+2k\pi}{n}}$, $k = 0,1,...n-1$
- Rešitve ležijo na ogliščih pravilnega n-kotnika v kompleksni ravnini.

![[Drawing 2025-10-23 08.26.17.excalidraw]]

![[Pasted image 20251023084159.png]]

![[Drawing 2025-10-23 08.42.27.excalidraw]]

# Zaporedja
**Zaporedje** je neka urejena množica 'zaporedoma' postavljenih števil. Matematično natančneje rečemo, da je zaporedje preslikava $\mathbb{N} \rightarrow \mathbb{R}$, $i \mapsto a_i$, ki vsakemu naravnemu številu i (indeksu) priredi točno določeno realno število $a_i$. Pri tem jih imenujemo i indeks, $a_i$ pa i-ti člen zaporedja.

Zaporedje predstavimo:
- z naštevanjem: 1,2,4,8, ...
- opisno: "Vsa soda števila"
- eksplicitno: $a_n = \frac{1}{n}$ za $n \ge 1$ (podano eksplicitno z izrazom $a_n = f(n)$ in neko točno določeno funkcijo $f(x)$)
- rekurzivno: $a_0 = 1$ in $a_{n+1} = 2a_n$ za $n  \ge 0$ (podano s prvim členom $a_0$ ali $a_1$ in neko točno določeno funkcijo $f(x)$, ki pove, kako iz $a_n$ dobimo $a_{n+1}$)

Geometrijsko lahko zaporedje predstavimo:
- na številski premici:
![[Pasted image 20251023085610.png]]
Ko člene narišemo, se ne vidi 'zaporednosti' členov (kateri člen je 3. ali 4.).
- kot točke ($n,a_n$) v ravnini:
![[Pasted image 20251023085759.png]]
Abscisa (x-koordinata) točke pove *kateri člen* zaporedja je enak ordinati (y-koordinati).

## Primer

**Aritmetično zaporedje**
- Intuitivni opis: Začnemo z neko vrednostjo. 'Delamo' enako dolge korake v desno.
- Eksplicitni opis: $a_n = a + nd$
- Rekurzivni opis: $a_0 = a,a_{n+1} = a_n + d$
- Primer: $1,2,3,4,5,...$
- Primer: $1,3,5,7,9,...$
- Primer: $1,1+\sqrt{3},1+2\sqrt{3},1+3\sqrt{3},1+4\sqrt{3},...$

**Geometrijsko zaporedje**
- Intuitivni opis: Začnemo z neko vrednostjo. V vsakem koraku prejšnjo vrednost pomnožimo z istim faktorjem.
- Eksplicitni opis: $a_n = aq^n$
- Rekurzivni opis: $a_0 = a$, $a_{n+1} = a_nq$

## Lastnosti zaporedji
- **Naraščajoče** zaporedje: $a_n \le a_{n+1}$, za vse $n \in \mathbb{N}$
- **Strogo naraščajoče** zaporedje: $a_n < a_{n+1}$ za vse $n\in N$
- **Padajoče** zaporedje: $a_n \ge a_{n+1}$ za vse $n\in \mathbb{N}$
- **Strogo padajoče** zaporedje: $a_n > a_{n+1}$ za vse $n\in \mathbb{N}$
- **Navzgor omejeno** zaporedje: Obstaja zgornja meja $M \in \mathbb{R}$, da velja $a_n \le M$, za vse $n\in \mathbb{N}$
- **Navzdol omejeno** zaporedje: Obstaja spodnja meja $m \in R$, da velja $m \le a_n$, za vse $n\in \mathbb{N}$
- **Navzgor in navzdol omejeno** zaporedje: Obstajata meji $m,M$, da velja $m  \le a_n \le M$, za vse $n \in \mathbb{N}$

M in m **nista enolično določena**. Če je $m = 0$, je $m \le 0$ in če $M = n$, je $M \ge N$.

## Stekališče zaporedja
**Stekališče** zaporedja je število k kateremu se '*steka*' neskončno členov zaporedja. Natančneje, **Stekališče** zaporedja je tako število, da je *v vsaki njegovi okolici neskončno členov zaporedja*. Zaporedje ima lahko več stekališč.
![[Pasted image 20251023095859.png]]

![[Drawing 2025-10-23 10.27.57.excalidraw]]

## Limita zaporedja
**Limita** zaporedja je tako število, da je v vsaki njegovi okolici *neskončno* členov, zunaj te okolice pa končno členov zaporedja. Je taka točka, od katere naprej bodo vsi elementi v njeni okolici.
![[Drawing 2025-10-23 10.38.55.excalidraw]]
- Lahko rečemo tudi: **Limita** zaporedja $a_n$ je tako število L, da za vsak $\epsilon > 0$ obstaja tak indeks $N \in \mathbb{N}$, da velja $|L-a_n| < \epsilon$, za vse $n \ge N$.
- Limito zaporedja $a_n$ označimo $\displaystyle \lim_{n \to \infty} a_n$
- Zaporedje ima lahko več stekališč in zato **nima limite**.
- Zaporedje ima lahko eno samo stekališče, pa vseeno to stekališče ni nujno limita.
- Limita zaporedja je **vedno** stekališča, obratno pa **ni vedno** res.

Zaporedje je **konvergentno**, če ima limito. V nasprotnem primeru je **divergentno**.
- Naraščajoče in navzgor omejeno zaporedje je konvergentno.
- Padajoče in navzdol omejeno zaporedje je konvergentno.

### Računanje limit
Če je $\displaystyle \lim_{n \to \infty} a_n$ in $\displaystyle \lim_{b \to \infty} b_n = b$ potem velja:
- $\displaystyle \lim_{n \to \infty} (a_n+b_n) = a+b$
- $\displaystyle \lim_{n \to \infty}a_n*b_n = ab$
- Če je $b_n \ne 0$ za vsak n in $b \ne 0$, je $\displaystyle \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{a}{b}$
- Če je $a_n > 0$, za vsak n in $a > 0$, je $\displaystyle \lim_{n \to \infty}a_n^{b_n} = a^b$

### Izrek o "sendviču"
Če za vsak n velja $a_n \le b_n \le c_n$ in $\displaystyle \lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = a$, je tudi $\displaystyle \lim_{n \to \infty} b_n = a$
![[Drawing 2025-10-30 08.30.32.excalidraw]]

# Vrste

Vrsta je vsota členov zaporedja. Iz končnih zaporedji tako dobimo **končne vrste**, ki jih vedno lahko izračunamo. Pri neskončnih vrstah pa o vsoti neskončno mnogo členov ne moremo govoriti, saj ni mogoče sešteti neskončno členov.

**Vrsta** je končna vsota členov: $a_1 + a_2 + a_3 + ... + a_k$, ki jo zapišemo krajše s sumacijskim znakom $\displaystyle a_1 + a_2 + a_3 + ... + a_k = \sum_{i=1}^k a_i$ (končna vsota)
$\displaystyle a_1 + a_2 + ... = \sum_{i=1}^\infty a_i$ (neskončna vsota)
$\displaystyle a_1 + a_2 + ... = \lim_{n \to \infty}(q_1 + a_2 + ... + a_n)$
$\displaystyle \sum_{i=1}^\infty a_i = \lim_{n \to  \infty}(\sum_{i=1}^n a_i)$
delna vsota(Sn) = $\displaystyle \sum_{i=1}^n a_i$
neskončna vsota: $\displaystyle \sum_{i = 1}^\infty a_n = \lim_{n\to\infty}Sn$
**Neskončna vsota je konvergentna, če obstaja limita delnih vsot $S_n$.**

Vrsta $\displaystyle \sum_{i=1}^\infty a_i$ je **konvergentna**, če je konvergentno zaporedje delnih vsot $\displaystyle Sn = \sum_{i=1}^n a_i$.
Vrsta je torej konvergentna, če lahko smiselno govorimo o njeni vsoti. V nasprotnem primeru je vrsta **divergentna**.

Torej, če je vrsta $\displaystyle \sum_{n=1}^\infty$ konvergentna, je $\displaystyle \lim_{n\to\infty} a_n = 0.$ Vendar pa obratno ni nujno res. **Harmonična vrsta** (divergentna) je vrsta, katere členi sicer gredo proti 0, vendar pa ni konvergentna. Če bi člene tako vrste seštevali dovolj dolgo, bi prišlo do poljubno velikega števila.

Primer: $\displaystyle \sum_{n=1}^\infty \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + ...$

Če za pozitivne člene $a_n$ velja $\displaystyle \lim_{n\to\infty} a_n = 0$, potem je vrsta $\displaystyle \sum_{n=1}^\infty (-1)^n * a_n$ konvergentna. Torej, če členom alterniramo predznak, imajo vsote limito.

Primer: $\displaystyle \sum_{n=1}^\infty \frac{(-1)^n}{n} = -1 + \frac{1}{2} - \frac{1}{3} + \frac{1}{4} - \frac{1}{5} + ...$ = $log_e2 = -0.693147$

## Geometrijska vrsta
Formula končne vsote: $\displaystyle \sum_{i=0}^n a*q^i = a * \sum_{i=0}^n q^i = a * \frac{1-q^{n+1}}{1-q}$
Neskončna vsota:
$\displaystyle \sum_{i=0}^\infty a*q^i = \lim_{n\to\infty}(\sum_{i=0}^n a * q^i) = lim_{n\to\infty}(q * \frac{1-q^{n+1}}{1-q})$

# Funkcije

**Funkcija** je predpis, ki vsakemu elementu x iz **definicijskega območja $D_f \subset \mathbb{R}$** priredi natanko določeno število $f(x) \in \mathbb{R}$.
$f: D_f \rightarrow \mathbb{R}$ (funkcija f "slika" iz definicijskega območja v realna števila)
$x \mapsto f(x)$ (x se "preslika" v f(x))
- x je **argument** (neodvisna spremenljivka), y (=$f(x)$) pa je odvisna spremenljivka. Odvisnost se nanaša na neodvisno spremenljivko x in predpis same funkcije f.
- **Definicijsko območje** $D_f$ so vse vrednosti x, za katere lahko izračunamo f(x), oziroma za katere ima predpis f(x) smisel. (množica vseh x-ov, ki jih vstavljamo v funkcijo)
- **Zaloga vrednosti** $Z_f = f(D_f)$ so vse vrednosti y, ki jih dobimo kot y=f(x), ko x "preteče" celo definicijsko območje. (množica vseh y-ov, ki jih dobimo iz funkcije)

## Graf funkcije
**Graf funkcije** f je množica točk (x,f(x)) v ravnini.
$\ulcorner (f) = \{(x,f(x));x\in D_f\}\subset \mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$
- Graf funkcije seka poljubno navpično premico **največ** v eni točki, saj za vsak $x \in D_f$ dobimo **samo eno točno določeno** vrednost f(x).
![[nepravilni_grafi.png]]

## Naraščanje & padanje
Če za funkcijo na nekem intervalu iz definicijskega območja velja:
- $x_1 \le x_2 \implies f(x_1) \le f(x_2)$, rečemo, da funkcija na danem intervalu **narašča**.
- $x_1 \le x_2 \implies f(x_1) \ge f(x_2)$, rečemo, da funkcija na danem intervalu **pada**.

## Sode & lihe funkcije
- Funkcija f(x) je **soda**, če je *simetrična preko y osi*. Zapišemo: $f(-x) = f(x)$, torej ima isto vrednost pri x-u, kot pri $-$x-u.
![[Pasted image 20251111081623.png]]
- Funkcija f(x) je **liha**, če je *simetrična preko izhodišča*. Zapišemo: $f(-x) = -f(x)$
![[Pasted image 20251111081753.png]]
- Funkcija f(x) lahko hkrati ni niti soda, niti liha, če ne sledi nobenemu od predpisov.
![[Pasted image 20251111081918.png]]

## Injektivne & surjektivne funkcije
- Funkcija f(x) je **injektivna**, če za $x_1 \ne x_2$ velja $f(x_1) \ne f(x_2)$, kar pomeni, da injektivna funkcija pri dveh različnih x-ih ne more imeti enake vrednosti. Na grafu velja, da *vsaka vodoravna premica seka graf **največ enkrat***.
![[Pasted image 20251111082223.png]]
- Funkcija f(x) je **surjektivna**, če za vsako vrednost $y \in \mathbb{R}$ obstaja vrednost $x \in D_f$, da velja f(x) = y, preprosto lahko rečemo, da surjektivna funkcija zavzame vsako vrednost oz. $Z_f = \mathbb{R}$. Na grafu velja, da *vsaka vodoravna premica seka graf **vsaj enkrat***.
![[Pasted image 20251111082501.png]]
- Funkcija f $D_f \rightarrow \mathbb{R}$ je **bijektivna**, če je injektivna in surjektivna hkrati. Za vsak $y\in \mathbb{R}$ obstaja **natanko en** $x\in D_f$, da drži $f(x)= y$. Na grafu velja, da *vsaka vodoravna premica seka graf **natanko enkrat***.
![[Pasted image 20251111082612.png]]
- Funkcija pa lahko hkrati ni niti injektivna, niti surjektivna. Primer $f(x) = x^2$
![[Pasted image 20251111083240.png]]

## Kompozitum ali sestavljena funkcija
Za funkciji f(x) in f(x) definiramo **kompozitum** funkcij
$(g \circ f)(x) = g(f(x))$ - kompozitum dveh funkcij pomeni *zaporedno delovanje dveh funkcij*, ki ga smatramo kot novo funkcijo. Odvisna spremenljivka (rezultat) notranje funkcije postane neodvisna spremenljivka zunanje funkcije.
$f \circ g \ne g \circ f$

## Inverzna funkcija
Če je f(x) **injektivna** funkcija, potem velja $(f^{-1}\circ f)(x) = x$ in $(f \circ f^{-1})(x)=x$, kjer je $f^{-1}$ **inverzna funkcija** funkcije f. Velja tudi $f^{-1} \circ f = f \circ f^{-1} = id$, pri čemer id označuje identično funkcijo id(x) = x. Če $f(x) = y$, potem $f^{-1}(y) = x$

Če funkcija nebi bila injektivna, bi različni x-i imeli enak y. Z istim y-om, pa v inverzni funkciji nebi dobili vseh x-ov.

Graf inverzne funkcije $f^{-1}$ dobimo tako, da prezrcalimo graf funkcije f prek simetrale lihih kvadrantov.

Inverzno funkcijo $f^{-1}$ lahko dobimo tako, da v zapisu funkcije f zamenjamo x in f(x) in poskusimo izolirati f(x)

$f(x) = 2x + 1 \implies y = 2x + 1$
$f^{-1}(x): x = 2y + 1 \implies x - 1 = 2y \implies$$y = \frac{x}{2}-\frac{1}{2}$
$f^{-1}(x) = \frac{x}{2} - \frac{1}{2}$ je inverzna funkcija od $f(x) = 2x + 1$

## Transformacije funkcij
S kompozitumi si pomagamo pri **transformacijah** funkcij.
$g(x) = x + 1$
$(g \circ f)(x) = g(f(x)) = f(x) + 1 \implies$ premik f(x) za 1 *navzgor*

$(f \circ g)(x) = f(g(x)) = f(x+1) \implies$ premik f(x) za 1 *levo*

### Premiki funkcij
1. Vodoravno:
	- premik **levo**: $f(x+a)$
	- premik **desno**: $f(x-a)$
	- **razteg**: $f(\frac{x}{a})$
	- **krčenje**: $f(x*a)$
2. Navpično:
	- premik **navzgor**: $f(x) + a$
	- premik **navzdol**: $f(x) - a$
	- **razteg**: $f(x) * a$
	- **krčenje**: $\frac{f(x)}{a}$
3. Zrcaljenje:
	- preko **x** osi: $-f(x)$
	- preko **y** osi: $f(-x)$

## Potenčna funkcija
Je vsaka funkcija oblike $f(x) = x^a; a\in \mathbb{R}$, tudi $f(x) = x^{-1}$, itd. 

1. **Liha pozitivna potenca**: $f(x) = x^{2k + 1}; k\in \mathbb{N}$
	- $D_f = \mathbb{R}$ - definirana za **vsa realna števila**
	- $Z_f = \mathbb{R}$ - funkcija se preslika v **vsa realna števila**
	- je **liha**
	- **strogo naraščajoča**
	- neomejena
	- injektivne, surjektivne $\implies$ **bijektivne**
	![[Pasted image 20251112182140.png|150]]

2. **Soda pozitivna potenca**: $f(x) = x^{2k}; k\in \mathbb{N}$
	- $D_f = \mathbb{R}$ - definirana za **vsa realna števila**
	- $Z_f = [0,\infty)$ oz. $\mathbb{R}^+ +\{0\}$ - funkcija se preslika v **vsa *nenegativna* realna števila**
	- je **soda**
	- na ($-\infty,0$] **strogo padajoča**, na $[0,\infty)$ **strogo naraščajoča**
	- navzdol omejena ($m=0$)
	- niti injektivna, niti surjektivna
	![[Pasted image 20251112182219.png|200]]


>[!info]  $f(x)=x^0 \equiv 1$
>To *konstantno* funkcijo štejemo med potenčne funkcije s *sodo pozitivno potenco*. Ima $D_f = \mathbb{R}$ in $Z_f = \{1\}$. Nikjer ne narašča/pada in ni niti injektivna, niti surjektivna.

3. **Liha negativna potenca**: $f(x) = x^{-(2k+1)};k\in \mathbb{N}$
	- $D_{f} = \mathbb{R}-\{0\}$ - definirana za **vsa realna števila, *razen 0***
	- $Z_{f} = \mathbb{R} - \{0\}$ - preslika se v **vsa realna števila, *razen 0***
	- je **liha**
	- **strogo padajoča**
	- neomejena
	- **injektivna** (ni surjektivna, ker ne zavzame vrednosti 0)
	![[Pasted image 20251112182248.png|150]]

4. **Soda negativna potenca**: $f(x)=x^{-2k};k\in \mathbb{N}$
	- $D_{f} = \mathbb{R} - \{0\}$ - definirana za **vsa realna števila, *razen 0***
	- $Z_{f}=(0,\infty) = \mathbb{R}^{+}$ - preslika se v **vsa *pozitivna* realna števila**
	- je **soda**
	- na $(-\infty,0)$ je **strogo naraščajoča**, na $(0,\infty)$ pa **strogo padajoča**
	- navzdol omejena ($m = 0$)
	- niti injektivna, niti bijektivna
	![[Pasted image 20251112182317.png|200]]

5. **Ne-cela potenca**: $f(x)=a * x^{n};a\in \mathbb{R} \textbackslash \{0\}, n\in \mathbb{Q}\textbackslash \mathbb{Z}$
	- $D_{f} = [0,\infty) \equiv \mathbb{R}^+ + \{0\}$ - definiran samo za **nenegativna realna števila**
	- $Z_{f} = [0,\infty) \equiv \mathbb{R}^++\{0\}$ - preslika se v **nenegativna realna števila**
	- vse gredo skozi točko (1,1)
	- funkcija se spreminja glede na potenco:
	![[Pasted image 20251112185625.png|250]]

## Polinomi
Glede na *najvišjo stopnjo* neodvisne spremenljivke v funkciji, poznamo polinome raznih stopenj: $f(x)=x^{7}+2x^{2}+8x + 23 \implies \text{Polinom 7. stopnje}$

### Ponovitev
1. Polinom prve stopnje: $f(x) = k*x+n$
	- predstavlja premico
	- n je **začetna vrednost** $\implies$ Premica gre čez točko (0,n)
	- k je **smerni koeficient** premice $\implies$ Premica gre čez točko (1,n+k)

2. Polinom druge stopnje: $f(x)=ax^{2}+bx+c$
	- za $a\ne 0$ predstavlja kvadratno funkcijo
	- **temenska oblika**: $ax^{2}+bx+c = a(x-p)^{2}+q; p=-\frac{b}{2a},q=\frac{{4ac-b^{2}}}{4a}$, kjer je T(p,q) **teme** - minimum funkcije ($a>0$) ali maksimum funkcije ($a < 0$)
### Splošno
**Splošna oblika**: $p(x) = a_{n}x^{n}+a_{n-1}x^{n-1}+\dots a_{1}+a_{0};a_{n}\ne 0, a_{i}\in \mathbb{R}$
- $a_{0},a_{1},\dots,a_{n}$ - koeficienti
- $a_{n}\neq0$ - vodilni koeficient (določa stopnjo polinoma $=n$)
- $a_{0}$ - začetna vrednost polinoma
- $D_{f} = \mathbb{R}$

**Ničelna oblika**:
$p(x)=a(x-x_{1})(x-x_{2})\dots(x-x_{n})$
- enostavno razberemo ničle polinoma (kje graf seka x-os $\implies y=0$)

### Deljenje Polinoma
$\frac{x^{2}+x}{x^{2}-4} = 1 + \frac{x+4}{x^{2}-4}$
![[Drawing 2025-11-13 09.48.08.excalidraw]]

### Nerazcepni polinomi
- polinomi, ki *realnih* ničel sploh nimajo
- lahko pa ga razcepimo v množici kompleksnih števil $\mathbb{C}$, saj $x^{2}+1=(x-i)(x+i)$, kjer je $i\in \mathbb{C}$ kompleksno število, za katerega velja $i^{2}=-1$
- nerazcepen je tudi vsak polinom oblike $p(x)=x^{2}+c; c > 0$. Lahko se razcepi v $\mathbb{C}$, kot $x^{2}+c=(x-i\sqrt{ c })(x+i\sqrt{ c })$
- obstajajo polinomi brez ničel: $p(x)=(x^{2}+1)(x^{2}+2)(x^{2}+5)=x^{6}+8^{4}+17x^{2}+10$ nima nobene realne ničle
- vsak polinom *lihe stopnje* ima **vsaj eno realno ničlo**
- polinom *n-te stopnje* ima **največ n-ničel**
- vse polinome je mogoče razcepiti na **linearne, nerazcepne kvadratne faktorje s koeficienti v $\mathbb{R}$** ($x^{3}-x^{2}+x-1=(x-1)(x^{2}+1)$) in na **linearne faktorje s koeficienti v $\mathbb{C}$** ($x^{3}-x^{2}+x-1=(x-1)(x-i)(x+i)$)
### Interpolacijski polinom
Če si izberemo povsem naključne točke z različnimi x-vrednostmi, vedno obstaja polinom, katerega graf vsebuje vse te točke. Če točke: $(x_{1},y_{1}),(x_{2},y_{2}),\dots,(x_{n},y_{n})$, potem obstaja $P(x_{1})=y_{1}, P(x_{2})=y_{2},\dots,P(x_{n})=y_{n}$

#### Lagrangeov način iskanja
$$
P(x) = \sum_{i=1}^{n} y_{i}.L_{i}(x)
$$
$$
L_{i}(x) = \prod_{j=1\atop j\ne i}^{n} \frac{{x-x_{i}}}{x_{i}-x_{j}}
$$
- n - število točk

**Postopek**:
Točke $(x_{1}y_{1}),(x_{2},y_{2}),\dots,(x_{n},y_{n})$

- Zgradimo $L_{1},L_{2},\dots,L_{n}$:
$L_{1}(x)=\frac{(x-x_{2})(x-x_{3})\dots(x-x_{n})}{(x_{1}-x_{2})(x_{1}-x_{3})\dots(x_{1}-x_{n})}$
$L_{2}(x)=\frac{(x-x_{1})(x-x_{3})\dots(x-x_{n})}{(x_{2}-x_{1})(x_{2}-x_{3})\dots(x_{2}-x_{n})}$
$L_{3}(x)=\frac{(x-x_{1})(x-x_{2})\dots(x-x_{n})}{(x_{3}-x_{1})(x_{3}-x_{2})\dots(x_{3-x_{n}})}$
$\dots$
$L_{n}(x)=\frac{(x-x_{1})(x-x_{2})\dots (x-x_{n-1})}{(x_{n}-x_{1})(x_{n}-x_{2})\dots(x_{n}-x_{n-1})}$

- Izračunamo vrsto:
$\displaystyle \sum_{i=1}^n y_{i} . L_{i} = y_{1}.L_{1}+y_{2}.L_{2}+\dots+y_{n}.L_{n}$
$\displaystyle P(x) = \sum_{i=1}^n y_{i}.L_{i}(x)$

**Primer**:
Točke: (1,2), (2,3), (4,1) $\implies n=3$
Zgradimo $L_{1},\dots L_{n}$ ($L_{1},L_{2},L_{3}$):

$L_{1}(x)=\frac{(x-2)(x-4)}{(1-2)(1-4)} = \frac{(x-2)(x-4)}{3}$
$L_{2}(x) = \frac{(x-1)(x-4)}{(2-1)(2-4)} = -\frac{(x-1)(x-4)}{2}$
$L_{3}(x)=\frac{(x-1)(x-2)}{(4-1)(4-2)}=\frac{(x-1)(x-2)}{6}$

Sestavimo $P(x)$:
$P(x)=2 \cdot \frac{x^2-6x+8}{3} + 3\cdot \left( -\frac{x^{2}-5x+4}{2} \right) + \frac{x^{2}-3x+2}{6}=$
$=\frac{4x^{2}-24x+32}{6}-\frac{9x^{2}-45x+36}{6}+\frac{x^{2}-3x+2}{6}=$
$=\frac{-4x^{2}+18x-2}{6}=\frac{-2x^{2}+9x-1}{3}=$


$P(x)=\frac{2}{3}x^{2}+3x-\frac{1}{3}$
## Racionalne funkcije
So funkcije v obliki ulomka: $r(x)=\frac{p(x)}{q(x)}$, kjer sta funkciji $p(x)$ in $q(x)$ polinoma.
- **poli** - x, kjer funkcija ni definirana
- **asimptota** je premica, ki se ji graf racionalne funkcije približuje, a je nikoli ne doseže.
- $D_{f} = \mathbb{R} \textbackslash \{\text{ničle imenovalca}\}$
- Pri deljenju polinoma, **kjer je graf ostanka deljenja = 0, graf racionalne funkcije seka asimptoto**.

| Lastnost  | Način                                                                                                                                                                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ničle     | ničle števca                                                                                                                                                                                                                                       |
| poli      | ničle imenovalca                                                                                                                                                                                                                                   |
| asimptota | $n=\text{deg}(p),m=\text{deg}(q)$:<br>- če $n<m \implies y=0$<br>- če $n=m \implies y=\frac{\text{vodilni koeficient števca}}{\text{vodilni koeficient imenovalca}}$<br>- če $n=m+1$ - delimo polinoma<br>- če $n > m+1$ - brez linearne asimptote |
V ničlah sode stopnje graf ohrani predznak (se x-osi le dotakne), v ničlah lihe stopnje pa graf spremeni predznak (x-os preseže). Podobno velja tudi za pole sodih in lihih stopenj.
### Ne-okrajšane racionalne funkcije
Če se zgodi, da je ničla racionalne funkcije hkrati tudi pol, potem je racionalna funkcija zapisana v **ne-okrajšani obliki**.
## Eksponentna funkcija
