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

---
# Domača naloga, 7. teden
1. Ali drži enakost $C + (A\cap B) = (C\textbackslash (A\cup B)) \cap/(A\cap B\cap C)$?

```spoiler-markdown
![[Drawing 2025-11-18 09.27.03.excalidraw]]
```

2. Ali velja enakost $((A+B)\textbackslash C)\cup(A\cap B\cap C) = ((A\cup B)\textbackslash C)+(A\cup B)$?

```spoiler-markdown
![[Drawing 2025-11-18 09.41.30.excalidraw]]
```

3. Koliko elementov ima množica $P(P(\{1,2\}))$.

```spoiler-markdown
$|P(P({1,2}))| = 2^2^2 = 16$
```

---

# Kolokvij1
1. Trimestni izjavni veznik A je definiran z opisom $A(p,q,r)\equiv(p \implies q)\vee r$, zaporedje izjavnih izrazov pa definiramo z začetnima členoma $A_{1}=q\implies p,A_{2}=p\land \neg q$ in pri $n\ge 3$ z rekurzivno zvezo $A_{n}=A(A_{n-2},p,A_{n-1})$.
	- Izračunaj prvih šest členov zaporedja ($A_{i},i\in \mathbb{N}$)
	- Pokaži, da za vsako naravno število $k\ge 1$ velja trditev: Če sta člena $A_{k}$ in $A_{k+1}$ tavtologiji, potem sta tudi člena $A_{k+1}$ in $A_{k+2}$ tavtologiji.
	- S pomočjo indukcije izračunaj $A_{2024}$

```spoiler-markdown
![[Drawing 2025-11-23 08.09.54.excalidraw]]
```

2. Dan je sklep 
	 $\neg r\vee p,r\vee s,s\implies \neg p,q\vee(r\implies s)\models p\implies q$. Preveri ali je sklep pravilen in zapiši formalen dokaz tega sklepa. Ali sklep ostane pravilen, če zaključek $p \implies q$ zamenjamo s $p\vee q$? Zakaj?

```spoiler-markdown

```

3. V področju pogovora živalskih vrst uporabimo predikate $R,A,H$ z naslednjimi pomeni: $A(x) \dots x$ živi v Afriki, R(x) ... x ima rep, H(x,y) ... x je hitrejši od y.
	Tako R(lev) formalizira izjavo "Lev ima rep."
	Izjavo "x je hitrejši od slona." pa formaliziramo s formulo H(x, slon).
	Formaliziraj naslednje izjave. Pri tem smiselno definiraj potrebne manjkajoče predikate.
	- Nekatere živali nimajo repa.
	- Vsaka afriška žival zna plavati.
	- Nekatere afriške živali nimajo repa in ne znajo plavati.
	- Slon je najhitrejša žival.
	- Najhitrejša žival živi v Afriki in zna plavati.

```spoiler-markdown
$\exists x \neg R(x)$
$\forall x(A(x)\implies P(x))$
$\exists x(A(x) \land\neg R(x)\land \neg P(x))$
$\forall xH(slon,x)$
$\forall x(\forall yH(x,y)\implies A(x)\land P(x))$
ali
$\exists x(\forall y H(x,y)\land A(x)\land P(x))$

```

4. Naj bodo A,B in C poljubne množice. Opazujemo množice:
	- $U = A+B+C$
	- $V=(A\cup B\cup C)\textbackslash (A\cap B\cap C)$
	- $W=(A+B)\cup(B+C)\cup(C+A)$
	1. Utemelji, da sta množici V in W enaki.
	2. Pokaži, da v splošnem ne velja vsebovanost $U \subseteq V$. Ravno tako pokaži, dae v splošnem ne velja vsebovanost $W \subseteq U$.

```spoiler-markdown
![[Drawing 2025-11-23 08.09.54.excalidraw]]
```

