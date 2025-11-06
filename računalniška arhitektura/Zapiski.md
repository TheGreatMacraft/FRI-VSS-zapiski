
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
# Obveznosti predmeta
Pogoji za pristop k izpitu:
- redno obiskovanje in sodelovanje na predavanjih in vajah
- opravljanje vaje
- uspešno opravljanje krajših preverjanj med vajami

# Kaj je arhitektura računalnikov?
- Začetek (20. stol, pred 2. sv. vojno): Ali je mogoče najti natančen predpisan matematični postopek, s katerim se da izračunati vse kar se izračunati da. - Stroj
- Turingov stroj - tak postopek -> iz tega nastala *teorija izračunljivosti*, ki dokaže ali je problem izračunljiv in kako se ga da izračunati (s strojem)y
- Stroj, ki to zmore je računalnik. -> Filozofska razprava za tak stroj o tem kako naj dela, da bo uporaben in praktičen.
- **Arhitektura** je veda, ki skuša podati odgovor na vprašanje: *Kako naj delajo "stroji" s katerimi je možno izračunati vse, kar je izračunljivo.*
	- Kako naj jemljejo navodila za računanje (ukazi)
	- kje naj bodo navodila
	- v kakšnem vrstnem redu naj jih jemlje
	- ali bo navodila med izvajanjem navodilo možno spreminjati med delovanjem
	- kje naj bodo podatki (operandi), ki jih najbolj potrebujemo
	- kako naj bodo ukazi in operandi zapisani (kodirani)
	- kako naj bo zapisana informacija o tem kje so ukazi in operandi
	- kako naj računalnik "komunicira" z okolico
- Leta 1945: Von Neummanova arhitektura -> uporabljajo jo skoraj vsi današnji računalniki

# Von Neumanova arhitektura
1. "*Računalnik naj deluje izključno na osnovi vsebine ukazov*. => *Naj ne spreminja svojega ožičenja.*" (CPE - zajema, interpretira in izvaja ukaze)
2. "*Naj bodo ukazi shranjeni nekje v računalniku. Zaporedje ukazov naj se imenje program.*" => **računalnik s shranjenim programom** (pomnilnik)
3. Poleg ukazov računalnik potrebuje tudi podatke nad katerimi bo izvrševal ukaze => **operandi** (pomnilnik)
4. Običajno CPE prebere nek ukaz, ki pravi naj nekaj naredi z operandi (npr: C = A+B), pri čemer je A,B in C v pomnilniku. Zato mora CPE operande prebrati iz pomnilnika in jih začasno hraniti pri sebi. To pomeni, da CPE potrebuje majhen pomnilnik => **registri**
5. CPE izvršuje ukaze iz programa zaporedoma - **enega za drugim** (zato je V.N. rekel, da mora CPE imeti neko možnost, da šteje izvedene ukaze in tako ve, kateri je naslednji na vrsti => **program counter**), razen če v programu ne piše drugače ali če pride do **izjeme**, ki zahteva, da se izvede nek drug program.
	**programski števec** => hrani evidenco o trenutno izvajajočem se ukazu in pove, kateri bo naslednji - je nekakšen "kazalec", ki kaže, kje je trenutni ukaz v pomnilniku. Po vsakem izvedenem ukazu: **PC = PC + 1**
6. V.N. računalnik naj ima možnost komunikacije z zunanjim svetom:
	- vpis v računalnik
	- prošnja informacije o trenutnem stanju
	- naj ima možnost interakcije z zunanjim svetom
	To mu omogočajo **vhodno izhodne enote** (V/I)
- Delovanje takega računalnika ne določa **nič drugega**, kakor shranjeni programi.
- **V.N. ozko grlo** - dostop do pomnilnika je bil (in še vedno je) počasnejši od potencialne hitrosti izvajanja ukazov.


![[Drawing 2025-10-07 13.01.58.excalidraw|1000x400]]

## Pomnilnik
- pomnilnik je sestavljen iz zaporedja *pomnilniških besed (memory word)*
- **pomnilniška beseda** je najmanjša količina informacije, ki se prenaša med pomnilnikom in CPE
![[Drawing 2025-10-07 13.36.44.excalidraw|1500]]
- v digitalni elektroniki, s katero implementiramo rač. sisteme se najmanjši količini informacije reče *bit*. Hrani se jo v obliki 0/1 (visoka ali nizka napetost => 3.3V ali 0V)
- Vsaka pomnilniška beseda ima svoj enoličen **naslov**, ki je informacija o poziciji besede v pomnilniku
- Tipična širina podatkovne besede je **8 bitov**, oziroma 1 bajt. 

