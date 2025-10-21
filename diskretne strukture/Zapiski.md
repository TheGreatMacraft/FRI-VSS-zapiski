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

**Primer:**
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

## Izjavni vezniki

1. **Negacija** izjave $A, \neg A$, beremo kot "Ne A" in je resnična *natanko tedaj*, ko je A <u>neresnična</u>. $\neg$ je **enomestni** veznik

$\begin{array}{c|c}A & \neg A \\ \hline 0 & 1 \\ 1 & 0 \end{array}$

2. **Konjunkcija** izjav A in B ($A \land B$), beremo kot "A in B" in je resnična *natanko tedaj*, ko sta <u>obe</u> izjavi A in B resnični.

$\begin{array}{c|c} A & B & A \land B \\ \hline 0 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$

3. **Disjunkcija** izjav A in B ($A \vee B$), beremo kot "A ali B" in je resnična *natanko tedaj*, ko je resnična <u>vsaj ena</u> od izjav A ali B.

$\begin{array}{c|c} A & B & A \vee B \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{array}$

4. **Ekskluzivna disjunkcija** izjav A in B ($A \veebar B$), beremo "A ekskluzivni ali B" in je resnična *natanko tedaj*, ko je <u>natanko eden</u> od izjav A ali B resničen.

$\begin{array}{c|c} A & B & A \veebar B \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$

5. **Implikacija** izjav A in B ($A \implies B$), beremo "Iz A sledi B" in je ==ne==resnična *samo v primeru*, ko je izjava A resnična, izjava B pa neresnična. Vlogi členov sta različni.

$\begin{array}{c|c} A & B & A \implies B \\ \hline 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$

6. **Ekvivalenca** izjav A in B ($A \Longleftrightarrow B$), beremo "A ekvivalentno B", "A natanko tedaj, ko B", "A če in samo če B" in je resnična *natanko tedaj*, ko imata obe izjavi A in B <u>enako logično vrednost</u>.

$\begin{array}{c|c} A & B & A \Longleftrightarrow B \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$

Če z oklepaji ni drugače naznačeno, potem je prednostni red takšen:

![[Drawing 2025-10-08 12.10.35.excalidraw]]

## Izjavni izrazi

- **Izjavni konstanti** sta 0 in 1, ki jima pravimo tudi *laž* in *resnica*, sta izjavna izraza.
- **Izjavne spremenljivke** $p,q,r, ...$ so izjavni izrazi
- Če je A izjavni izraz, potem je tudi ($\neg A$) izjavni izraz
- Če sta A in B izjavna izraza, potem so izjavni izrazi tudi: ($A \land B$), ($A \vee B$), ($A \veebar B$) in ($A \Longleftrightarrow B$), ($p \implies q$), $p \implies \neg r$, $q \land (p \implies \neg r)$

## Konstrukcijsko drevo
- **Konstrukcijsko drevo** opiše, kako izjavni izraz zgradimo iz bolj enostavnih izjavnih izrazov.
- I nastopa v izjavnem izrazu J, *natanko tedaj*, ko je I moč najti v **konstrukcijskem drevesu** izjavnega izraza J.
- **Globina izjavnega izraza** nam pove število korakov, ki jih moramo narediti, da pridemo iz "osnovnih" izjavnih izrazov (p,q,r) do "originalnega" izjavnega izraza ($q \land (p \implies \neg r)$)
- **Dolžina izjavnega izraza** pa predstavlja število spremenljivk in veznikov, ki jih izjavni izraz vsebuje.
- Primer $q \land (p \implies \neg r)$:
![[Drawing 2025-10-08 13.11.12.excalidraw|250]]
V $q \land (p \implies \neg r)$ nastopajo izjavni izrazi: p, q, r, $\neg r$, $p \implies \neg r$, $q \land (p \implies \neg r)$
V $p \land q \vee r$ (lahko zapišemo tudi kot $(p \land q) \vee r$) nastopajo izjavni izrazi: $p,q,r,(p \land q), (p \land q \vee r)$, ne nastopa pa izjavni izraz $q \vee r$.