# Kolokvij2
1. V vasi Žogobrc živijo sami navdušeni športniki. Nekega dne je v vas prišel novinar in tri mimoidoče vprašal, če so se uvrstili v državno nogometno reprezentanco. 
	A: Če jaz nisem v reprezentanci, v njej tudi ni B.
	B: Vsi trije smo v reprezentanci.
	C: Poleg mene je v reprezentanci še vsaj eden od A in B.
	- Kdo med njimi je zagotovo reprezentant, če veš, da reprezentanti vedno govorijo resnico, ostali pa zaradi nevoščljivosti vedno lažejo?
	- Novinar je izvedel, da je med njegovimi sogovorniki sodo mnogo reprezentantov. Ali mu lahko pomagaš ugotoviti kdo je v reprezentanci in kdo ne?

```spoiler-markdown
![[Drawing 2025-11-23 16.22.17.excalidraw]]
```

2. Ali je naslednji sklep pravilen?
	$p \land q\implies r,q\vee r,\neg p\land q\implies s\land r \models r$
	Poišči protiprimer oz. dokaži s pomočjo pravil sklepanja.

```spoiler-markdown
![[Drawing 2025-11-23 17.07.21.excalidraw]]
```

3. V oddaljeni deželi sta Zgornja in Spodnja vas.
	- Zapiši izjavo: A: "Janez ima prijatelja v Zgornji vasi." s pomočjo predikatne formule. Določi področje pogovora in predikate.
	- Zapiši negacijo izjave A kot izjavo in kot predikatno formulo.
	- Zapiši izjave s pomočjo predikatnih formul v Preneseni normalni obliki. 
		- B: “Nekdo iz Spodnje vasi je prijatelj z vsemi iz Zgornje vasi.”
		- C: “Vsakdo iz Spodnje vasi je prijatelj z nekom iz Zgornje vasi.”
		- D: “ Če je kdo iz Spodnje prijatelj z vsemi iz Zgornje vasi, potem imajo vsi iz Spodnje vasi prijatelja v Zgornji vasi.”

```spoiler-markdown
![[Drawing 2025-11-23 17.27.45.excalidraw]]
```

4. Pokaži, da za poljubne množice A, B in C velja
	$(A+B)\textbackslash C \subseteq B \textbackslash (A+B) \cup A\textbackslash (B\cup C)$.
	Naj bosta zdaj A in B disjunktni. Pokaži, da velja enakost:
	$(A+B)\textbackslash C = B \textbackslash (A+C) \cup A \textbackslash (B \cup C)$

```spoiler-markdown
![[Drawing 2025-11-23 18.04.08.excalidraw]]
```

# Kolokvij3
1. Odgovori na vprašanja:
	- Katere logične vrednosti ohranjata izjavna veznika implikacija in ekskluzivna disjunkcija: $\implies$ in $\veebar$?
	- Izrazi konjunkcijo $p \land q$ samo z uporabo zgornjih dveh izjavnih veznikov.
	- Ali je $\{\implies,\veebar\}$ poln nabor izjavnih veznikov?

```spoiler-markdown
![[Drawing 2025-11-24 13.15.56.excalidraw]]
```

2. Ali je pravilen naslednji sklep:
	$r \vee \neg t\implies p\land s, p\vee u,(r\land t)\vee u \models\neg p \implies u$?
	Ali ostane sklep pravilen tudi, če odstranimo predpostavko $p\vee u$?

```spoiler-markdown
![[Drawing 2025-11-24 13.38.25.excalidraw]]
```

3. Ugotovi ali so naslednji izjavni izrazi med seboj enakovredni:
	- $(\forall x\neg P(x)\implies \neg \exists yR(y))\implies \exists xP(x)$ in $\exists (P(x)\land R(x))$
	- $(\forall x\neg P(x)\implies \neg \exists yR(y))\implies \exists xP(x)$ in $\exists x(P(x)\vee R(x))$

```spoiler-markdown
```

4. Naj bodo A,B in C poljubne množice. Ali velja:
	- enakost: $(B\textbackslash C)\cup(A\cap C)\textbackslash B=(A\cup B)\cap(C\cup B)$
	- vsebovanost: $(B\textbackslash C)\cup(A\cap C)\textbackslash B\subseteq(A\cup B)\cap(C\cup B)$

```spoiler-markdown
![[Drawing 2025-11-24 14.03.58.excalidraw]]
```

# Kolokvij4

1. Dokaži veljavnost naslednjega sklepa:
	$\neg t\vee s,q\implies t,r\vee \neg s\implies \neg p\models p \land q\implies \neg r\land t$