## CPE
Enota v VN arhitekturi, ki:
	- zajema ukaze in operande iz pomnilnika,
	- izvršuje ukaze nad operandi (npr. C = A + B -> + je *operacija*, A, B, C pa so *operandi* **!informacija o operaciji in operandih je zapisana v ukazu!**),
- CPE *mora vedeti, kje je naslednja enota*, ki jo mora zajeti in izvršiti. Zato ima CPE eno enoto, ki se ji reče **programski števec** (program counter = PC) => V VN arhitekturi, kjer so ukazi shranjeni eden za drugim v pomnilniku, se po vsakem zajetem in izvršenem ukazu, PC preprosto poveča za 1. *PC = PC + 1* (inherentna lastnost VN arhitekture)
- CPE zajema in izvršuje ukaze enega za drugim, razen če:
	- drugače ne piše v ukazu (*skočni ali vejitveni ukazi*)
	- pride zunanji signal, ki zahteva spremembo toka izvajanja ukazov (*prekinitev oz. interrupt*)
	V teh primerih $PC \ne PC +1$, ampak postane neka nova vrednost.
Zaradi pravila PC = PC + 1, ki ga "kršimo" le izjemoma, vem z zelo visoko verjetnostjo iz katerega dela pomnilnika oz.  iz katerih pomnilniških besed se bodo brali ukazi. - **prostorska lokalnost**: Z veliko verjetnostjo do pomnilnika dostopamo v takšnem zaporedju naslovov: A, A+1, A+2, A+3, ... A+n
Dodatno: Če imam 1000 operandov, in vsakega od njih želim "obdelati" s 5 ukati, si ne želim pisati programa, ki bi imel 1000 setov istih 5 ukazov, ampak si želim v arhitekturi imeti ukaz, s katerim je mogoče peterček ukazov 1000-krat ponovit.

ukaz1->ukaz2->ukaz3->ukaz4->ukaz5->skoči na ponovi => **spremeni pravilo PC = PC + 1 v PC <= ponovi**
- z zelo veliko verjetnostjo vem, da če sedaj izvajam npr. ukaz3, da bom čez relativno kratek čas *spet izvedel ukaz 3*, prav tako lahko z veliko verjetnostjo trdim, da bom iz pomnilnika bral ukaze z naslovov: A, A+1, A+0. A+3, A+4, A+5, A, A+1, A+0. A+3, A+4, A+5, ... oziroma, da bom nekaj časa zajemal ukaze iz majhnega in vedno istega dela pomnilnika - **časovna lokalnost**
- Isti ukazi, ki se pogosto pojavljajo (kot npr. v zankah), se *začasno* shranijo v **predpomnilniku (cashe)**

Predpostavimo, da izvajamo nek program, ki ima veliko ukazov. Med tem naborom ukazov, obstaja delež ukazov, ki jih lahko izvedem N-krat hitreje, ker uporabim N VN računalnikov.
![[Drawing 2025-10-09 12.58.01.excalidraw]]

$S(N) = \frac{1}{\frac{t}{N}+(1-t)}$

Primer: t=0.5, N = 1000
$S(1000) = \frac{1}{\frac{0.5}{1000}(1-0.5)} = \frac{1}{\frac{0.5 + 500}{1000}} = \frac{1000}{500.5} = 1.998$

$\lim_{N \to \infty} S(N) = \frac{1}{\frac{t}{N} + (1-t)} = \frac{1}{(1-t)}$ = max možna pohitritev.

Na žalost nam VN arhitektura ne omogoča učinkovite rave paralelnih računalnikov.

## Ukazi in operandi

- informacije v VN se delijo na *ukaze* in *operande*
- operande delimo na številske in ostale
Kako zapisati števila v pomnilniku, če so besede sestavljene iz bitov $\in \{0,1\}$?
Kako z zapisom določiti vrednost? **pozicijski zapis** - glede na pozicijo v nizu števk, imajo drugačno vrednost.

$745,13_{[10]}$ = $7*10^2 + 4*10^1 + 5*10^0 + 1*10^{-1} + 3*10^{-2} = \Sigma_{-p}^{n-1}x_i*10^i$

V pomnilniku: 1bit ima le dve možni števili {0,1}.

$101011,011_{[2]} = 1*2^5+1*2^3+1*2+1*2^0+1*2^{-2}+1*2^{-3} = 32 + 8 + 2 + 1 + 0,25 + 0.125 = 43.375$
## Zapis celih predznačenih števil