## Resničnostna tabela
- **Resničnostna tabela** izjavnega izraza je *podatkovna struktura*, ki za vsak *nabor* logičnih vrednosti izjavnih spremenljivk pove logično vrednost izjavnega izraza.
- Primer $q \land (p \implies \neg r)$:

$\begin{array}{c|c} p & q & r & \neg r & p \implies \neg r & q \land (p \implies \neg r) \\ \hline 0 & 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 & 1 & 1 \\ \hdashline 1 & 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 & 0 \end{array}$

- **Tavtologija** je izjavni izraz, ki je "vedno" resničen.
- Tavtologije: 1, $p \vee \neg p$, $p \implies p$, $p \Longleftrightarrow p$, $p \implies (q \implies p)$
- **Protislovje** je izjavni izraz, ki je "vedno" neresničen.
- Protislovja: 0, $p \land \neg p$, $(p \implies q) \land \neg(p \implies q)$, $\neg(p \implies p)$, $\neg (p \Longleftrightarrow p)$, $\neg p \Longleftrightarrow p$
- Izjavni izraz, ki ni niti tavtologija, niti protislovje imenujemo **nevtralni izjavni izraz**. V pravilnostni tabeli ima ničle in enice hkrati.
- Izjavna izraza A in B sta **enakovredna**, če imata pri vseh naborih vrednosti izjavnih spremenljivk enako vrednost.
- Primer $p \implies q, \neg p \vee q$:

$\begin{array}{c|c} p & q & p \implies q & \neg p \vee q \\ \hline 0 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 \end{array}$

Izjavna izraza $p \implies q$ in $\neg p \vee q$ sta **enakovredna** ($p \implies q \sim \neg p \vee q$).

==**Izrek**==: Izjavna izraza A in B sta enakovredna natanko tedaj, ko je izraz $A \Longleftrightarrow B$ tavtologija.
==**Izrek**==: Za enakovrednost izjavnih izrazov veljajo naslednje zveze:
1. $A \sim A$
2. Če $A \sim B$, potem $B \sim A$.
3. Če $A \sim B$ in $B \sim C$, potem $A \sim C$.

## Zakoni izjavnega računa
Nekateri pari enakovrednih izjavnih izrazov imajo posebna imena. To so **zakoni izjavnega računa**:
1. Zakon dvojne negacije:
- $\neg \neg A \sim A$
2. Idempotenca:
- $A \land A \sim A$     
- $A \vee A \sim A$
3. Komutativnost:
- $A \land B \sim B \land A$
- $A \vee B \sim B \vee A$
- $A \Longleftrightarrow B \sim B \Longleftrightarrow A$
4. Asociativnost:
- $(A \land B) \land C \sim A  \land (B \land C)$
- $(A \vee B) \vee C \sim A  \vee (B \vee C)$
- $(A \Longleftrightarrow B) \Longleftrightarrow C \sim A  \Longleftrightarrow (B \Longleftrightarrow C)$
5. Absorpcija:
- $A \land (A \vee B) \sim A$
- $A \vee (A \land B) \sim A$
6. Distributivnost:
- $(A \vee B) \land C \sim (A\land C) \vee (B \land C)$
- $(A \land B) \vee C \sim (A\vee C) \land (B \vee C)$
7. de Morganova zakona:
- $\neg (A \vee B) \sim \neg A \land \neg B$
- $\neg (A \land B) \sim \neg A \vee \neg B$
8. Kontrapozicija:
- $A \implies B \sim \neg B \implies \neg A$
9. Lastnosti 0 in 1:
- $A \implies A \sim 1$
- $A \Longleftrightarrow A \sim 1$
- $A \vee \neg A \sim 1$
- $A \land \neg A \sim 0$
10. Še lastnosti 0 in 1:
- $A \land 0 \sim 0$
- $A \vee 0 \sim A$
- $A \land 1 \sim A$
- $A \vee 1 \sim 1$
- $A \implies 0 \sim \neg A$
- $0 \implies A \sim 1$
- $A \implies 1 \sim 1$
- $1 \implies A \sim A$
11. Lastnosti implikacije:
- $A \implies B \sim \neg A \vee B$
- $\neg(A \implies B) \sim A \land \neg B$
12. Lastnosti ekvivalence:
- $A \Longleftrightarrow B \sim (A \implies B) \land (B \implies A)$
- $A \Longleftrightarrow B \sim (A \land B) \vee (\neg A \land \neg B)$
- $\neg (A \Longleftrightarrow B) \sim \neg A \Longleftrightarrow B$
13. Dodatno pravilo:
- $(\neg A \land B) \vee (A \land \neg B) = A \veebar B$