```spoiler-markdown
![[Drawing 2025-11-24 14.35.38.excalidraw]]
```

2. Katere izjavne formule so paroma enakovredne in katere ne? Natančno utemelji!
	- $\forall y\exists x(P(x)\vee \neg Q(y))$
	- $\forall y(\exists x\neg P(x)\vee Q(y))$
	- $\exists x(P(x)\implies \forall yQ(y))$
	- $\exists y(P(y)\vee \forall x\neg Q(x))$

```spoiler-markdown
![[Drawing 2025-11-24 15.22.46.excalidraw]]
```

3. Spodnji enakosti dokaži ali pa ju ovrzi, tako da poiščeš protiprimer.
	- $(A+B)\cup(A\cup B)^{c}=(A\cap B)^{c}$
	- $A\cap B\cap C = (A\cap B)+((A\cup B)\textbackslash C)$

```spoiler-markdown
![[Drawing 2025-11-24 15.33.52.excalidraw]]
```

4. V družini množic definiramo dvomestno operacijo $\triangleleft$ s predpisom $A \triangleleft B := A \cup B^{c}$.
	- Poenostavi izraza: $((A\triangleleft B) \cap A) \triangleleft B$ in $((((A \triangleleft B)\cap A)\triangleleft B)\cap A)\triangleleft B$.
	- Izračunaj $((A \triangleleft B) \triangleleft C) \triangleleft A$
	- Odloči, pod katerimi pogoji velja enakost $A \triangleleft B = B \triangleleft A$.

```spoiler-markdown
![[Drawing 2025-11-24 15.54.19.excalidraw]]
```

# Kolokvij5

1. Poišči tak izjavni izraz X, odvisen le od p,r in s, da bo naslednji izraz protislovje:
	$\neg p\land(X\implies(r\vee s))\Longleftrightarrow ((r\land s)\veebar X)$

```spoiler-markdown
![[Drawing 2025-11-24 16.10.04.excalidraw]]
```

2. Če je spodnji sklep pravilen, zapiši njegov dokaz:
	$p\land q\implies \neg t,s\vee t,q\land r \models p \implies r \land s$
	Preveri še, da je sklep napačen, če predpostavko $q \land r$ zamenjamo s q.

```spoiler-markdown
![[Drawing 2025-11-24 16.45.42.excalidraw]]
```

3. Ali sta formuli $\neg \exists x(\forall y\neg Q(x,y)\land P(x))$ in $\exists y\forall x(P(x)\implies Q(x,y))$ enakovredni? Če sta, to pokaži, sicer pa poišči protiprimer.

```spoiler-markdown
![[Drawing 2025-11-24 17.04.54.excalidraw]]
```

4. Naj za množici C in D velja zveza $C \subseteq D$. Katere od naslednjih vsebovanosti veljajo pri poljubnih množicah A in B? Pokaži oziroma poišči ustrezne protiprimere.
	- $A \cap C \subseteq A \cap D$
	- $A+C\subseteq A+D$
	- $A\cup(B\cap C)\subseteq A\cup(B\cap D)$
	- $(A\cap B)\textbackslash C\subseteq(A\cap B)\textbackslash D$
	- $A\textbackslash (B+C)\subseteq A\textbackslash (B+D)$

```spoiler-markdown
![[Drawing 2025-11-24 17.11.26.excalidraw]]
```

# Kolokvij6
1. Izjavni izraz I = I(X) $(p \implies(q\implies r))\implies(X\implies(p\Longleftrightarrow r))$ vsebuje neznani izjavni izraz X.
	- Poišči vsaj tri takšne izjavne izraze X, za katere bo I tavtologija.
	- Ali lahko poiščeš izraz X, za katerega bo I protislovje? Utemelji.

```spoiler-markdown
![[Drawing 2025-11-25 21.20.21.excalidraw]]
```

2. Ali je kateri izmed spodnjih sklepov pravilen?
	- $p \vee (q \land r), \neg s \implies (p \implies t), p\Longleftrightarrow r \models \neg t \implies s$
	- $p \vee(q \land r), \neg s \implies(p \implies t), p \Longleftrightarrow \models t \implies s$

```spoiler-markdown
![[Drawing 2025-11-25 21.49.40.excalidraw]]
```