1. Predznak & velikost (sign $ magnitude)
Ideja: Najvišji bit pri n-bitnem celem številu določimo za predznak: $0 \implies +, 1 \implies -$

**$b_{N-1}$** - naj bo predznak$,b_{N-2},b_{N-3} ... b_2, b_1, b_0$
$V = (-1)^{b_N-1} * \Sigma^{N-2}_{i=0} bi*2^i$


Poskusimo seštet pozitivno in neg število:
3 + (-3) = 0011 + 1011 = 1110 **NAROBE**

2. Zapis z odmikom
Predpostavimo, da je N = 3
![[Drawing 2025-10-14 17.53.13.excalidraw]]

Vsaka od teh binarnih števil vsebuje v sebi enak odmik od vrednosti, ki jo želimo kodirati.
Odmik določimo po formuli: $O = \frac{2^N}{2}$, kjer je N število bitov

**Full dobro**: Če gledam od leve proti desni nam prvi bit, pri katerem se dve števili razlikujeta pove, katero je večje/manjše $\implies$ *Leksikografsko primerjanje*

3. Eniški komplement
Predpostavimo N=3
![[Drawing 2025-10-14 18.22.32.excalidraw|500]]

Naj bo negativna vrednost nekega pozitivnega števila zapisana tako, da enostavno invertiram bite.
Težava: 2 Ničli (pozitivna in negativna) $\implies$ razdalja med 1 in -1 je 3, morala pa bi biti 2.

**Rešitev:** vsa negativna števila zamaknemo za 1.

4. Dvojiški komplement

![[Drawing 2025-10-14 18.33.20.excalidraw]]

3 + (-3) = 011 + 101 = 000 *štima*
2 + (-3) = 010 + 101 = 111 *tudi štima*

Dajmo seštet dve dovolj veliki pozitivni števili:

1 + 3 = 001 + 011 = 100 (-4)  je preliv, ni prenosa | Rezultat presega maksimalno vrednost pozitivnih števil. (*preliv*) Zgodi se pri seštevanju dveh enako predznačenih števil. 
-2 + (-3) = 110 + 101 = *1(prenos/carry)* 011 (3)  je preliv, je prenos
3 + (-3) = 011 + 101 = 1 000 $\implies$ ni preliva, je prenos

Kadarkoli računamo s predznačenimi celimi števili nam **le preliv** pove, da je rezultat napačen.

Predpostavimo nepredznačena števila in predpostavimo, da je N=3:
3 + 5 = 011 + 101 = 1 000 $\implies$ Prenos nam pove, da imamo premajhno število bitov za zapis rezultata.

Pri nepredznačenih številih nam le prenos pove, da je rezultat napačen.

$V = \Sigma^{N-1}_{i=0} bi*2^i*b_{N-1}*2^N$

Zgled:

00101111 = 47 - $0^8$
10110001 = (128+32+16+1) - 1*$2^8$ = -79

0011 = 3
00011 = 3
000011 = 3
0...00011 = 3

*Če pozitivnim številom dodam 0 na levi ne spremenim velikosti.*

10 = -2
110 = -2
1110 = -2
11110 = -2
1...1110 = -2

*Če negativnim številom dodam 1 na levi ne spremenim velikosti.*

Temu pravimo **razširitev predznaka**.

## Plavajoča vejica (floating point)
$1011,01101 = 1*2^3+1*2^1+1*2^0 + 1*2^{-1}+1*2^{-2}+1*2^{-5} = 11 + 0,25 + 0,125 + 0,03125 = 11,40625_{[10]}$
**Zapis v eksponenti obliki:**
$1011,01101 ** 2^0 = 1,01101101 * 2^3$ $\implies$ Vejica "plava" s spreminjanjem eksponenta.
Splošno: V zapisu z eksponentom: $m * 2^E$, kjer m(*matisa*) in E(*eksponent*)

Če bomo vejico postavili za najbolj levo (pomembo) enico, bo pred vejico **vedno in samo** enica. Zato nam začetne enice ni potrebno pisati (prihranimo 1 bit). Takšnemu zapisu mantise, se reče **normaliziran zapis**

Zapis števil v plavajoči vejici po standardu *IEEE 754*.
	- Za zapis števil, ta standard uporablja 32 bitov.
	- Najvišji bit določa predznak ($1 \implies -; 0 \implies +$)
	- Naslednjih 8 (od $b_{30}$ do, vključno z $b_{23}$) se uporablja za zapis števil
	$$v = (-1)^S*1,m * 2^{E-127}$$, kjer v - value, S - size, m - matisa, E - eksponent

