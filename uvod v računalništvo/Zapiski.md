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

# Teme
- uporabniška zgodba, primeri uporabe, wireframe
- računalnik kot stroj
- zbirni jezik
- binarna števila, zvok, slika, ascii
- turingov stroj - prob 1. kolokvij
- grafana (part 1)
- programski jezik: gramatike
- programski jezik: algoritmi
- programski jezik: kompleksnost algoritmov
- informacijska varnost
- razvoj PO
- podatkovne baze
- grafana (part 2) - prob 2. kolokvij

# Odkrivanje in analiza zahtev

- z iskanjem dejstev poiščemo uporabniške potrebe (intervju z zaprtimi/odprtimi vprašanji, različne ciljne skupine, skupinsko delo, pregled obstoječih sistemov, opazovanje)
- funkcionalne zahteve - temeljne akcije PO, odgovor na vhode, kako sistem rana v določenih situacijah
- nefunkcionalne zahteve - omejitve sistema (časovne, razvijalske, ...)

## Uporabniška zgodba
- neformalna, splošna razlaga določene funkcije programa iz zornega kota *končnega uporabnika*
- razčleni, kako bo funkcija PO prinesla vrednost uporabniku
- končne uporabnike postavimo v središče pogovora
- ko razvijalska ekipa prebere uporabniško zgodbo, bo vedela, zakaj nekaj razvijajo
- Kaj kdo hoče? 
Kot [vloga uporabnika], želim [cilj ali funkcijo], da [korist ali razlog].

| Končni uporabnik | Funkcionalne zahteve         | Nefunkcionalne zahteve |
| ---------------- | ---------------------------- | ---------------------- |
| študenti         | vpis v predmet               | mobilnost              |
|                  | prijava na izpit             | dostopnost > 99,99%    |
| profesorji       | registracija novega predmeta | varnost podatkov       |
|                  | vnos ocen                    |                        |
## Unified Modeling Language - UML
- standardiziran modelirni jezik
- za prikazovanje načrtovanja sistema
- vključuje mnogo podvrst programov

![[Pasted image 20251016144951.png]]

- Behaviour diagram -> kako se bo aplikacija obnašala z vidika končnega uporabnika
- Structure diagram -> kako bo aplikacija narejena
## Use case diagram
- grafični prikaz uporabnikovih interakcij s sistemom
- ponudi pogled sistema
- enostavno komuniciranje z neračunalničarji

![[Pasted image 20251016145255.png]]

- generalizacija/specializacija - organizacija uporabnikov v hijerarhijo.
- 2 vrsti povezav: extend in include
- **Include** - use case **vedno** uporablja še nek use case. (Glavno dejanje "vključuje" sekundarno dejanje): 
 ``` [glavno dejanje ] ---<<include>>---> [sekundarno dejanje]```
- **Extend** - use case **včasih** uporablja še nek drug use case (Sekundarno dejanje "razširi" glavno dejanje)
``` [glavno dejanje] <---<<extend>>--- [sekundarno dejanje] ```

![[Pasted image 20251016145846.png]]

![[Pasted image 20251016150001.png]]

## Class diagram
- prikazuje strukturo sistema
- pokaže razrede, atribute, metode, povezave med objekti

### Razredi
Prikažemo jih v pravokotnikih s tremi razdelki:
- ime razreda (krepko, na sredini, velika začetnica)
- atributi razreda (levo poravnani, mala začetnica)
- metode razreda (levo poravnane, mala začetnica)

| BankAccount                                             |
| ------------------------------------------------------- |
| owner: String; balance: Dollars = 0                     |
| deposti (amount: Dollars), withdrawal (amount: Dollars) |
![[Pasted image 20251016151207.png]]

## GUI prototip (wireframe)
- nedelujoč prikaz programa
- predstavimo primere uporabe v praksi
- lahko prikažemo za različne platforme
- navodila za programerje in oblikovalce
- poceni prikaz končnega izdelka

![[Pasted image 20251016151508.png]]

# Računalnik kot Stroj
- računalniki imajo vsi isto zasnovo
- Von Neumannova arhitektura - 3 karakteristike:
- 4 glavni podsistemi: pomnilnik, vhod/izhod, aritmetično-logična enota, krmilna enota
- program shranjen v pomnilniku
- zaporedno izvajanje ukazov

## Pomnilnik
- Funkcijska enota za shranjevanje in branje podatkov.
- Pomnilnik z naključnim dostopom (Random Access Memory - RAM)
- Naslovni register (Memory Address Register - MAR)
- Podatkovni register (Memory Data Register -MDR)
- Branje in pisanje
- Enodimenzionalna in dvodimenzionalna pomnilniška organizacija

$MAR = log_2(MemmorySize)$