3. Pokaži, da je unija množic
	$A \textbackslash B, B\cap C^{c}\cap D^{c},C\textbackslash D,D\textbackslash (A\cap C)$ in $A\cap B\cap C\cap D$ enaka množici $A\cup B\cup C\cup D$. Pokaži tudi, da so omejene množice paroma disjunktne, če je $A\cap(C+D)=\emptyset$.

```spoiler-markdown

```

4. Na množici A = {$\land,\vee,\implies,\Longleftrightarrow ,\veebar$} definiramo relacijo R s predpisom aRb ... a ima v pravilnostni tabeli največ toliko enic kot b.
	- Dokaži, da je relacija R refleksivna in tranzitivna
	- Nariši graf relacije $R^{2}$ in določi $R^{+}$

```spoiler-markdown
![[Drawing 2025-11-25 22.05.21.excalidraw]]
```

# Kolokvij7
1. Ali je sklep $(p\land q)\implies(r\vee s), s \vee \neg r \land (\neg q \implies t) \models \neg s \implies (\neg p \vee t)$ pravilen? Kaj pa sklep $(p \land q) \implies(r \vee s), s \vee \neg r \land (\neg q \implies t) \models \neg s \implies (p \vee t)$
```spoiler-markdown

```

# Kolokvij Fijavž 2022
1. Z uporabo matematične indukcije utemelji, da za vsako naravno število n ≥ 1 velja: $\frac{1}{2}+\frac{2}{2^{2}}+\frac{3}{2^{3}}+\dots+\frac{n}{2^{n}}=2-\frac{{n+2}}{2^{n}}$

```spoiler-markdown
![[Drawing 2025-11-26 07.51.55.excalidraw]]
```

2. Trimestni izjavni veznik T je dan z opisom T(p,q,r) ima vrednost 1 natanko tedaj, ko je vrednost r enaka vrednosti p ali vrednosti q.
	- (5 točk) Zapiši resničnostno tabelo za T(p,q,r) in zapiši T(p,q,r) v disjunktivni normalni obliki.
	- Le z uporabo veznika T in logične konstante 0 zapiši izjavna izraza p ⇒ q ter p$\Longleftrightarrow$q.
	- Kateri izmed naborov {T}, $\{T,\implies\}$,$\{T,0\}$,{$T,\neg$} so polni nabori? Zakaj oz. zakaj ne?

```spoiler-markdown
![[Drawing 2025-11-26 08.03.34.excalidraw]]
```

3. Dana sta sklepa
	$\neg q \implies r \land t, r \vee \neg t \implies \neg p \land s \models p \land q$
	$\neg q \implies r \land t, r \vee \neg t \implies \neg p \land s \models p \implies q$
	Ali sta sklepa resnična?

```spoiler-markdown
![[Drawing 2025-11-26 08.34.46.excalidraw]]
```

4. Naj bodo A, B in C poljubne množice. Ali velja enakost:
	- $((B+C)\textbackslash B)\cap A^{c}=C\textbackslash (B\cup A)$
	- $((B+C)\textbackslash B)\cap A^{c}=C\textbackslash (B\cap A)$

```spoiler-markdown
![[Drawing 2025-11-26 08.59.28.excalidraw]]
```

# Kolokvij Fijavž
1. Z uporabo matematične indukcije utemelji, da za vsako naravno število n ≥ 1 velja:
$1^{2}+3^{2}+6^{2}+\dots+(2n-1)^{2} = \frac{{4n^{3}-n}}{3}$

```spoiler-markdown
![[Drawing 2025-11-26 09.18.23.excalidraw]]
```

2. Tromestni izjavni veznik A je definiran kot $A(p,q,r)\equiv p \Longleftrightarrow (\neg q\vee \neg r)$
	- Zapiši resničnostno tabelo za veznik A in zapiši konjunktivno normalno obliko (KNO) izraza A(p,q,r).
	- Kateri izmed naborov {A, 0}, {A,⇒}, {A, V}, {A, A}, {A, 1}, so polni? Odgovore natančno utemelji.

```spoiler-markdown
![[Drawing 2025-11-26 09.30.18.excalidraw]]
```