Nič se predstavi tako, da so vsi biti v $m = 0$ in $E = 0$
Če imamo zelo majhno število: Če E ne morem več zmanjšati, potem vejice ne morem premakniti za "1" => Ne morem normalizirati števil.

**Denormalizirana števila** $\implies m \ne 0; E = 0$
$$v_{denorm.} = (-1)^S*0,m*2^{-126}$$
Kako predstaviti +/- $\infty$?
Pojavi se pri deljenju z 0. Neskončnost predstavimo tako, da ima eksponent vse bite 1 $\implies E = 1111 1111, m = 0$

Kako zapisati NaN (nedefinirana števila "Not a Number")?
Pojavi se pri $\frac{0}{0}$. Predstavimo enako kot neskončnost, vendar mantisa ne sme biti 0.
 $\implies E = 1111 1111, m \ne 0$
Vsa ostala normalizirana števila:
$$v = (-1)^S*1,m*2^{E-127};E\in[1,254)$$
To je zapis v enotni natančnosti (single percision).

**Zapis v dvojiški natančnosti (double percision)**
Zanj uporabljamo 64 bitov:
- Najpomembnejši bit je +/-
- 11 bitov je namenjenim eksponentu
- 52 pa matisi

Normalizirano:
$$v = (-1)^S*1,m*2^{E-1023}; E\in[1...2047]$$



# Ostali številski sistemi
- dvojiški, pozicijski zapis: $\displaystyle V(b) = \sum_{i=0}^{n-1}bi2^i; bi \in \{0,1\}$
- osmiški: $\displaystyle v(x) = \sum_{i=0}^{n-1}xi8^i; xi \in \{0,7\}$
- šesnajstiški: $\displaystyle v(x) = \sum_0^{n-1}xi*16^i; xi = \{0...9,A,B,C,D,E,F\}$
![[Drawing 2025-10-21 11.26.00.excalidraw]]

---

# Ukazi
Končno zaporedje bitov, s katerimi kodiramo vsebuje:
- informacijo o operaciji (Kaj naj procesor dela)
- informacijo o operandih (Nad čem naj to naredi)
Danes so ukazi najpogosteje 32 ali 64 bitov
- nekatere arhitekture imajo poljubno dolge ukaze (npr. Intel)
Sodobne arhitekture (RISC-V ali ARC) imajo vse ukaze enako dolge (32 ali 64 bitov)

Ukaz (n-biten), ima nekje bite za operacije in nekje bite o operandih. **Format ukazov** določi, kateri biti kodirajo operacijo in kateri biti kodirajo operande.

Ukazi so bitni zapisi, ki hranijo informacijo o operaciji in operandih. Hranijo se v pomnilniku (VN arhitektura). Vse dogajanje znotraj računalnika je določeno **le** z ukazi.

**Format ukaza** natančno določa, kateri bit v ukazu kodirajo informacijo o operaciji in informacijo o operandih.
**Operacijska koda** je bitni zapis v ukazu s katerimi kodiramo informacijo o operaciji.

Ukazi opredeljujejo naslednje lastnosti računalnikov:
1. Kako se operandi hranijo znotraj CPE.
	- CPE mora pred izvajanjem ukazov, ukaze in operande prebrat iz pomnilnika.
	- Kje je ukaz - določa PC, ki hrani naslov naslednjega ukaza
	- Kje so operandi - je zapisano v ukazu
	- Ko CPE prebere operande iz pomnilnika, jih mora nekje začasno hraniti.
	- Obstaja velika verjetnost, da:
		- bomo isti operand uporabili v več ukazih
		- bomo rezultat nekega ukaza ponovno uporabili v enem od naslednjih ukazov
		Torej je pomembno operande **začasno hraniti v CPE**
2. Število eksplicitnih operandov v ukazu.
	- Po eni strani si želimo veliko število operandov v ukazu, zato, da bi lahko z enim samim ukazom obdelal čim več ukazov.
		- Večje število operandov - **daljši ukazi** - veliko časa, da jih prenesemo v CPE
3. Kako bo v ukazu zapisana informacija o lokaciji operandov v pomnilniku.
	- Najbolj naiven pristop: za vsak operand v ukazu zapišimo njegov celoten naslov. Ta rešitev je neučinkovita, ker potrebujemo zelo veliko število bitov, za zapis operandov. Pri določenih računalnikih je naslov dolg 64 bitov. Za dva operanda, v ukazu bi potrebovali 128 bitov, kar bi bilo **predolgo**.