1. Najmanj koliko bitov je potrebnih za naslovni register pri velikosti pomnilnika:
- 1MB ... 20
- 10MB ... 24
- 100MB ... 27
- 1GB ... 30

2. Pomnilnik naj ima dvorazsežno, kvadratno organizacijo. Kakšne so mere pomnilnika vzdolž vsake izmed obeh razsežnosti, če lahko vanj shranimo 1 MB podatkov? Kako velik bo naslovni register? Koliko bitov se pošlje v dekodirnik vrstice in koliko v dekodirnik stolpca? Koliko izhodov imata vsak izmed obeh dekodirnikov?

$a^2 = 1MB$
$a^2 = 2^{20}$
$a = 2^{10} \implies 10$

3. Recimo, da ima pomnilnik 24-bitni naslovni register, prvih 16 bitov je pri tem namenjenih naslovu vrstice, preostalih 8 bitov pa naslovu stolpca. Koliko bajtov podatkov lahko shranimo v ta pomnilnik? Kakšne so mere pomnilnika vzdolž vsake izmed obeh razsežnosti, če predpostavimo, da ima pomnilnik največjo možno velikost?

$a*b = 2^N*2^M = 2^16 * 2^8 = 2^{24} \sim 16 MB$

## Predpomnilnik
- Ozko grlo in princip lokalnosti (dostopanje do podatkov je počasno)
- Uporaba:
	- Poglej v predpomnilnik in uporabi podatek, če je tam.
	- Če ga ni, dostopaj do pomnilnika RAM
	- Kopiraj še k naslednjih podatkov.

1. Povprečni čas dostopa do pomnilnika je 25 ns, povprečni čas dostopa do predpomnilnika pa 10 ns. Kakšen je skupni povprečni čas dostopa, če je verjetnost zadetka v predpomnilniku enaka 80%? Kakšna pa bi morala biti verjetnost zadetka, če želimo skupni povprečni čas dostopa znižati na 12 ns?

$t_{pm} = 25ns$
$\Delta t_{pr} = 10ns$
$CacheProb = 80$%
$\Delta t = 0.8 * 10 + 0.2 * 35 = 15ns$

$\Delta t_2 = 12ns$
$12 = x*10+(1-x)*35$
$12 = 10x + 35 - 35x$
$12 = -25x + 35$
$25x = 23$/25
$x = \frac{23}{25}$
$x = 0,92$

## Trdi disk
- Zunanji pomnilnik - trajni
- Vhodno-izhodne naprave

1. Recimo, da ima trdi disk naslednje lastnosti: 
- hitrost vrtenja: 7200 obratov / min = 120 rot/s
- čas premika glave: 0,5 ms (fiksni začetni čas) + 0,05 ms za vsako sled
- število površin: 2 (glavi obeh površin se pomikata sočasno)
- število sledi na površino: 500
- število sektorjev na sled: 20
- število bajtov na sektor: 1024
a) Koliko bajtov podatkov lahko shranimo na ta disk? 
$2*500*20*1024 = 20480000 \sim 20.5MB$
b) Kakšni so časi dostopa do enega sektorja v najboljšem, najslabšem in srednjem primeru? Predpostavi, da se v srednjem glava premakne preko 150 sledi.

|             | Najboljši primer             | Srednji primer               | Najslabši primer                    |
| ----------- | ---------------------------- | ---------------------------- | ----------------------------------- |
| Čas iskanja | 0.5ms                        | 0.5+150 * 0.05 = 8ms         | 0.5 + 499 * 0.05 = 25.45ms          |
| Latenca     | 0ms                          | $\frac{8.33ms}{2} = 4.165ms$ | $\frac{1}{120} = 0.00833s = 8.33ms$ |
| Čas prenosa | $\frac{8.33}{20} = 0.4165ms$ | 0.4165ms                     | 0.4165ms                            |
| Skupaj      | 0.9156ms                     | 12.5815ms                    | 34,1965ms                           |

2. V splošnem podatki na disku niso shranjeni povsem naključno, temveč se običajno shranjujejo tako, da je čas, ki je potreben za dostop do podatkov kar najkrajši. Če bi imeli disk iz naloge 5, kam bi shranili 50 KB podatkov, da bi bil poznejši dostop do njih kar najhitrejši?

POGLEJ SLIKO NA FONU

Latence ne moreme izboljšati. Čas iskanja zmanjšamo tako da shranimo podatke tako da so blizu sledi 250. Napolnimo eno sled oz. 20 KB. Na isto sled, na drugo površino shranimo še 20KB podatkov. Preostale podatke (10KB) shranimo na sosednjo sled.

3. Na spletu najdite računalniško konfiguracijo in kategorizirajte komponente po Von Neumannovi arhitekturi.

