1. Predpostavite , da register R ter pomnilniške celice 80 in 81 vsebujejo naslednje vrednosti:
	- R: 20,
	- pomnilniška celica 80: 43,
	- pomnilniška celica 81: 97.
	Te vrednosti se nahajajo v registru oz. obeh pomnilniških celicah pred izvedbo vsakega izmed spodnjih ukazov zbirnega jezika.
	
	 Ugotovite, kakšne so vrednosti v registru in obeh pomnilniških celicah po izvedbi vsakega izmed ukazov.
	 - LOAD 80
	 - STORE 81
	 - COMPARE 80
	 - ADD 81
	 - IN 80
	 - OUT 80
```spoiler-markdown
|            | R   | M(80)            | M(81) |
| ---------- | --- | ---------------- | ----- |
|            | 20  | 43               | 97    |
| LOAD 80    | 43  | 43               | 97    |
| STORE 81   | 20  | 43               | 20    |
| COMPARE 80 | 20  | 43; GT=1         | 97    |
| ADD 81     | 117 | 43               | 97    |
| IN 80      | 20  | vhodna vrednost  | 97    |
| OUT 80     | 20  | 43; izpiše se 43 | 97    |
```

2. Predpostavite , da register R ter pomnilniške celice 50 in 55 vsebujejo naslednje vrednosti:
	- R: 100, 
	- pomnilniška celica 50: 90,
	- pomnilniška celica 55: 35. 
	Te vrednosti se nahajajo v registru oz. obeh pomnilniških celicah pred izvedbo vsakega izmed spodnjih ukazov zbirnega jezika. Ugotovite, kakšne so vrednosti v registru in obeh pomnilniških celicah po izvedbi vsakega izmed ukazov:
	- STORE 50
	- ADD 55
	- CLEAR 55
	- INCREMENT 55
	- DECREMENT 50
	- SUBTRACT 50

```spoiler-markdown
|              | R:100 | 50: 90 | 55: 35 |
| ------------ | ----- | ------ | ------ |
| STORE 50     | 100   | 100    | 35     |
| ADD 55       | 135   | 90     | 35     |
| CLEAR 55     | 100   | 90     | 0      |
| INCREMENT 55 | 100   | 90     | 36     |
| DECREMENT 50 | 100   | 89     | 35     |
| SUBTRACT 50  | 10    | 90     | 35     |
```

3. Predpostavite, da pomnilniška celica 50 vsebuje vrednost 4, oznaka L pa ustreza pomnilniški lokaciji. Katero vrednost v register R naloži vsak izmed naslednjih ukazov LOAD?
	- LOAD 50
	- LOAD 4
	- LOAD L
	- LOAD L+1 (predpostavimo da je operacija dovoljena)

```spoiler-markdown
- LOAD 50 $\rightarrow$ 4
- LOAD 4 $\rightarrow$ kopija vsebine 4. pomnilniške celice
- LOAD L $\rightarrow$ 4, saj je L ekvivalenten pomnilniški celici 50
- LOAD L+1 $\rightarrow$ kopija vsebine 51. pomnilniške celice
```

4. Dan je naslednji program v strojnem jeziku, tabela simbolov in tabela kod ukazov.
	Operacijska koda ukaza je 4 bitna, naslovi 12 bitni. Kakšen je ustrezen program v zbirniku?
	- 0101001100001100 
	- 0011000000000111

```spoiler-markdown
0101001100001100 - operacija[0101] & naslov[001100001100] - SUBTRACT 780

0011000000000111 - operacija[0011] & naslov[000000000111] - ADD 7
```

5.  Z uporabo nabora ukazov s predavanj prevedite naslednje algoritmične operacije v zbirni jezik. Zapišite tudi vse potrebne psevdo-ukaze .DATA
	Če x > 50 
		izpiši vrednost x 
	sicer 
		preberi novo vrednost x 
	
	Predpostavimo da je X-u predhodno bila prirejena vrednost