3. Pravilnost sklepa $p\vee q,q \vee r,r\implies s, \neg(q\land s)\models p$ dokaži s pravili sklepanja.
	- Pokaži, da sta izjavni formuli $\forall x(P(x)\implies Q(x))$ in $\forall xP(x)\implies \exists xQ(x)$ enakovredni. Utemelji z zakoni predikatnega računa.

```spoiler-markdown
![[Drawing 2025-11-26 09.52.11.excalidraw]]
```

4. Naj bodo A,B in C poljubne množice, dokaži:
	- $(A\textbackslash B)\textbackslash C \subseteq A\textbackslash (B\textbackslash C)$
	- $(A\textbackslash B)\textbackslash C = A \textbackslash (B\textbackslash C)$

```spoiler-markdown
![[Drawing 2025-11-26 11.33.27.excalidraw]]
```

# Kolokvij Fijavž 2020
1. Z uporabo matematične indukcije utemelji, da za vsako naravno število n > 0 velja: $4+9+14+19+\dots+(5n-1)=\frac{{n(c+5n)}}{2}$

```spoiler-markdown
![[Drawing 2025-11-26 11.53.35.excalidraw]]
```

2. Dan je sklep $(\neg p\vee q)\implies r,r\implies(s\vee t),\neg s\land \neg u,\neg u\implies \neg t\models p$
	- Dokaži, da je sklep pravilen tako da zapišeš formalen dokaz.
	- Ali ostane sklep pravilen tudi, če prvo predpostavko $(\neg p\vee q)\implies r$ zamenjamo s $(p\land \neg q)\implies r$ ? Ce ostane pravilen, zapiši formalen dokaz, sicer poišči protiprimer.
```spoiler-markdown
![[Drawing 2025-11-26 12.11.40.excalidraw]]
```

3. Dane so izjavne formule
	- A $\equiv \exists xP(x) \implies \forall xR(x)$,
	- B $\equiv \forall x \forall y(P(x)\implies R(y))$,
	- C $\equiv \forall x(P(x)\implies R(x))$
	- Utemelji, da sta formuli A in B enakovredni.
	- Poišči interpretacijo (področje pogovora in pomen predikatov), v kateri imata formuli A in C različni logični vrednosti. Odgovor utemelji!

```spoiler-markdown
![[Drawing 2025-11-26 12.24.37.excalidraw]]
```

4. Ali velja enakost $(A+B)\cap(A+C) = (A\textbackslash (B\cup C))\cup((B\cap C)\textbackslash A)$
	- Utemelji, da množici $(A\times C)\textbackslash (B\times D)$ in $(A\textbackslash B) \times (C\textbackslash D)$ nista nujno enaki.

```spoiler-markdown
![[Drawing 2025-11-26 12.45.08.excalidraw]]
```

# Kolokvij 2019
1. Z uporabo matematične indukcije utemelji, da velja $\displaystyle 1\cdot 2 + 2\cdot 3 + \dots + n(n+1) = \sum_{k=1}^{n}k(k+1)=\frac{1}{3}n(n+1)(n+2)$.
```spoiler-markdown
![[Drawing 2025-11-26 16.51.59.excalidraw]]
```

2. Ali je $\{0,\land\}$ poln nabor izjavnih veznikov? Če je z njim izrazi $a \Longleftrightarrow b$ ter $a\implies b$.
	- Ali je $\{|\}$, kjer je $a|b = \neg(a\land b)$ poln nabor izjavnih veznikov? Če je, z njim izrazi $a \Longleftrightarrow b$ ter $a \implies b$.

```spoiler-markdown
![[Drawing 2025-11-26 17.05.02.excalidraw]]
```

3. Dan je sklep $r \vee t, (p \implies \neg r) \land s, t \land s \implies q \models p \implies q$
	- Dokaži, da je sklep pravilen tako, da zapišeš formalen dokaz.
	- Ali ostane sklep pravilen tudi, če predpostavko ($p \implies \neg r$)$\land s$ zamenjamo s $p \implies \neg r$? Zakaj?

```spoiler-markdown
![[Drawing 2025-11-26 17.36.28.excalidraw]]
```

# Relacije
Relacijo R definiramo na množici A: $R\subseteq A\times A$
- množica urejenih praov
$(a,b)eR \Longleftrightarrow aRb$