4. Operacije.
5. S kakšno vrsto operandov želimo delat (celo število ali floating point) in koliko bitov bomo namenili za zapis posamezne vrste operandov (8,16,128,...)

---
## Kje hranimo operande znotraj CPE
- V CPE vgradimo zelo majhen pomnilnik, ki ima le nekaj pomnilniških besed. Vsaki taki pomnilniški besedi, rečemo register. Računalniki imajo lahko 1,2,8,16,32 registrov:
	- če ima CPE en sam register, se mu reče **akumulator** (ACC)
		ACC $\leftarrow$ ACC operacijo OPERAND
		Tipični primer takega računalnika: z80, 6502
		Add #16 : ACC $\leftarrow$ ACC + 16 - eden od operandov je bil *eksplicitno* naveden (16), drugi pa *implicitni* (ACC)
	- če ima CPE pomnilnik narejen iz več pomnilniških besed, se jim reče **registrski niz**
		- rešitev pri vseh sodobnih računalnikih, ker imajo 8,16,32 registrov (32 ali 64 bitni)

**Registrski niz** je razdeljen v skupini registrov:
1. Starejši registri:
	- registri v katerih se hranijo operande za splošne aritmetične operacije
	- registri za računanje z naslovi
	**Motorola 6800**: (70-ta leta)
	- A,B - dva registra za aritmetične operacije - 8 bitna
	- x - hranjenje in računanje z naslovi - 16 bitna
	- SP - stack-pointer (skladni kazalec) - 16 bitna
	**Intel x86-32**:
		EAX, EBX, ECX, EDX - 32 bitni registri za aritmetične operacije
		ESI, EDI, EBP, ESP - 32 bitni registri za računanje z naslovi
2. Novejši registri:
	Vsi registri so **enakovredni** in se uporabljajo tako za aritmetične operacije, kot tudi za hranjenje in računanje z naslovi. $\implies$ splošno-namenski registri
	**ARMv7** (32-bit)
		16 registrov: $r_0,r_1,r_2,...,r_{14},r_{15}$,
		kjer je $r_{15}$ PC, $r_{14}$ LR (link register), $r_{13}$ stack pointer
	**RISC-V** (32-bit)
		32 registrov: $x_0$-$x_{31}$
## Število eksplicitnih operandov
1. Eno-operandni računalniki
	ACC $\leftarrow$ ACC operacija OPERAND
	V ukazu sta eksplicitno zapisano samo informacija o operaciji in operandu.
	**Z80, 6502** (70-ta leta)
2. Dvo-operandni računalniki
	OP1 $\leftarrow$ OP1 operacija OP2
	zgled(Intel) ADD EAX, EBX (EAX $\leftarrow$ EAX + EBX)
3. Tri-operandni računalnik
	OP3 $\leftarrow$ OP1 operacija OP2
	**ARMv7**
		ADD R2,R5,R7; R2 $\leftarrow$ R5 + R7
		AND R2,R1,R8 ; R3 $\leftarrow$ R1 & R8
	**RISC-V**
		ADD X7,X13,X11 ; X7 $\leftarrow$ X13 + X11
		SUB X29, X17, X30 ; X29 $\leftarrow$ X17 - X30
## Lokacija operandov in načni naslavljanja
- Kje smejo biti operandi, ki se uporabljajo v *aritmetičnih operacijah*. Te operacije so zelo pogoste!!! Ker jih želimo izvajati hitro zato ne želimo operandov v pomnilniku.

Dve vrsti računalnikov:
1. Registrsko-pomnilniški (npr. Intel) reg $\leftarrow$ reg OP (operand v pomnilniku)
2. Registrsko-registrski - vsi operandi so v registrih (ARMv7,RISC-V)

