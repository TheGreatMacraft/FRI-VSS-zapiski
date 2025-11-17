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

4. Zaporedje Fibonaccijevih števil $(f_n)_{n \in N}$ je definirano z začetnima členoma, $f_0 = 0, f_1 = 1$, in rekurzivno zvezo $f_n = f_{n−1} + f_{n−2}$ za $n \ge 2$. S pomočjo matematične indukcije dokaži, da je za vsak n število $f_{4n}$ deljivo s 3. #NeZnam
```spoiler-markdown

```

5. V danem izjavnem izrazu z oklepaji nakažite vrstni red računanja (glede na prednost izjavnih veznikov):
- $\neg A \vee B \vee C \Longleftrightarrow \neg B \Longleftrightarrow A \land B$
- $A \implies B \implies C \implies \neg A \Longleftrightarrow \neg B$
- $\neg B \Leftrightarrow A \implies C \implies \neg B \land C \vee A$
```spoiler-markdown
![[Drawing 2025-10-18 12.55.34.excalidraw]]
```

6. Določi logične vrednosti enostavnih izjav p,q, r, s, nato pa še logične vrednosti iz njih dobljenih sestavljenih izjav A, B, C.

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
![[Drawing 2025-10-17 08.11.56.excalidraw|1500]]
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
![[Drawing 2025-10-18 11.40.08.excalidraw]]
```
- Ali sta izraza $\neg p \land (r \Longleftrightarrow q)$ in $(p \vee r \vee q) \implies (p \land r \land \neg q)$ enakovredna?
```spoiler-markdown
![[Drawing 2025-10-18 12.11.57.excalidraw]]
```
- Ali sta izraza $\neg p \land (r \Longleftrightarrow q)$ in $(p \vee r \vee q) \implies (\neg p \land r \land q)$ enakovredna?
```spoiler-markdown
![[Drawing 2025-10-18 12.21.41.excalidraw]]
```
# Vaje 2. teden

1. Kateri od naslednjih izjavnih izrazov so tavtologije, kateri protislovja in kateri nevtralni?

- $p \implies (\neg q \implies p \land q)$
```spoiler-markdown
![[Drawing 2025-10-17 09.22.19.excalidraw]]
```
- $(p \land q) \implies (p \vee q)$
```spoiler-markdown
![[Drawing 2025-10-17 09.27.07.excalidraw]]
```
- $(p \land q) \Longleftrightarrow \neg p \vee \neg q$
```spoiler-markdown
![[Drawing 2025-10-17 09.31.49.excalidraw]]
```
- $((p \implies q) \land r) \vee (r \implies p)$
```spoiler-markdown
![[Drawing 2025-10-20 11.43.37.excalidraw]]
```
- $(q \implies p \land r) \land (p \vee r \implies q)$
```spoiler-markdown
![[Drawing 2025-10-20 12.03.17.excalidraw]]
```
- $(p \implies q) \implies r$
```spoiler-markdown
![[Drawing 2025-10-20 12.07.46.excalidraw]]
```

2. Ali so naslednji izjavni izrazi enakovredni?
- $p \implies \neg q$ in $q \implies \neg p$
```spoiler-markdown
![[Drawing 2025-10-20 12.11.01.excalidraw]]
```
- $(p \land \neg q) \implies r$ in $\neg p \land q \land r$
```spoiler-markdown
![[Drawing 2025-10-17 09.36.59.excalidraw]]
```
- $p \implies (q \vee r)$ in $\neg p \vee q \vee r$
  ```spoiler-markdown
  ![[Drawing 2025-10-20 12.12.42.excalidraw]]
  ```
  - $(p \implies \neg q) \land (\neg q \implies p)$ in $(\neg p \land q) \vee (p \vee \neg q)$
```spoiler-markdown
![[Drawing 2025-10-17 09.49.58.excalidraw]]
```

3. Poenostavi naslednje izraze:
- $\neg (p \land q) \implies p \land r$
```spoiler-markdown
![[Drawing 2025-10-17 09.55.04.excalidraw]]
```
- $p \implies (q \implies p)$
```spoiler-markdown
![[Drawing 2025-10-17 09.56.49.excalidraw]]
```
- $(p \implies q) \implies (\neg q \implies \neg p)$
```spoiler-markdown
![[Drawing 2025-10-17 09.58.56.excalidraw]]
```
- $\neg p \implies (p \vee q)$
```spoiler-markdown
![[Drawing 2025-10-17 10.01.08.excalidraw]]
```

4. Poišči tak izjavni izraz X, da bosta izraza $(p \implies X) \land (q \implies X)$ in $\neg p \implies (X \implies q)$ tavtologiji
```spoiler-markdown
![[Drawing 2025-10-17 10.04.21.excalidraw]]
```
5. Ali obstaja kak izjavni izraz X, za katerega sta izraza $(p \land X) \vee (q \land \neg X)$ in $(p \implies X) \implies q$ enakovredna?

```spoiler-markdown
![[Drawing 2025-10-17 10.10.14.excalidraw]]
```

6. Preoblikuj pare izjavnih izrazov v DNO oziroma KNO, nato pa ugotovi, ali so enakovredni.
- $(p \implies q) \land (r \implies q)$ in $(p \vee r) \implies q$
```spoiler-markdown
![[Drawing 2025-10-17 10.33.13.excalidraw]]
```
- $p \vee (p \veebar \neg q)$ in $q \implies p$
```spoiler-markdown
![[Drawing 2025-10-17 10.37.52.excalidraw]]
```

# Vaje 3. teden

1. Kateri izmed naslednjih naborov so polni?
- {$\implies, \neg$}
```spoiler-markdown
![[Drawing 2025-10-24 11.32.53.excalidraw]]
```
- {$\implies,0$}
```spoiler-markdown
![[Drawing 2025-10-24 11.39.35.excalidraw]]
```
- {$\implies,1$}
```spoiler-markdown
![[Drawing 2025-10-24 11.44.23.excalidraw]]
```
- {$\implies, \land$}
```spoiler-markdown
![[Drawing 2025-10-24 11.46.16.excalidraw]]
```
- {$\implies \centernot \implies$}
```spoiler-markdown
![[Drawing 2025-10-24 11.48.55.excalidraw]]
```

2. Naj bo w trimestni veznik $W(p,q,r) = (p\vee q) \implies r$
Kateri so polni?
- {W}
- {W,1}
- {W,0}
```spoiler-markdown
![[Drawing 2025-10-24 11.55.24.excalidraw]]
```

3. Zaporedje izjavnih izrazov $B_n$ je definirano rekurzivno: 
$B_0 = \neg p$
$B_1 = \neg q$
$B_2 = W(p,q,B_{n-1}\land B_{n-2})$
```spoiler-markdown
![[Drawing 2025-10-24 12.07.41.excalidraw]]
```

4. Kateri od naslednjih sklepov so pravilni?
- $p \land r$, $q \land p \implies \neg r$, sklep: $\neg q$
```spoiler-markdown
![[Drawing 2025-10-24 12.23.59.excalidraw]]
```
- $p \vee q$, $\neg q \land r \implies \neg p$, sklep: $q \vee r$
```spoiler-markdown
![[Drawing 2025-10-24 12.32.05.excalidraw]]
```
 - $p \implies q$, $r \implies s$, $p \vee r$, sklep $q \land s$
```spoiler-markdown
![[Drawing 2025-10-24 12.35.39.excalidraw]]
```
 - $p \implies q$, $p \vee s$, $q \implies r$, $s \implies t$, $\neg r$, sklep: $t$
```spoiler-markdown
![[Drawing 2025-10-24 12.39.31.excalidraw]]
```

# 4. Domača naloga
1. Tromestni veznik A je definiran s predpisom $A(p,q,r) = P \vee (\neg q \land \neg r)$. Ali je nabor veznikov poln?
- {A}
- {$A,\neg$}
- {$A,1$}
- {A,0}
- {A,$\veebar$}
```spoiler-markdown
![[Drawing 2025-10-28 09.58.11.excalidraw]]
```

2. Veznik A je definiran z $A(p,q,r) = \neg p \land \neg q \land \neg r$. Izrani $A_i i=0,1,...,$ so definirani rekurzivno z:
- $A_0 = 0$
- $A_1 = p$
- $A_2 = q$
- $A_N = A(A_{n-1},A_{n-2},A_{n-3})$ za n = 3,4,...
Izračunaj $A_2004$.
```spoiler-markdown
![[Drawing 2025-10-28 10.40.32.excalidraw]]
```

# 5. Teden Vaje

1. Preveri pravilnost sklepov s pomočjo dokaza s protislovjem.
- $(p \implies q) \land (r \implies s )$, $s \land q  \implies t$, $\neg t \models \neg(p \land r)$
```spoiler-markdown
![[Drawing 2025-10-28 15.21.03.excalidraw]]
```
- $p \vee q, p \implies r, q \implies s \models r \vee s$
```spoiler-markdown
![[Drawing 2025-10-28 15.34.24.excalidraw]]
```
- $p \implies r \land t, t \vee s \implies \neg q \models \neg (p\land q)$
```spoiler-markdown
![[Drawing 2025-10-28 15.44.01.excalidraw]]
```

2. Preveri pravilnost sklepa s pomočjo pogojnega sklepa.
- $p \implies (q \vee r), \not r \models p \implies q$
```spoiler-markdown
![[Drawing 2025-10-28 16.16.47.excalidraw]]
```
- $p \vee q \implies r \land s, r \vee t \implies u \models p \implies u$
```spoiler-markdown
![[Drawing 2025-10-28 16.21.20.excalidraw]]
```
3. Za področje pogovora izberemo naravna števila. Enomestni predikat P in dvomestni predikat D interpretiramo kot:
	P(x) : x je praštevilo,
	D(x,y) : število x deli število y.
	Zapiši interpretacije in določi logične vrednosti spodnjih izjavnih formul. Zapiši še negacije teh izjavnih formul.
- $\forall x (P(x) \vee D(2,x))$
```spoiler-markdown
Vsako naravno število je praštevilo ali pa večkratnik števila 2.
```
- $\exists x (P(x) \land D(2,x))$
```spoiler-markdown
Obstaja naravno število, ki je praštevilo in večkatnik števila 2.
```
- $\exists x (P(x) \land D(5,x))$
```spoiler-markdown
Obstaja naravno število x, ki je praštevilo in večkratnik števila 5
```
- $\forall x (P(x) \implies \neg D(10,x))$
```spoiler-markdown
Za vsako naravno število velja: če je praštevilo, potem ni deljivo.
```
- $\forall x \exists y D(x,y)$
```spoiler-markdown
Za vsako naravno število x, obstaja naravno število y, tako da x deli y.
Negacija: $\exists x \forall y \neg D(x,y) \sim 1$
```
- $\exists x \forall y (D(x,y) \implies \neg P(y))$
```spoiler-markdown
Obstaja naravno število x, da za vsako naravno število y velja, da če x deli y, potem y ni praštevilo.