## Aritmetično-logična enota (ALE)
- skupaj z *krmilno enoto* tvori procesor
- vsebuje **aritmetična** (+,-,* ,/) in  **primerjalna/logična vezja** (IN, ALI, NE)
- vsebuje **registre** - hitre (namenske) pomnilniške enote, povezane z vezjem ALE
- vsebuje **podatkovno pot** (Data path) - kako potuje informacija v ALE med registri in vezji

## Strojni ukazi
Format ukaza v strojnem jeziku:
- koda operacije
- naslovi pomnilniških lokacij z operandi

Primer:
op code: 9
naslov X: 99
naslov Y: 100
ADD X,Y: sešteje števili in zapiše rezultat nazaj na lokacijo Y
### Prenosi podatkov
- pomnilniška lokacija $\Longleftrightarrow$ register ALE
- pomnilniška lokacija A $\rightarrow$ pomnilniška lokacija B
- register ALE A $\rightarrow$ register ALE B
**Primeri**:
	- LOAD X $\rightarrow$ naloži vsebino pomnilniške lokacije v register R
	- STORE X $\rightarrow$ shrani vsebino registra R na pomnilniško lokacijo X
	- MOVE X,Y $\rightarrow$ kopiraj vsebino pomnilniške lokacije X na pomnilniško lokacijo Y
### Aritmetika
- aritmetične in logične operacije v ALE: +,-, * ,/,IN,ALI,NE
**Primeri:**
	- ADD X,Y,Z $\rightarrow$ vrednost(Z) = vrednost(x) + vrednost(Y) *tro-naslovni ukaz*
	- ADD X,Y $\rightarrow$ vrednost(Y) = vrednost(X) + vrednost(Y) *dvo-naslovni-ukaz*
	- ADD X $\rightarrow$ R = vr(X) + R *eno-naslovni ukaz*
### Primerjanje
- rezultat primerjanja postavi vrednosti bitov pogojnih kod
**Primer:**
	- COMPARE X,Y $\rightarrow$ primerja vrednosti pomnilniški lokacij X in Y in postavi vrednost pogojnih kod:
		 - vrednost(X) > vrednost(Y) GT=1, EQ=0, LT=0
		 - vrednost(X) = vrednost(Y) GT=0, EQ=1, LT=0
		 - vrednost(X) < vrednost(Y) GT=0, EQ=0, LT=1
### Vejitve
- spreminjanje normalnega zaporednega toka ukazov
- tipično po ukazu za primerjanje
**Primeri:**
	- JUMP X $\rightarrow$ vzemi naslednji ukaz s pomnilniške lokacije X
	- JUMPGT X $\rightarrow$ skoči samo, če je indikator GT postavljen na 1
	- JUMPGE X $\rightarrow$ skoči samo, če sta GT in EQ indikatorja postavljena na 1
	- HALT $\rightarrow$ ustavi izvajanje programa
### Tabela strojnih ukazov

| Binarna Koda Operacij | Operacija   | Pomen                                                                                                              |
| --------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 0000                  | LOAD X      | CON(X) $\rightarrow$ R                                                                                             |
| 0001                  | STORE X     | R $\rightarrow$ CON(X)                                                                                             |
| 0010                  | CLEAR X     | 0 $\rightarrow$ CON(X)                                                                                             |
| 0011                  | ADD X       | R + CON(X)                                                                                                         |
| 0100                  | INCREMENT X | CON(X) + 1 $\rightarrow$ CON(X)                                                                                    |
| 0101                  | SUBSTRACT X | R - CON(X) $\rightarrow$ R                                                                                         |
| 0110                  | DECREMENT X | CON(X) - 1 $\rightarrow$ CON(X)                                                                                    |
| 0111                  | COMPARE X   | - if(CON(X) > R then GT = 1 else 0)<br>- if (CON(X) = R then EQ = 1 else 0)<br>- if(CON(X) > R then LT = 1 else 0) |
| 1000                  | JUMP X      | dobi naslednji program iz pomnilniške lokacije X                                                                   |
| 1001                  | JUMPGT X    | dobi naslednji program iz pomnilniške lokacije X, če GT = 1                                                        |
| 1010                  | JUMPEQ X    | dobi naslednji program iz pomnilniške lokacije X, če EQ = 1                                                        |
| 1011                  | JUMPLT X    | dobi naslednji program iz pomnilniške lokacije X, če LT = 1                                                        |
| 1100                  | JUMPNEQ X   | dobi naslednji program iz pomnilniške lokacije X, če EQ = 0                                                        |
| 1101                  | IN X        | vnesi celo-številsko vrednost iz vhodne naprave v pomnilniško lokacijo X                                           |
| 1110                  | OUT X       | izpiši, v decimalnem zapisu, vrednost shranjeno v pomnilniški lokaciji X                                           |
| 1111                  | HALT        | prenehaj izvajanje programa                                                                                        |
# Turingov stroj