- Kako je podana *informacija o lokaciji* operandov?
	- Informaciji o lokaciji, se reče **način naslavljanja**
	- poznamo 3 vrste operandov (glede na njihovo lokacijo)
		- **Takojšni operandi** (immediate) - operandi, ko so že v ukazu (ADD r4,r3,#1 ; r4 $\leftarrow$ r3 + 1) ![[Drawing 2025-10-28 13.31.09.excalidraw]]
			- #1 je že takoj zapisan v ukazu in takoj na voljo za operacijo
		- **Registrski operandi** so operandi, ki so že v enem od registrov v CPE. Informacija o njihovi lokaciji je podana z naslovom (indeksom, imenom) registra v ukazu.
			npr: ADD r4, r3, #1 (r4 je **registrski operand**)
			Ko CPE prebere tak ukaz, še nima tega operanda!!
			- ima le informacijo, da se operand nahaja v r3
			- ni takoj na voljo CPE, ker ga mora pred uporabo prebrati iz registra
			![[Drawing 2025-10-28 13.37.45.excalidraw]]
			- Če ima CPE $2^n$ registrov, potem v ukazu potrebujemo n bitov za zapis naslov registra
		- **Pomnilniški operandi** 
			- če v ukazu dovolimo pomnilniške operande, potem v ukazu moramo zapisati naslov pomnilniške besede, ki hrani operand. Kako?
				- **Neposredno** v ukaz zapišemo naslov. Težava je, da so naslovi dolgi! (Intel)
				- **Posredno** - naslov ali del naslova je vsebovan v enem od registrov.
## Kakšne operacije naj poznajo arhitekture
1. **Aritmetično-logične operacije**
	- aritmetika (+,-,\*,...,/)
	- logične (IN, ALI, NE, ...)
	- pomiki (logični & aritmetični)
2. **Prenos podatkov med CPE registri in RAM**
	- LOAD/STORE ukazi
3. **Kontrolni ukazi**
	- z njimi spreminjamo potek izvajanja ukazov oz. programov
	- to so ukazi, ki **spreminjajo PC**
		Spreminjanje PC je lahko:
		1. **Brezpogojno** (brezpogojni skoki) 
			- običajno ukazi za klicanje in vračanje iz podprograma
		2. **Pogojno** (pogojni skoki)
			- Pogojni biti (*N - negative, Z - zero, V - overflow, C - carry*) - zastavice (flags)
				- CPE po vsaki operaciji postavi/pobriše te bite
				- po vsaki izredni operaciji CPE pregleda rezultat:
					a) če so vsi biti v rezultatu = 0
					b) če je MSB = 1, potem postavi N bit
					c) če sešteva 2 števili in zunaj ... IDK
					d) če seštevamo ali odštevamo dve enako predznačeni števili in ima rezultat drugačen predznak $\implies V = 1$
				- CPE mora imeti dokaj kompleksno logiko, da vsakič preveri rezultat glede na te 4 bite. $\implies$ naslednji člen (pogojni skok) lahko premeni PC glede na te 4 bite. (Intel)
			- Pogojni register - ukaz za pogojni skok preveri ali je v registru = 0 - pogoj postavljamo z ukazi, ne s posebno logiko (RISC-V)
4. **Operacije v FP (floating point)** - operacije v DP, sistemski ukazi
## Vrste in dolžina operandov
- dolžina v bitih: 8 - byte, 16 - half word, 32 - word, 64 - double word, 128 - quad word
Vrste:
- številski (predznačeni, nepredznačeni, FP)
- znaki
- barve
- zvoki
# Arhitektura Ukazov ARM-V Lite
1. Kako se operandi hranijo znotraj CPE?
- ARMv7 ima 16 32-bitnih registrov.
- R15 je PC - le ta register ima poseben namen, glede kaj **hrani** - hrani naslov naslednjega ukaza (PC)
- R14 - v njem je shranjen *povratni naslov* (Link Register)
- R13 - *Stack Pointer*
1. ARMv7 ima 3-operandne ukaze
**Format ukazov pri ARMv7 Lite**
- vsi ukazi so 32-bitni:
	31 - 28: pod kakšnim pogojem naj se nek ukaz izvede (condition)
	- 0000 - izvedi, če je Z=1 (EQ)
	- 0001 - izvedi, če je Z=0 (NEQ)
	- 0010 - izvedi, če je C=1 (CS)
	- 0011 - izvedi, če je C=0 (CC)
	- 0100 - izvedi, če je N=1 (NS)
	- 0101 - izvedi, če je N=0 (NC)
	- 0110 - izvedi, če je V=1 (VS)
	- 0111 - izvedi, če je V=0 (VC)

	- 1110 - ALWAYS (izvedi ukaz bedno) $\implies$ to bodo imeli v zgornjih 4 bitih vsi ukazi razen pogojnih
	27-25: povejo tip ukaza:
	- 00x: data processing
	- 010: LOAD/STORE ukazi
	- 10x: kontrolni ukazi
## Data Processing Ukazi
![[Drawing 2025-11-04 12.38.29.excalidraw]]

## Load/Store Ukazi
![[Drawing 2025-11-04 13.26.36.excalidraw]]