Negacija: $\forall x \exists y (\neg (D(x,y) \implies \neg P(y)))$
```
4. Poišči interpretacije v katerih imajo naslednji pari izjavnih formul nasprotne logični vrednosti.
- $\forall x (P(x) \implies R(x)), \exists x (P(x) \implies R(x))$
```spoiler-markdown
![[Drawing 2025-10-28 16.34.35.excalidraw]]
```

# Kviz po predavanjih v 5. tednu
1. Katera izmed naslednjih formul je resnična v vsaki interpretaciji?
- $\forall x (P(x) \land Q(x)) \implies \forall x P(x) \land \forall x Q(x)$
- $\forall x (P(x) \land Q(x)) \implies \exists x P(x) \vee \exists x Q(x)$
- $\exists x (P(x) \land Q(x)) \implies \forall x P(x) \land \forall x Q(x)$
- $\forall x (P(x) \vee Q(x)) \implies \exists x P(x) \land \exists x Q(x)$

```spoiler-markdown
1.
```
2. Za množice A={1,2,3}, B={3,4,5} in C={5,6} določi, katere izmed naslednjih zvez veljajo:
- A in B sta disjunktni
- A in C sta disjunktni
- $A \cap B \cap C = \emptyset$
- $B \subseteq A \cup C$
- $A \cup B \subseteq A \cup C$
- $A \cup B \subset B + C$
- $A + B \subseteq A \cup C$
- $A^c \cap B \subseteq A \cup C$
```spoiler-markdown
2,3,6,7
```
3. Naj bodo A,B,C poljubne množice. Katere od naslednjih enakosti z množicami držijo in zakaj?
 - $B \cup (B \cap C) = C$
 - $A + (B \cup C) = (A + B) \cup (A+C)$
 - $C \cap (B \cup A) = (C \cap B) \cup (C \cap A)$
 - $A \cap B \cap A = A$
 - $B + (A \cap C) = (B + A) \cap (B + C)$
 - $B \cap (A + C) = (B \cap A) + (B \cap C)$
 - $C \cap B \cap C = B \cap C$
 - $C \cup (C \cap A) = C$
 ```spoiler-markdown
 3,7,8
 ```
# Domača naloga, 5. teden
1. Ali je sklep $\neg p \implies q \implies \neg r$, $\neg q \vee (p \implies r)$, $(\neg q \vee s) \Leftrightarrow (r \implies p) \models p \vee q \land r$
```spoiler-markdown
![[Drawing 2025-11-04 09.39.36.excalidraw]]
```
2. Koliko je protiprimerov za sklep $t \vee p \vee u, s \vee \neg t \vee s, u \land (\neg t \vee s) \models \neg r \vee q$?
```spoiler-markdown
![[Drawing 2025-11-05 10.24.54.excalidraw]]
```
3. Področje pogovora so planeti. $Z(x)$ pomeni, da je planet x podoben Zemlji, $Ž(x)$ pa pomeni, da ima planet x življenje. Napiši ustrezno interpretacijo naslednjih izjav.
- $\forall x Z(x) \vee \forall x Ž(x)$
- $\neg \forall (Z(x) \vee Ž(x))$
- $\forall x (Ž(x) \implies Z(x))$
- $\forall x Z(x) \vee \forall x \neg Z(x)$
- $\forall x (Z(x) \vee \neg Z(x))$
```spoiler-markdown
1. Vsi planeti so podobni zemlji, ali pa imajo vsi planeti življenje.
2. Obstaja tak planet, ki ni podoben zemlji in nima življenja.
3. Vsak planet, ki ima življenje, je podoben zemlji.
4. Vsi planeti so podobni zemlji ali pa noben planet ni podoben zemlji.
5. Za vsak planet velja, da je podoben zemlji ali pa ni podoben zemlji.
```
# Domača naloga, 6. teden
1. Naj A(x) pomeni, da je x astronavt, naj P(x) pomeni, da je x planet in naj V(x,y) pomeni, da bo x potoval na y.
	Zapiši simboličen zapis izjave: **Nobenega planeta ne bodo obiskali vsi astronavti.**
```spoiler-markdown
$\forall x(P(x) \implies \exists y(A(y) \land \neg V(y,x))$
```
2. Ali so naslednji izrazi paroma enakovredni?
- $\exists x(P(x) \land Q(w))$ in $\exists x P(x) \land Q(w)$
- $\forall x \exists z P(x,z)$ in $\exists x \forall z P(x,z)$
- $\forall x P(x)$ in $\forall z P(z)$
- $\forall x P(t)$ in $\exists x P(z)$
- $\forall x (P(x) \land Q(x))$ in $\forall x P(x) \land \forall x Q(x)$
```spoiler-markdown
1. DA
2. NE
3. DA
4. NE
5. DA
```

# Kviz po predavanjih v 6. tednu
1. Definirajmo množice:
- N = {0,1,2,3,...} množica naravnih števil
- S = {0,2,4,6,...} množica sodih števil
- L = {1,3,5,7,...} množica lihih števil
- P = {2,3,5,7,...} množica praštevil
- Q = {0,1,4,9,...} množica popolnih kvadratov
in operaciji množenja množice s številom in prištevanja števil k množici: 
če je $k \in N$ in $A=\{a_1,a_2,a_3,...\} \subseteq N$, potem je $kA = \{ka_1,ka_2,ka_3,...\}$ in $k + A = \{k+a_1,k+a_2,k+a_3,...\}$

Tj. kA je množica, ki jo dobimo tako, da vse elemente množice A pomnožimo s k. k+A pa dobimo, če vsem elementom množice A prištejemo k.

Katere od naslednjih trditev držijo?
- {S,L} je pokritje množice N.
- {i + S; $i \in L$} je pokritje množice N.
- {i + L; $i \in L$} je pokritje množice N.
- {iL; $i \in L$} je pokritje množice N.
- {iS; $i \in L$}  je pokritje množice N.
- {$2^iL$; $i \in L$}  je pokritje množice N.
- {$2^iL$; $i \in N$}  je pokritje množice N.
- {$2^iN$; $i \in N$}  je pokritje množice N.
- {$2^iP$; $i \in N$}  je pokritje množice N.
- {iP; $i \in P$}  je pokritje množice N \ {0,1}.
- {iQ; $i \in Q$}  je pokritje množice Q.
- {iP; $i \in Q$}  je pokritje množice L.
- {iQ; $i \in N$}  je pokritje množice N.
- {S,L}  je razbitje množice N.
- {2^iL;i \in N} je razbitje množice N \ {0}.

2. Za množice A,B,C velja |A| = 7, |B| = 4, |C| = 4, |$A \cap B$| = 2, |$A \cap C$|= 3 in |$B \cap C$| = 1. Kolikšna je moč množice $A \cap B \cap C$, če veš, da je |$A \cup B \cup C$| = 10

```spoiler-markdown
10 = 7+4+4-2-3-1+x
10 = 15-6 + x
10 = 9 + x
1 = x

Odgovor: $|A \cap B \cap C| = 1$
```

3. Množice A,B,C imajo vse po 6 elementov. Poleg tega je $|A \cap B|$ = 4, $|A \cap C|$ = 5 in |$A \cap B \cap C$| = 2. Določi moč množice $(B \cap C)$ \ A.

```spoiler-markdown
Podatki niso OK.
![[Drawing 2025-11-10 14.14.26.excalidraw]]
```

4. Za množice A,B,C velja $|A \cap B|$ = 2, $|A \cap C|$ = 3 in $|B \cap C|$ = 1. Kolikšno je najmanjše možno število elementov v množici $A \cup B \cup C$, če veš, da so množice A,B,C enakih moči?

```spoiler-markdown

```

5. Za množice A,B,C velja |$A\cap C$| = 3, $|A \cap C|$ = 3 in $|B \cap C| = 1$. Kolikšno je najmanjše možno število elementov v množici $A \cup B \cup C$, če veš, da so množice A,B,C samih **različnih moči**?

```spoiler-markdown

```

---

2. Določi množice:
- $\emptyset \cap \{\emptyset\}$
- $\{\emptyset\} \cap \{\emptyset\}$
- $\{\emptyset,\{\emptyset\}\}$ \ $\{\emptyset\}$
```spoiler-markdown
![[Drawing 2025-11-11 17.12.27.excalidraw]]
```

3. Ali veljajo naslednje enakosti oz. vsebovanosti z množicami? Dokaži ali pa poišči protiprimer.
- $((A \cap B ) \cup (C \cap D))^c = (A^c \cup B^c) \cap (C^c \cup D^c)$
- $((A \cup B) \cap (A \cup B^c)) \cup ((A^c \cup B) \cap (A^c \cup B^c)) = S$
- (A ∪ B) ∩ (A ∪ $B^c$ ) ∩ ($A^c$ ∪ B) ∩ ($A^c$ ∪ $B^c$ ) = ∅
- A \ (A \ (B \ (B \ C))) = A ∩ B ∩ C
- A \ (B ∪ C) = (A \ B) ∩ (A \ C)
- A ∪ (B + C) = (A ∪ B) + (A ∪ C)
- (A ∩ B) \ C ⊆ (A ∪ C) ∩ B
- (A + B) \ A = B \ A
- (A + B) + (A + C) = A + (B + C)
- A + B ⊆ A + (B + C)

```spoiler-markdown
![[Drawing 2025-11-11 17.17.56.excalidraw]]
```

4. Ali velja enakost (B \ C) ∪ (A ∩ C) \ B = (A ∪ B) ∩ (C ∪ B)? Kaj pa vsebovanost (B \ C) ∪ (A ∩ C) \ B ⊆ (A ∪ B) ∩ (C ∪ B)?

```spoiler-markdown
![[Drawing 2025-11-11 18.33.17.excalidraw]]
```