```spoiler-markdown
LOAD FIFTY
COMPARE X
JUMPGT THEN
IN X
JUMP DONE
THEN: OUT X
DONE: naslednji ukaz

X: .DATA 0
FIFTY: .DATA 50
```

6. Recimo, da posamezen program med izvajanjem 50% svojega časa porabi za čakanje na zaključek vhodno/izhodnih operacij.
	- Kolikšen je odstotek časa, v katerem procesor opravlja koristno delo (oz. kolikšen je t.i. izkoristek procesorja), če so v pomnilniku naloženi trije programi?
	- Koliko programov bi morali imeti v pomnilniku, če bi želeli doseči vsaj 95% izkoristek procesorja?

```spoiler-markdown
$(\frac{1}{2})^3 = \frac{1}{8}$
Verjetnost, da vsi čakajo na zaključek operacije je $\frac{1}{8}$ oz. 12,5%, torej procesor opravlja koristno delo 87,5% časa.

št programov: $(\frac{1}{2})^x \le \frac{5}{100} oz. \frac{1}{20} \implies$$2^x \ge 20 \implies \log_2{20} \le x \implies x = 5$
```

7. Predpostavite da register R ter pomnilniške celice 50 in 55 vsebujejo naslednje vrednosti:
	- R: 45, 
	- pomnilniška celica 50: 115,
	- pomnilniška celica 55: 23.
	Te vrednosti se nahajajo v registru oz. obeh pomnilniških celicah pred izvedbo vsakega izmed spodnjih ukazov zbirnega jezika. Ugotovite, kakšne so vrednosti v registru in obeh pomnilniških celicah po izvedbi vsakega izmed ukazov.
	- LOAD 50
	- INCREMENT 55
	- COMPARE 55
	- ADD 50
	- DECREMENT 50
	- OUT 55


|              | R: 45 | 50: 115 | 55: 23           |
| ------------ | ----- | ------- | ---------------- |
| LOAD 50      | 115   | 115     | 23               |
| INCREMENT 55 | 45    | 115     | 24               |
| COMPARE 55   | 45    | 115     | 23; LT = 1       |
| ADD 50       | 160   | 115     | 23               |
| DECREMENT 50 | 45    | 114     | 23               |
| OUT 55       | 45    | 115     | 23; izpiše se 23 |
8. Dan je naslednji program v strojnem jeziku, tabela simbolov in tabela kod ukazov. Operacijska koda ukaza je 4 bitna, naslovi 12 bitni. Kakšen je ustrezen program v zbirniku?
	- 0100001000001001
	- 0111001101111100

```spoiler-markdown
0100001000001001 - op code[0100] & naslov[001000001001] - INCREMENT 521

0111001101111100 - op code[0111] & naslov[001101111100] - COMPARE 892
```

9. Z uporabo nabora ukazov s predavanj prevedite naslednje algoritmične operacije v zbirni jezik. Zapišite tudi vse potrebne psevdo-ukaze .DATA
	vsota = 0
	I = 0
	Dokler I < 50, ponavljaj 
		vsota = vsota + I
		I = I + 1

```spoiler-markdown
LOAD ZERO
STORE SUM
STORE I
LOOP: LOAD FIFTY
	  COMPARE I
	  JUMPEQ DONE
	  LOAD SUM
	  ADD I
	  STORE SUM
	  INCREMENT I
	  JUMP LOOP
DONE: naslednji ukaz

SUM: .DATA 0
I: .DATA 0
ZERO: .DATA 0
```

---

1. Kakšna je desetiška vrednost 8-bitne dvojiške količine 10101000, če jo tolmačimo kot
	- nepredznačeno celo število
	- predznačeno celo število, predstavljeno v zapisu predznak in velikost?

```spoiler-markdown
1. 10101000 - 8 + 32 + 128 = 168
2. 10101000 - (8 + 32) \* (-1) = - 40 
```

2. Kako bi v dvojiški obliki s pomočjo osmih bitov zapisali nepredznačeno desetiško vrednost 97?

