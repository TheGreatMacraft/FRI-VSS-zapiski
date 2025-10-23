# Pametna specializacija

## Cilji
- pametne aplikacije
- področja pametne specializacije S4
- poslovni pogled na aplikacije
- programsko inženirstvo, življenjski ciklus programske opreme
- natančno:
	- definicija problema
	- uporabniške zgodbe
	- analiza zahtev (nizko in visokonivojske zahteve)
	- kakovost storitev
	- načrtovanje, razvoj,...
Zahteve aplikacij so:
- funkcionalne - aplikacija opravlja svojo nalogo
- nefunkcionalne - aplikacija je dovolj hitra, ...
- sistemske - produkt ima dovolj prostora, ...  
- visokonivojska/zaupljiovst
Zahteve moramo točno določiti, preden se lotimo izdelovanja produkta/programa.
DevOps - sprotno nadgrajevanje sistema, brez da bi ta nehal delovati

## Pametne aplikacije
- običajno temeljijo na internetu stvari, umetni inteligenci, računalništvu v oblaku, na robu in v megli ter na tehnologijah veriženja blokov
- aplikacije, ki imajo še posebej izražene uporabniške, aplikacijske in sistemske zahteve
- Microstoritve
- orkestracija aplikacijskih komponent, mikrostoritev - kontejnerje lahko prenašamo med računalniki ves čas

### Področja pametne specializacije
- nacionalni in Evropski raziskovalni ter inovacijski program
- podobne programe imajo tudi druge napredne države: ZDA, J. Koreja, Japonska, Avstrija ipd.
- v Slovenskem programu je 8 aplikacijskih domen
- program je vil razvit v zadnjih letih in temelji na nenehnem podjetniškem procesu odkrivanja
- Slovenska strategija pametne specializacije: Zdravje, Gospodarstvo, Mobilnost, Javne storitve, Energija in trajnost, novice, mediji ter zabava, industrija, turizem, izobraževanje in izmenjava znanja
## Zdravje

- glej powerpoint
# Analiza zahtev

---
# Vaje

## Teme
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

4. 