$\land$ in $\vee$ nastopata "dualno"

## Enakovrednost izjavnih izrazov
Kako lahko pokažemo, da sta izjavna izraza A in B enakovredna?
- Primerjamo njuni pravilnostni tabeli. (za n-spremenljivk bomo imeli $2^n$ vrstic tabele - proces hitro postane dolgotrajen)
- Uporabimo privedbo in zakone izjavnega računa. 
Kako lahko pokažemo, da izjavna izraza A in B **nista** enakovredna?
- Dovolj je poiskati en sam nabor logičnih vrednosti spremenljivk, pri kateri imata A in B različni logični vrednosti. 

## Disjunktivna normalna oblika
**Disjunktivna normalna oblike (DNO)** izjavnega izraza A je izjavni izraz $A_{DNO}$, za katerega velja:
- $A \sim A_{DNO}$
- $A_{DNO}$ je disjunkcija osnovnih konjunkcij.
**Osnovna konjunkcija** je konjunkcija izjavnih spremenljivk in/ali njihovih negacij.
$A_{DNO}$ lahko zgradimo tako, da za vsak nabor pravilnostne tabele, pri katerem je izraz A resničen, pripravimo eno osnovno konjunkcijo. V njej nastopajo v tem naboru resnične spremenljivke in negacije v tem naboru lažnih spremenljivk.

## Konjunktivna normalna oblika
**Konjunktivna normalna oblika (KNO)** izjavnega izraza A je izjavni izraz $A_{KNO}$, za katerega velja:
- $A \sim A_{KNO}$
- $A_{KNO}$ je konjunkcija osnovnih disjunkcij
**Osnovna disjunkcija** je disjunkcija izjavnih spremenljivk in/ali njihovih negacij.
$A_{KNO}$ lahko zgradimo tako, da za vsak nabor pravilnostne tabele, pri katerem je A neresničen, pripravimo eno osnovno disjunkcijo. V njej nastopajo v tem naboru lažne spremenljivke in negacije v tem naboru resničnih spremenljivk.

## Kdaj KNO in DNO
Vsak izjavni izraz ima DNO **in** KNO.
- Kaj je DNO protislovja? $(p \land \neg p) \vee (q \land \neg q)$
- Kaj je KNO tavtologije? $(p \vee \neg p) \land (q \vee \neg q)$

## Polni nabori izjavnih veznikov
Družina izjavnih veznikov $\mathcal{N}$ je **poln nabor izjavnih veznikov**, če za vsak izjavni veznik A obstaja enakovreden izjavni izraz B, ki vsebuje samo veznike $\mathcal{N}$.
- Poln nabor izjavnih veznikov je {$\neg, \land, \vee$}
- Nekaj drugih polnih naborov izjavnih veznikov: {$\neg, \vee$}, {$\neg, \land$}, {$\neg, \implies$}, {$0, \implies$}

Dokaz: {$\neg$, $\vee$} je poln nabor.
Izberemo poljuben izjavni izraz A.
Ker je {$\neg, \land, \vee$} poln nabor, obstaja izjavni izraz A', za katerega velja: $A' \sim A$, in A' uporablja samo $\neg, \land, \vee$.
Kako bi se v A' znebili konjunkcij?
$p \land q \sim \neg \neg (p \land q) \sim \neg (\neg p \vee \neg q)$
Če v A' vsako izmed konjunkcij nadomestimo, kot v zgornjem zgledu, predelam A'', $A'' \sim A' \ sim A$, ki uporablja samo $\neg$ in $\vee$.

