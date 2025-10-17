1. Nariši resničnostno tabelo izjavnega izraza $(p \implies q) \vee (\neg q \implies p)$.
Pomoč: [[diskretne strukture/Zapiski#Resničnostna tabela|Resničnostna tabela]]

Rešitev:
```spoiler-markdown
![[Drawing 2025-10-08 15.39.24.excalidraw|1500]]
```

2. Preveri ali je izjavni izraz $p \implies (q \implies p)$ tavtologija.
Pomoč: [[diskretne strukture/Zapiski#Resničnostna tabela|Resničnostna tabela]]

Rešitev:
```spoiler-markdown
![[Drawing 2025-10-08 16.41.50.excalidraw|1500]]
```

3. Poišči izjavni izraz s predpisano resničnostno tabelo:

$\begin{array}{c|c} p & q & r & A \\ \hline 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 1 \end{array}$

Pomoč: [[diskretne strukture/Zapiski#Disjunktivna normalna oblika|Disjunktivna normalna oblika]], [[diskretne strukture/Zapiski#Konjunktivna normalna oblika|Konjunktivna normalna oblika]]
```spoiler-markdown
Preverimo, kje je A resničen in v oklepajih zapišemo stanje spremenljivk na teh točkah, ki jih povežemo s konjunkcijo (in). Oklepaje nato med seboj povežemo z disjunkcijo (ali). S tem zapišemo [[diskretne strukture/Zapiski#Disjunktivna normalna oblika|Disjunktivno normalno obliko]].

$A_{DNO} = (\neg p \land \neg q \land r) \vee (\neg p \land q \land r) \vee (p \land \neg q \land \neg r) \vee (p \land \neg q \land r) \vee (p \land q \land r)$

Isto nalogo lahko rešimo s pomočjo [[diskretne strukture/Zapiski#Konjunktivna normalna oblika|Konjunktivne normalne oblike]], tako da preverimo kje A ni resničen in v oklepajih zapišemo stanja spremenljivk na teh točkah, povezana z disjunkcijo (ali), te oklepaje pa nato povežemo s konjunkcijo (in):

$A_{KNO} = (p \vee q \vee r) \land (p \vee \neg q \vee r) \land (\neg p \vee \neg q \vee r)$

```

4. Skrajšaj $(p \vee q \vee r) \land (p \vee \neg q \vee r) \land (\neg p \vee \neg q \vee r)$
Pomoč: [[diskretne strukture/Zapiski#Zakoni izjavnega računa|Zakoni izjavnega računa]]

```spoiler-markdown
![[Drawing 2025-10-08 18.25.33.excalidraw|2500]]
```

# Kviz po predavanjih v 2. tednu

1. Katere operacije (aritmetične, logične) so komutativne?
- seštevanje, konjunkcija, množenje
- implikacija, seštevanje, odštevanje
- konjunkcija, odštevanje, ekvivalenca
- konjunkcija, odštevanje, implikacija

```spoiler-markdown
seštevanje, konjunkcija, množenje
```

2. Kateri pari izjavnih izrazov so enakovredni?
- $\neg p \vee q$ in $q \implies p$
- $p \land \neg q$ in $\neg (q \vee \neg p)$
- $p \implies q$ in $q \implies p$
- $p \land \neg q$ in $\neg (p \implies q)$

```spoiler-markdown
![[Drawing 2025-10-10 13.55.14.excalidraw|3000]]
```

3. Pri koliko naborih logičnih vrednosti za spremenljivke $p,q$ in $r$ ima izraz $p \vee (q \land \neg r)$ logično vrednost 1?

```spoiler-markdown
![[Drawing 2025-10-11 10.30.10.excalidraw|1500]]
```

4. Globina izjavnega izraza je vedno vsaj četrtina dolžine tega istega izraza.

```spoiler-markdown
![[Drawing 2025-10-11 10.39.15.excalidraw|1500]]
```

5. Izjavni izraz $p\land q$ je vsebovan v izjavnem izrazu $p \land q \vee r$, ali to drži?

```spoiler-markdown
![[Drawing 2025-10-11 10.49.15.excalidraw|1500]]
```

6. Izjavni izraz $q \vee r$ je vsebovan v izjavnem izrazu $p \land q \vee r$, ali to drži?

```spoiler-markdown
![[Drawing 2025-10-11 10.49.15.excalidraw 1|1500]]
```

7. Vsi vezniki nabora $\{\vee,\land,\implies,\Longleftrightarrow\}$ ohranjajo isto logično vrednost. Katero?

```spoiler-markdown
![[Drawing 2025-10-11 10.59.17.excalidraw|1500]]
```

8. Vemo, da je nabor logičnih veznikov $\{\vee, \neg\}$ poln. Tudi nabora {$\vee, \Longleftrightarrow, \neg$} in {$\vee,\implies,\neg$} sta polna. Ali to drži?

Namig:
```spoiler-markdown
Če vemo, da je nabor A = $\{\vee, \neg\}$ poln in bi želeli dokazati, da je nabor B = {$\vee, \Longleftrightarrow, \neg$} prav tako poln, moramo vse njegove veznike zapisati samo z vezniki, ki so v naboru A. Če tega ne moremo storiti, nabor ni poln. 
```

```spoiler-markdown
![[Drawing 2025-10-11 11.04.11.excalidraw|1500]]
```

# 2. Domača naloga

1. Za izjavni izraz $J = (p \vee \neg r \implies p \land q) \vee (p \vee q \implies p \vee \neg r)$
```spoiler-markdown
![[Drawing 2025-10-14 17.17.24.excalidraw]]
```

2. Na otoku vitezov in oprod srečamo domačine A,B,C,D in E, ki podajajo naslednje izjave:
- A: "D je vitez ali pa je E oproda."  
- B: "Jaz in E sva različna."  
- C: "Jaz sem vitez ali pa je E oproda."  
- D: "A je vitez ali pa je E vitez."  
- E: "B je oproda ali pa sem jaz vitez."

```spoiler-markdown
![[Drawing 2025-10-14 17.53.13.excalidraw]]
```
# Vaje 2. teden

1. S pomočjo matematične indukcije dokaži, da za vse $n  \in \mathbb{N}$ velja:

- $2+4+6+...+2n = n(n+1)$
```spoiler-markdown
![[Drawing 2025-10-13 09.38.02.excalidraw]]
```

- $1+4+7+...+(3n-2) = \frac{n(3n-1)}{2}$
```spoiler-markdown
![[Drawing 2025-10-13 09.53.01.excalidraw]]
```

- $1*2^1 + 2 * 2^2 + 3 * 2 ^3 + ... + n*2^n = (n-1) * 2^{n+1}  + 2$
```spoiler-markdown
![[Drawing 2025-10-13 10.09.06.excalidraw]]
```

- $1*1!+2*2!+3*3!+...+n*n! = (n+1)!-1$
```spoiler-markdown
![[Drawing 2025-10-13 10.44.36.excalidraw]]
```

2. S pomočjo matematične indukcije dokaži, da za vsako naravno število $n \ge 3$ velja $n! < n^{n-1}$.

```spoiler-markdown
![[Drawing 2025-10-13 10.51.28.excalidraw]]
```

3. S pomočjo matematične indukcije dokaži:

- da je za vsako naravno število $n$ izraz $5 3n+2*11^n$ deljiv s 3.
Nerešeno:
```spoiler-markdown
![[Drawing 2025-10-13 13.01.55.excalidraw]]
```

- da ima vsaka triangulacija konveksnega n-kotnika (brez dodatnih oglišč) natanko $n-2$ trikotnikov.
```spoiler-markdown
![[Drawing 2025-10-13 13.39.45.excalidraw]]
```

4. Zaporedje Fibonaccijevih števil $(f_n)_{n \in N}$ je definirano z začetnima členoma, $f_0 = 0, f_1 = 1$, in rekurzivno zvezo $f_n = f_{n−1} + f_{n−2}$ za $n \ge 2$. S pomočjo matematične indukcije dokaži, da je za vsak n število $f_{4n}$ deljivo s 3.
```spoiler-markdown

```

# 3. Domača naloga

1. Za naslednje izjavne izraze odloči, ali so tavtologije, protislovja ali nevtralni izjavni izrazi.
- $p \Longleftrightarrow \neg p$
```spoiler-markdown
![[Drawing 2025-10-17 07.46.58.excalidraw]]
```
- $(p \implies q) \land (q \implies r)  \implies (p \implies r)$
```spoiler-markdown
![[Drawing 2025-10-17 07.48.54.excalidraw]]
```
- $(p \land q \implies r) \land \neg(p \implies (q \implies r))$
```spoiler-markdown
![[Drawing 2025-10-17 08.11.56.excalidraw]]
```
- $\neg p \implies \neg q$
```spoiler-markdown
![[Drawing 2025-10-17 08.22.40.excalidraw]]
```
- $\neg (p \implies p \land q)$
 ```spoiler-markdown
 ![[Drawing 2025-10-17 08.36.10.excalidraw]]
 ```

2. Izberi pravilen odgovor.
- Ali sta izraza $p \Longleftrightarrow r \vee q$ in $\neg p \vee q \implies ((p \vee r \vee q ) \implies p \land r)$ enakovredna?
```spoiler-markdown

```