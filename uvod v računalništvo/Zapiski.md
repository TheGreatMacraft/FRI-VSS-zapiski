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