Kako v praksi pokazati, da je nabor izjavnih veznikov $\mathcal{N}$ poln?
1. Izberemo znan poln nabor izjavnih veznikov $\mathcal{Z}$.
2. Vsak veznik iz znanega nabora $\mathcal{Z}$ izrazimo samo z uporabo veznikov iz $\mathcal{N}$.

Kako pokazati, da nabor izjavnih izrazov ni poln?
Lahko poiščemo ovire (nabor {$\implies,\land$} ohranja vrednost 1, zato ni sposoben opisati negacije)

**Trditev:** Izraz $A_1 \veebar A_2 \veebar A_3 \veebar ... \veebar A_n$ je *ne glede na to, kako so postavljeni oklepaji* resničen natanko tedaj, ko je *liho mnogo* členov izmed $A_1,A_2,A_3,...,A_n$ resničnih.

![[Drawing 2025-10-16 11.34.11.excalidraw]]

## Sklepanje v izjavnem računu
Predpostavki: 
1. Če dežuje, je oblačno (Če A, potem B -> $A\implies B$)
2.  Dežuje (A = 1)
Zaključek:
3. Oblačno je (B = 1)

Predpostavke:
1. Ta žival ima krila ali pa ni ptič ($k\vee \neg p$)
2. Če je ta žival ptič, potem leže jajca ($p \implies j$)
3. Ta žival nima kril ($\neg k$)
Zaključek:
4. Ta žival ne leže jajc. ($\neg j$)

### Pravilen sklep

Zaporedje izjavnih izrazov $A_1.A_2....,A_n,B$ je *pravilen sklep* s *predpostavkami* $A_1,A_2,...,A_n$ in *zaključkom* B, če je zaključek B resničen pri vseh naborih vrednosti izjavnih spremenljivk, pri katerih so resnične vse predpostavke.

Pišemo $A_1,A_2,...,A_n$ |= B
in beremo: Iz predpostavk $A_1,A_2,...,A_n$ logično sledi zaključek B.

Zgled:
Predpostavke:
1. Šel bom na tekmo, zvečer pa bom naredil domačo nalogo
2. Če grem na tekmo in nato še v kino, zvečer ne bom mogel narediti domače naloge.
Zaključek:
3. Ne morem iti v kino.

![[Drawing 2025-10-16 11.55.40.excalidraw]]

Dokaz $A_1,A_2,...,A_n$ |= B, "vedno", ko so resnične vse $A_1,...,A_n$, je resničen B. Vedno, ko je resničen $A_1 \land A_2 \land ... \land ... A_n$, je resničen tudi B.

$(A_1 \land A_2 \land ... \land A_n) \implies B$ je "vedno" red (tavtologija)

#### Pravila sklepanja (osnovni pravilni sklepi)

$A,A\implies B \models B$   modus ponens (MP)
$A \implies B, \neg B \models  \neg A$   modus tollens (MT)
$A \vee B, \neg B \models A$   disjunktivni silogizem (DS)
$A \implies B, B \implies C \models A \implies C$   hipotetični sigolizem (HS)
$A,B \models A \land B$   združitev (Zd)
$A \land B \models A$   poenostavitev (Po)
$A \models A \vee B$   pridružitev (Pr)

#### Dokaz pravilnosti sklepa

Pravilnost sklepa $A_1,A_2,...,A_n \models B$ pokažemo tako, da sestavimo zaporedje izjavnih izrazov $C_1,C_2$

Ali iz predpostavk $p\implies q, p \vee r, q \implies s, r \implies t, \neg s$ sledi t?
1. $p \implies q$ predpostavka
2. $p \vee r$ predpostavka
3. $q \implies s$ predpostavka
4. $r \implies t$ predpostavka
5. $\neg s$ predpostavka
6. $p \implies s$ HS(1,3)
7. $\neg p$ MT(6,5)
8. r DS(2,7)
9. t MP(8,4)