```spoiler-markdown
97 - 01100001
```

3. Kako izgledajo predznačena cela števila -300 in +254 v dvojiški obliki, če uporabimo 10 bitov in obliko zapisa predznak in velikost?

```spoiler-markdown
- 300 - 1100101100
+ 254 - 0011111110
```

4. Izvedite naslednje 5-bitno dvojiško seštevanje, pri tem zapisujte tudi bit za prenos. Predpostavite, da sta obe števili nepredznačeni.
	01110+01011
```spoiler-markdown
11001
```

5. Kako izgledata predznačeni desetiški vrednosti +6 in -3, če ju zapišemo s 4 biti v obliki dvojiškega komplementa?

```spoiler-markdown
+6 - 0110
-3 - 0011 (3) - 1100 + 1 = 1101
```

6. Kako izgleda predznačena desetiška vrednosti -34, če jo zapišemo z 8 biti v obliki dvojiškega komplementa?

```spoiler-markdown
-34 - 00100010 (34) - 11011101 + 1 = 11011110
```

7. Kakšna je notranja predstavitev naslednjih dveh vrednosti, v primeru, da 10 bitov namenimo za mantiso (v zapisu predznak in velikost) in 6 bitov za eksponent (prav tako v zapisu predznak in velikost)? Najmanj koliko bitov potrebujemo za zapis mantise in eksponenta, da ne izgubimo natančnosti?
	- + 0,25
	- − 32 $\frac{1}{16}$

```spoiler-markdown
+0,25 = 0,01 - mantisa = 0010000000, eksponent = 100001; minumum: mantisa 2b & eksponent 2b

- 32 $\frac{1}{16}$ = 1100000,0001 - mantisa
  = 1100000000, eksponent = 000110;
  minimum: mantisa 11b & eksponent 4b
```