Primer:
Na množici $A = \mathbb{N}$ definiramo relacijo $\leq$
$1\leq 2,1 \leq 1, 100 \leq 200$

![[Drawing 2025-11-28 11.23.29.excalidraw|750]]

![[Drawing 2025-11-28 11.59.47.excalidraw|750]]

![[Drawing 2025-11-28 12.18.05.excalidraw|750]]
![[Drawing 2025-11-28 12.30.46.excalidraw|750]]

---

# Domača naloga, 8. teden

1. Kolokvija iz diskretnih struktur se je udeležilo 208 študentov. Na kolokviju dobijo tri naloge.  
  
	Na kolokviju 87 študentov reši prvo, 93 študentov drugo in 104 študentov tretjo nalogo.  
43 študentov reši prvo in drugo, 41 študentov drugo in tretjo in 40 študentov prvo in tretjo nalogo.  
Število študentov, ki niso rešili nobene naloge, je dvakratnik števila študentov, ki so rešili vse tri naloge.  
  
Koliko študentov na kolokviju ni rešilo nobene naloge?

```spoiler-markdown
![[Drawing 2025-11-30 11.42.02.excalidraw]]
```

2. Naj bo:
	- T - naravna število do 100, deljiva s 3,
	- S  - naravna števila do 100, deljiva s 4
	- P - praštevila do 100
	
	Koliko elementov ima množica $p\times(S\cup T\cup P)$

```spoiler-markdown
![[Drawing 2025-11-30 12.03.47.excalidraw]]
```

---

![[Drawing 2025-12-05 11.17.56.excalidraw]]

# Preslikave
$f:A \rightarrow B$
$f:x \mapsto y$
*f injektivna*: $f(x_{1})=f(x_{2})\implies x_{1}=x_{2}$
*f surjektivna*: $Z_{f}=B$
*f bijektivna*: injektivna + surjektivna
**kompozitum**: $(f\circ g)(x) =f(g(x))$

1. Dani sta preslikavi $f,g: \{1,2,3,4,5,6\}\rightarrow \{1,2,3,4,5,6\}$. Slikamo tako: $\displaystyle f:(\begin{align} 1,2,3,4,5,6 \\ 2,6,3,1,4,1\end{align})$, $\displaystyle g:(\begin{align} 1,2,3,4,5,6 \\6,4,6,2,1,3 \end{align})$.

![[Drawing 2025-12-05 11.47.14.excalidraw]]

2. $f:\mathbb{N}\rightarrow \mathbb{Z}$
	$f(0)=1$
	$f(n+1)=\{\begin{align}6-f(n) f(n)\ge 5 \\f(n)^{2}+1, \text{sicer}\end{align}\}$

![[Drawing 2025-12-05 12.06.29.excalidraw]]

3. $f,g:\mathbb{Z}\times \mathbb{Z}\rightarrow \mathbb{Z}\times \mathbb{Z}$
	$f(x,y)=(x+y,x-y)$
	$g(x,y)=(x)$

![[Drawing 2025-12-05 12.17.46.excalidraw]]

5. $f:\mathbb{Z}\times \mathbb{Z}\rightarrow \mathbb{Z}$
	$f(x,y)=2xy-3x$

![[Drawing 2025-12-05 12.35.40.excalidraw]]

---
# Domača naloga, 9. teden

1. Na množici $A = \{1,2,3,4\}$ definiramo relacijo $R = \{(1,2),(2,3),(3,1),(2,4),(4,1)\}$. Relacija $R^{3}$ je refleksivna.

```spoiler-markdown
![[Drawing 2025-12-07 19.26.47.excalidraw]]
```

2. Dve državi sta v relaciji, če mejita ena na drugo. Ali je ta relacija ekvivalenčna?

```spoiler-markdown
ne, ker država ne more mejiti sama s sabo
```

3. Na množici prvih 12 naravnih števil definiramo relacijo R s predpisom $aRb \Longleftrightarrow \text{MOD}(ab,a+b+1)=3$
- Ali je relacija R refleksivna?
- Ali je relacija R simetrična?
- Ali je relacija R tranzitivna?

