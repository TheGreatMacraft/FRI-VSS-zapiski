
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
- dvojiški, pozicijski zapis: $$V(b) = \sum_{i=0}^{n-1}bi2^i; bi \in \{0,1\}$$
- osmiški: $$v(x) = \sum_{i=0}^{n-1}xi8^i; xi \in \{0,7\}$$
- šesnajstiški: $$v(x) = \sum_0^{n-1}xi*16^i; xi = \{0...9,A,B,C,D,E,F\}$$
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