Ali iz predpostavk:
1. Če sije sonce, nosim sončna očala.
2. Nosim kapo ali sončna očala.
3. Sončnih očal ne nosim.
sledi zaključek
4. Nosim kapo in sonce ne sije. ($k \land \neg s$)

s...sije sonce
k...nosim kapo
o...nosim očala

1. $s \implies o$
2. $k \vee o$
3. $\neg o$
4. k DS(2,3)
5. $\neg s$ MT(1,3)
6. $k \land \neg s$ Zd(4,5)

Z dvema protislovnima izjavama lahko sklepamo na karkoli:
1. $p$
2. $\neg p$
3. $p \land \neg p$ Zd(1,2)
4. 0 $\sim 3.$
5. $0 \vee q$ Pr(4)
6. $q \sim 5.$

#### Pomožni sklepi

**Pogojni sklep (PS)** uporabljamo, kadar ima zaključek sklepa obliko implikacije.
Izrek: $A_1,A_2,...,A_k \models B \implies C$ natanko tedaj, ko $A_1,A_2,...,A_k,B \models C$.
Če $A=A_1 \land A_2 \land ... \land A_n$, potem $A \implies (B \implies C)$ tavtologija, natanko tedaj, ko $(A \land B) \implies C$ tavtologija.

$A \implies (B \implies C) \sim \neg \vee (\neg B \vee C) \sim$$(\neg A \vee \neg B) \vee C \sim \neg (A \land B) \vee C \sim (A \land B) \implies C$

Zgled:
Predpostavke:
1. $p \implies q \vee r$
2. $\neg r$
3. 
	 1. p pred PS
	 2. $q \vee r$ MP(1,3.1)
	 3. q DS(2,3.2)
3 $p \implies q$ PS(3.1,3.3)3

Po zaključku protiprimira, ne smemo več uporabljati *notranjih vrstic*.

---

**Sklep s protislovjem (RA)** lahko uporabljamo kadarkoli.
Izrek: $A_1,A_2,...,A_k \models B$ natanko tedaj, ko $A_1,A_2,...,A_k, \neg B \models 0$.
$A \implies B$ tavtologija, natanko tedaj, ko $(A \land \neg B) \implies 0$ tavtologija.

$(A\land \neg B) \implies 0 \sim \neg(A \land \neg B) \vee 0 \sim$
$\sim \neg (A\land \neg B) \sim \neg A \vee B \sim A \implies B$

Zgled: Pokaži, da iz $p \implies \neg(q \implies r), s \land q \implies r$ in s sledi $\neg p$
1. $p \implies \neg(q\implies r)$ predpostavka
2. $s\land q \implies r$ predpostavka
3. $\neg p$ predpostavka
4.1 $\neg \neg p$ predpostavka RA
4.2 p $\sim 4.1$
4.3 $\neg (q \implies r)$MP(1,4.2)
4.4 $q \land \neg r \sim 4.3$
4.5 q Po(4.4)
4.6 $\neg r$ Po(4.4)
4.7 $s\land q$ Zd(3,4.5)
4.8 r MP(2,4.7)
4.9 $r \land \neg r \sim 0$ Zd(4.8,4.6)
4. $\neg p$ RA(4.1,4.9)

![[Drawing 2025-10-16 13.51.50.excalidraw]]

---

**Analiza primerov (AP)** lahko uporabljamo, kadar ima ena od predpostavk obliko disjunkcije.

Izrek:
$A_1,A_2,...,A_k.B_1 \vee B_2 \models C$ natanko tedaj, ko
$A_1,A_2,...,A_k,B_1 \models C$ in
$A_1,A_2$
### Nepravilen sklep

Kako pokažemo, da sklep ni pravilen?
Poiščemo *protiprimer*, nabor vrednosti izjavnih spremenljivk, pri katerem so vse predpostavke resnične, zaključek pa ne.

![[Drawing 2025-10-16 12.01.58.excalidraw]]

Sklep:

![[Drawing 2025-10-16 12.04.29.excalidraw]]

**Tips and tricks**: Kako dodati r v izjavni izraz kot $(p \land q \land \neg s)$
![[Drawing 2025-10-17 10.28.58.excalidraw]]