- Ali je relacija $R^{2}$ refleksivna?
- Ali je relacija $R^{2}$ simetrična?
- Ali je relacija $R^{2}$ tranzitivna?

```spoiler-markdown
![[Drawing 2025-12-07 19.37.20.excalidraw]]
```

1. Naloga:
- Naštej vsaj 4 lastnosti, ki so skupne vsem 3 grafom.
- Ali je kateri od teh grafov dvodelen?
- Za vsak par ugotovi ali sta izomorfna ali ne?

![[Drawing 2025-12-19 11.21.59.excalidraw]]

2. $G = (V,E)$, $V = \{1,2,3,4,5,6\}$, $E = \{12,23,34,45,56,16,13,36,46\}$
![[Drawing 2025-12-19 11.41.29.excalidraw]]

3. Je kateri od spodnjih grafov Eulerjev?
![[Drawing 2025-12-19 12.09.24.excalidraw]]

4. Kateri od spodnjih grafov so povezani? Ali je kateri od spodnjih grafov Hamiltonov?
![[Drawing 2025-12-19 12.13.23.excalidraw]]

5. Naloga:
- Za vsak graf ugotovi, če je Hamiltonov.
- Za vsak graf ugotovi, če je dvodelen
![[Drawing 2025-12-19 12.28.41.excalidraw]]

# Domača naloga 13

1. Reši diofantsko enačbo $12x + 21y = 6$. Naj bo $x =x_{0},y=y_{0}$ tista izmed rešitev, pri kateri je $x_{0}$ najmanjše možno celo število. Kaj je $y_{0}$?

```spoiler-markdown
![[Drawing 2026-01-04 13.27.55.excalidraw]]
```

2. Na prenosnem predvajalniku velikosti 8 GB imamo shranjene le datoteke tipov mp3 in wav. Vsaka datoteka tipa wav nam zasede 31 MB, vsaka datoteka tipa mp3 pa 5 MB prostora. Predvajalnik je poln do zadnjega kB. Koliko je najmanjše število datotek, ki jih imamo shranjenih?

```spoiler-markdown
![[Drawing 2026-01-04 13.38.36.excalidraw]]
```

# Kolokvij 2.1
1. Naj bo $A = \{1,2,3,4,5,6,7\}$. Preslikavi $f,g: A\rightarrow A$ sta dani s tabelama:
	$$
f = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 \\
2 & 4 & 6 & 1 & 3 & 1 & 5
\end{pmatrix}
$$
	in
	$$g = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 \\
5 & 6 & 2 & 4 & 1 & 3 & 1
\end{pmatrix}$$
	- Ali je f injektivna? Ali je g surjektivna?
	- S tabelo zapiši $g \circ f$.
	- Poišči $h: A\rightarrow A$, da bo $f \circ h = g$.
	- Ali obstaja injektivna $h: A \rightarrow A$, da je $f \circ h = g$. Če obstaja jo poišči.

```spoiler-markdown
![[Drawing 2025-12-30 09.41.32.excalidraw]]
```

2. Z uporabo razširjenega Evklidovega algoritma poišči največji skupni delitelj števil 24 in 66.
	Poišči splošno rešitev linearne diofantske enačbe $24x + 66y = 522$

```spoiler-markdown
![[Drawing 2025-12-30 10.13.01.excalidraw]]
```

3. Na množici $\mathbb{Z}$ je definirana relacija R s predpisom: $aRb$ natanko tedaj, ko $6|(3a+3b)$
	- Pokaži, da je R ekvivalenčna relacija.
	- Opiši ekvivalenčne razrede relacije R in kvocientno množico $\mathbb{Z}/R$.
	- Denimo, da je relacijo R definiramo na množici $A=\{1,2,3,4,5,6\}$. Pregledno nariši njen graf.

```spoiler-markdown
![[Drawing 2025-12-30 11.53.53.excalidraw]]
```

4. Podana sta grafa.
	![[Pasted image 20251231095353.png]]
	- Ali sta izomorfna? Če sta, poišči izomorfizem med njima. Če nista, pa to dobro utemelji.
	- Ali je kateri od grafov dvodelen? Utemelji.
	- Ali je 2. graf Eulerjev? Če je označi Eulerjev obhod. Če ni, pa to dobro utemelji.
	- Ali je 1. graf Hamiltonov? Če je, nariši kakšen Hamiltonov cikel. Če ni, pa to dokaži z izrekom o razpadu grafa.