8. Kakšna je notranja predstavitev niza "X+Y" (brez narekovajev), če se uporabi 8-bitna koda ASCII? Kakšna pa je v primeru, ko uporabimo 16-bitni [UNICODE](http://unicode-table.com)?

```spoiler-markdown
- X BIN: 88 -> 0101 1000 | HEX: 0058 - 0000 0000 0101 1000
- \+ BIN: 43 -> 0010 1011 | HEX: 002B - 0000 0000 0010 1011
- Y BIN: 89 -> 0101 1001 | HEX: 0059 - 0000 0000 0101 1001
```

9. Koliko bitov je potrebnih za shranjevanje triminutne pesmi, če uporabljamo zvočno kodiranje, ki vzorči s frekvenco 40.000 Hz in ima bitno globino 16, pri tem pa se stiskanje podatkov ne izvaja? Koliko bitov pa potrebujemo, če uporabimo metodo stiskanja s stopnjo stiskanja 5:1?

```spoiler-markdown
št_bitov = $40.000 * 16 * 3 * 60 = 115.200.000b = 14.400.000B \sim 14MB$
stiskanje = št_bitov $* \frac{1}{5} = 23.040.000b$
```

10. Koliko bitov je potrebnih za shranjevanje barvne slike v formatu RGB velikosti 1.200 x 800 slikovnih elementov, če se stiskanje podatkov pri tem ne izvaja? Kakšna pa bi bila stopnja stiskanja, če bi sliko stisnili in bi le-ta zavzela 2,4 Mb prostora?

```spoiler-markdown
velikost = $1.200*800*3*8 = 23.040.000b$

2,4 ... 1
23,04 ... x

$x = \frac{23,04}{2,4} = 9,6 \sim 10$
Stopnja stiskanja bi bila 10:1
```

---

# Turingov stroj

1. Podan je ukaz za Turingov stroj (1,1,0,2,L) in konfiguracija: ... b 1(1) 0 b... Zapišite novo konfiguracijo.

```spoiler-markdown
![[Drawing 2025-11-13 14.25.29.excalidraw]]
```

2. Turingov stroj vsebuje le naslednji pravili:
	(1,1,1,1,R)
	(1,b,1,2,R)
	Ali lahko ta stroj doseže naslednjo konfiguracijo?
	b01(1)b

```spoiler-markdown
![[Drawing 2025-11-13 14.29.00.excalidraw]]
```

3. Poiščite izhod, ki ga vrne Turingov stroj s pravili
	(1,1,1,2,R)
	(1,0,0,2,R)
	(1,b,1,2,R)
	(2,0,0,2,R)
	(2,1,0,1,R)
	če so na traku vhodni podatki:
	...b1001b...

```spoiler-markdown
![[Drawing 2025-11-13 14.32.32.excalidraw]]
```

4. Poiščite izhod, ki ga vrne Turingov stroj s pravili
	(1,1,1,2,L)
	(2,b,0,3,L)
	(3,b,1,4,R)
	(4,0,1,4,R)
	če so na traku podatki:
	...b1b...

```spoiler-markdown
![[Drawing 2025-11-13 14.39.49.excalidraw]]
```

5. Napiši pravila za Turingov stroj, ki pri vhodu ...b11111b... ustvari izhod ...b01111b...

```spoiler-markdown
![[Drawing 2025-11-13 14.45.23.excalidraw]]
```

6. Napišite pravila za Turingov stroj, ki poljuben niz enk na vhodu spremeni v izhodni niz, v katerem se izmenjujeta številki 1 in 0.

```spoiler-markdown
![[Drawing 2025-11-13 14.47.33.excalidraw]]
```

7. Nariši diagram stanj za Turingov stroj, ki poljuben niz enk obdela tako, da vsako tretjo enko spremeni v ničlo.

```spoiler-markdown
![[Drawing 2025-11-13 14.49.52.excalidraw]]
```

8. Podan je Turingov stroj s pravili:
	(1,1,1,1,R)
	(1,0,0,2,L)
	(2,1,0,2,L)
	(2,b,1,3,L)
	(3,b,b,1,R)
	in tak s podatki:
	...b101b...
	Simuliraj delovanje Turingovega stroja, dokler se vsak ukaz ne izvede vsaj enkrat. Opiši rekurzivno obnašanje Turingovega stroja.

```spoiler-markdown
![[Drawing 2025-11-13 14.53.30.excalidraw]]
```

9. Turingov stroj je podan z diagramom prehajanja stanj:
	![[Pasted image 20251113145924.png]]
	Katera so pravila tega stroja?
	V kaj se preslika ...b110100b...

```spoiler-markdown

```

---

# Kolokvij

1. Predpostavite, da register R ter pomnilniške celice 50 in 10 vsebujejo naslednje vrednosti: 
	- R: 50,
	- pomnilniška lokacija 50: 45,
	- pomnilniška lokacija 10: 50. 
	Te vrednosti se nahajajo v registru in obeh pomnilniških celicah pred izvedbo vsakega izmed spodnjih ukazov zbirnega jezika. Ugotovite, kakšne so vrednosti v registru in obeh pomnilniških celicah po izvedbi vsakega izmed ukazov.
	- COMPARE 10
	- INCREMENT 50
	- DECREMENT 50
	- LOAD 10
	- CLEAR 10
	- SUBTRACT 10


```spoiler-markdown
|              | R: 50 | 50: 45 | 10: 50     |
| ------------ | ----- | ------ | ---------- |
| COMPARE 10   | 50    | 45     | 50; EQ = 1 |
| INCREMENT 50 | 50    | 46     | 50         |
| DECREMENT 50 | 50    | 44     | 50         |
| LOAD 10      | 50    | 45     | 50         |
| CLEAR 10     | 50    | 45     | 0          |
| SUBTRACT 10  | 0     | 45     | 50         |
```

2. Na kakšen način so povezani jeziki z računskimi agenti?

```spoiler-markdown

```

3. V pomnilniku računalnika lahko shranimo natanko 128 slik ločljivosti 2048 ×1024 v formatu RGBA.
	- Izračunajte velikost pomnilnika v Gigabajtih 
	- Izračunajte najmanjšo možno velikost naslovnega registra
	Pomoč: 1KB = $2^{10}$ B, 1MB = $2^{20}$ B, 1GB = $2^{30}$ B

```spoiler-markdown
velikost = $128*2024*1024*4$B = $1.061.158.912B = \frac{1.061.158.912}{2^{30}} = 0,988 \sim 1GB$

$\log_{2}(2^{30}) = 30$
```

4. Pretvori desetiško število -33 v dvojiško obliko predstavljeno z dvojiškim komplementom z osmimi biti.

```spoiler-markdown
dvojiški komplement:
-33: 00100001 (33) -inventiraj-> 11011110 + 1 = 11011111 = -33
```

5. Pretvorite desetiško število 129,25 v binarno vrednost v znanstvenem zapisu, kjer 8 bitov namenimo za mantiso in 6 za eksponent. Mantisa in eksponent sta zapisana v obliki predznak in velikost. Nato pretvori zapis mantise in eksponenta nazaj v decimalno vrednost.

```spoiler-markdown
129 = 010000001; 0,25 = 0,01; 129,25 = 010000001,01
mantisa = 01000000101 (imamo le 8 bitov)
mantisa(8b) = 01000000
eksponent(6b) = 001000

decimalna vrednost: 128
```

6. Predpostavite, da register R ter pomnilniške celice 20 in 22 vsebujejo naslednje vrednosti: 
	- R: 50,
	- pomnilniška lokacija 20: 35,
	- pomnilniška lokacija 22: 100. 
	Te vrednosti se nahajajo v registru in obeh pomnilniških celicah pred izvedbo vsakega izmed spodnjih ukazov zbirnega jezika. Ugotovite, kakšne so vrednosti v registru in obeh pomnilniških celicah po izvedbi vsakega izmed ukazov.
	- DECREMENT 20
	- INCREMENT 22
	- SUBTRACT 20
	- LOAD 22
	- CLEAR 20
	- ADD 22


```spoiler-markdown
|              | R: 50 | 20: 35 | 22: 100 |
| ------------ | ----- | ------ | ------- |
| DECREMENT 20 | 50    | 34     | 100     |
| INCREMENT 22 | 50    | 35     | 101     |
| SUBTRACT 20  | 15    | 35     | 100     |
| LOAD 22      | 100   | 35     | 100     |
| CLEAR 20     | 50    | 0      | 100     |
| ADD 22       | 150   | 35     | 100     |
```

7. Opiši ključno razliko med izbirnikom in dekodirnikom.

```spoiler-markdown

```

8. Katero število v desetiškem sistemu predstavlja binarno število 01111100 v zapisu dvojiški komplement?

```spoiler-markdown
dvojiški komplement
01111100 = 124
```

9. Kakšna bo vrednost spremenljivke “SUM” in “I” po zaključku algoritma? Utemelji odgovore!

```
LOAD ZERO
STORE SUM
STORE I
LOOP: LOAD TEN
	  COMPARE I
	  JUMPEQ DONE
	  LOAD SUM
	  ADD I
	  STORE SUM
	  INCREMENT I
	  JUMP LOOP
DONE: naslednji ukaz

SUM: .DATA 10
I: .DATA 0
ZERO: .DATA 0
TEN .DATA 10
```

```spoiler-markdown
```cpp
sum = 0
i = 0
while(i < 10)
{
	sum = sum + i
	i++
}

cout << sum << i //sum = 45; i = 10
```

10. Za katere naloge skrbi operacijski sistem? Kako si predstavljate njegovo zgradbo?

```spoiler-markdown

```

11. Recimo, da ima trdi disk naslednje lastnosti: 
	- hitrost vrtenja: 7200 obratov / min
	- čas premika glave: 0,5 ms (fiksni začetni čas) + 0,05 ms za vsako sled
	- število površin: 2 (glavi obeh površin se pomikata sočasno)
	- število sledi na površino: 500
	- število sektorjev na sled: 20
	- število bajtov na sektor: 1000
	Koliko bajtov podatkov lahko shranimo na ta disk?
	Najmanj koliko sledi potrebujemo, da bi na disk shranili eno sliko v RGBA obliki z ločljivostjo 500x500?

```spoiler-markdown
bajti = $2*500*20*1000 = 20.000.000B$

bajti = $500*500*4 = 1.000.000B$
sledi = $\frac{1.000.000}{20*1000} = 50$ 
```

12. Operacijska koda ukaza je 4 bitna, naslovi 10 bitni. Kakšen bo strojni ukaz za naslednje operacijske kode? Ukaze pišite z velikimi črkami. Med operacijo in naslovom vstavite presledek.
	- 10010000001010
	- 00000000100001
	- 10110001000110

```spoiler-markdown
- JUMPGT 10
- LOAD 33
- JUMPLT 70
```

13. Kaj je tabela pravilnosti in po kakšnem postopku se jo sestavi?

```spoiler-markdown

```

14. Določi, ali so spodnje zahteve funkcionalne ali nefunkcionalne:
	- Prijava se izvede v največ pol minute.
	- Lastnik naroči pregled poslovanja.
	- Zaposleni naroči informativni izračun plače.
	- Kupec prejme potrdilo o nakupu v roku desetih minut.
	- Avtentikacija uporabnikov.

```spoiler-markdown
- Prijava se izvede v največ pol minute: nefunkcionalna
- Lastnik naroči pregled poslovanja: funkcionalna
- Zaposleni naroči informativni izračun plače: funkcionalna
- Kupec prejme potrdilo o nakupu v roku desetih minut: nefunkcionalna
- Avtentikacija uporabnikov: funkcionalna
```

15. Podane imamo naslednje inštrukcije za Turingov stroj, ki se nahaja v stanju 1:
```
(1,1,1,2,R)
(1,0,0,2,R)
(1,b,1,2,R)
(2,0,0,2,R)
(2,1,0,1,R)
```
v obliki (trenutno stanje, trenutni simbol, naslednji simbol, naslednje stanje, premik)In začetno stanje na traku, ki je naslednje: [ ... b 1 0 0 1 b ...].

Kakšno bo stanje na traku po preteku programa?

```spoiler-markdown
...b10001b...
```

16. Kateri ključni koncepti iz preteklosti so pripeljali do izuma računalnika?

```spoiler-markdown

```

17. Podan je Turingov stroj s pravili: 
```
(1, b, b, 2, L)
(1, 0, 1, 1, R)
(1, 1, 0, 1, R)
(2, 0, 1, 3, R)
(2, 1, 0, 2, L)
```
Poiščite izhod, ki ga vrne dani Turingov stroj, če so na traku naslednji vhodni podatki: b110100b
Katero operacijo izvede dani Turingov stroj nad binarnimi števili.

```spoiler-markdown
b001100b

Dvojiški komplement
```

18. Seštej števili 10000001 in 01000001, ki sta podani v dvojiškem komplementu. Kakšen je rezultat (prav tako v dvojiškem komplementu)?

```spoiler-markdown
 10000001
+01000001
 11000010
```

19. Operacijska koda ukaza je 4 bitna, naslovi 10 bitni. Kakšna bo operacijska koda za naslednje strojne ukaze?

```spoiler-markdown
| OP CODE      | BINARNO         |
| ------------ | --------------- |
| SUBTRACT 7   | 0101 0000000111 |
| ADD 32       | 0011 0000100000 |
| DECREMENT 64 | 0110 0001000000 |
| INCREMENT 65 | 0100 0001000001 |
| OUT 130      | 1110 0010000010 |
```

20. V kratkih črtah opišite prihodnost programskega inženirstva. Kakšne aplikacije bomo razvijali v bodoče? Kakšne tehnologije bomo uporabljali v ta namen? Na kakšen način? Kakšne bodo zahteve novih aplikacij?

```spoiler-markdown

```

