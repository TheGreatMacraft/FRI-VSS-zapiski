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