```spoiler-markdown
![[Drawing 2025-12-31 09.56.35.excalidraw]]
```

# Kolokvij 2.2

1. Na množici parov naravnih števil $A = \{1,2,3,4,5\}\times \{1,2,3,4,5\}$ definiramo relacijo R na sledeč način: $(a,b)R(c,d)$ natanko tedaj $c-a=d-b=k$, kjer $k \in \{-1,1\}$.
	- Določi vse pare $(c,d)\in A$, za katere velja $(2,3)R(c,d)$.
	- Ali je relacija R refleksivna, simetrična, tranzitivna? Kaj pa relacija $R^{2}$?
	- Utemelji, da je relacija $R^{*}$ ekvivalenčna. Opiši kvocientno množico $A/R^{*}$.

```spoiler-markdown
![[Drawing 2025-12-31 15.56.46.excalidraw]]
```

2. Kolikšna je dolžina najdaljšega cikla v grafih z zaporedjem stopenj točk enakim 3,3,3,3,3,3? Zakaj?

```spoiler-markdown
![[Drawing 2026-01-01 09.54.36.excalidraw]]
```

3. Graf G naj ima množico točk enako $\{1,\dots,12\}$, točki pa sta sosedi natanko tedaj, ko je njuna razlika praštevilo.
	- Čim lepše nariši graf G.
	- Ali je graf G dvodelen? Ali je Eulerjev?
	- Poišči kliko velikosti 4 v grafu G in določi kromatično število grafa G.

```spoiler-markdown
![[Drawing 2026-01-01 11.44.25.excalidraw]]
```

4. Z uporabo razširjenega Evklidovega algoritma poišči največji skupni delitelj števil 60 in 33.
	- Poišči splošno rešitev linearne diofantske enačbe $60x+33y = 120$
	- Ali ima enačba $60x+33y=120$ rešitve v množici naravnih š

  ```spoiler-markdown
  ![[Drawing 2026-01-01 11.59.39.excalidraw]]
  ```

# Kolokvij 2.3

1. Šola je priredila športno tekmovanje v troskoku, skoku v daljino in teku na 100 metrov. Nanj se je prijavilo 130 tekmovalcev. Od tega se jih je 75 prijavilo za tek in 40 za skok v daljino. V teku in troskoku bo tekmovalo 17 tekmovalcev, v teku in skoku v daljino 15 tekmovalcev in v troskoku in skoku v daljino 18 tekmovalcev. V vseh treh disciplinah bo tekmovalo 10 tekmovalcev.
	- Koliko tekmovalcev bo tekmovalo v troskoku?
	- Koliko tekmovalcev bo tekmovalo samo v eni disciplini?
	- Koliko tekmovalcev bo tekmovalo v skokih (torej v skoku na daljino in troskoku)?

```spoiler-markdown
![[Drawing 2026-01-02 15.38.57.excalidraw]]
```

2. Podan imamo graf.
	- Ali je Eulerjev?
	- Poišči njegovo kromatično število.
	- Ali je graf Hamiltonov? Če je, nariši kakšen Hamiltonov cikel, če ni pa to dokaži z izrekom o razpadu grafa.
	![[Pasted image 20260102155707.png]]

```spoiler-markdown
![[Drawing 2026-01-02 15.57.15.excalidraw]]
```

3. Dani so spodnji grafi. Za vsak par izmed njih preveri, če sta grafa izomorfna. Utemelji.
![[Pasted image 20260102160804.png]]

```spoiler-markdown
![[Drawing 2026-01-02 16.07.37.excalidraw]]
```

4. Na množici naravnih števil od 1 do 8 je podana relacija R s predpisom $aRb$ natanko tedaj, ko je $2a + b$ večkratnik števila 3.
	- Nariši graf relacije $R$.
	- Pokaži, da je $R$ ekvivalenčna relacija.
	- Poišči ekvivalenčni razred, v katerem je število 3.

```spoiler-markdown
![[Drawing 2026-01-02 16.14.13.excalidraw]]
```