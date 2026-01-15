1. Predpostavite, da cela števila zapisujemo s 16 biti. Zapišite desetiški števili 3012 in -435 v dvojiških zapisih z odmikom in v dvojiškem komplementu.
```spoiler-markdown
![[Drawing 2025-10-24 08.17.56.excalidraw]]
```
2. Zapišite števili 3012 in -435 v dvojiškem komplementu z 32 biti.
```spoiler-markdown
![[Drawing 2025-10-24 09.03.57.excalidraw]]
```

3. Pretvori -200 in 259 v dvojiški komplement. Kolikšno je minimalno potrebno število bitov?
```spoiler-markdown
![[Drawing 2025-10-24 09.09.58.excalidraw]]
```

4. Katere desetiške vrednosti predstavljata binarna zapisa 0100100101 in 1111101001, če ju interpretiramo kot:
- nepredznačeni celi števili
- predznačeni števili v zapisu predznak in velikost (sign-magnitude)
- predznačeni števili v zapisu z odmikom (offset/bias)
- predznačeni števili v dvojiškem komplementu (two’s complement)

```spoiler-markdown
![[Drawing 2025-10-24 09.24.02.excalidraw]]
```

5. Pretvori 0xFF3E v binarno in poišči desetiško vrednost, če je to dvojiški komplement.

```spoiler-markdown
![[Drawing 2025-10-24 09.38.42.excalidraw]]
```

6. Pretvori 17.0625 v binarno.

```spoiler-markdown
![[Drawing 2025-10-24 09.42.24.excalidraw]]
```

7. Pretvori 0.1 v binarno.

```spoiler-markdown
![[Drawing 2025-10-24 09.46.44.excalidraw]]
```

8. Pretvori 0.2 v binarno.

```spoiler-markdown
![[Drawing 2025-11-16 14.13.26.excalidraw]]
```

9. Pretvori 0.01 v binarno.

```spoiler-markdown
![[Drawing 2025-11-16 14.20.57.excalidraw]]
```

10. Pretvori 3.296875 v binarno.

```spoiler-markdown
![[Drawing 2025-11-16 14.35.22.excalidraw]]
```

11. Zapišite -35.6875 v IEEE754 z enojno natančnostjo.

```spoiler-markdown
![[Drawing 2025-11-16 14.46.55.excalidraw]]
```

12. Zapišite 43.11 v IEEE754 z enojno natančnostjo.

```spoiler-markdown
![[Drawing 2025-11-16 14.56.02.excalidraw]]
```

13. Binarno število 0.10101010101010... zapišite kot 32-bitno IEEE754 število

```spoiler-markdown
![[Drawing 2025-11-16 15.18.23.excalidraw]]
```

14. Številu iz prejšnje naloge določi desetiško vrednost.

```spoiler-markdown
![[Drawing 2025-11-16 15.36.42.excalidraw]]
```
15. Seštej 8-bitni nepredznačeni števili 0x85 in 0x13.

```spoiler-markdown
![[Drawing 2025-11-16 15.32.36.excalidraw]]
```

16. Seštej 8-bitni števili 120 in 57 v dvojiškem komplementu.

```spoiler-markdown
![[Drawing 2025-11-16 15.43.45.excalidraw]]
```

17. Seštej 8-bitni števili 0xF0 in 0x35. Kaj znate povedati o rezultatu, če ju interpretiramo kot predznačeni v dvojiškem komplementu in nepredznačeni.

```spoiler-markdown
![[Drawing 2025-11-16 15.46.50.excalidraw]]
```

18. Binarno zmnožite binarni števili 0xD in 0x3.

```spoiler-markdown
![[Drawing 2025-11-16 15.54.31.excalidraw]]
```

19. Zmnožite binarni števili 0x41 in 0x92.

```spoiler-markdown
![[Drawing 2025-11-16 16.00.05.excalidraw]]
```

20. Zmnožite binarni števili 0x37 in 0x07.

```spoiler-markdown
![[Drawing 2025-11-16 17.33.34.excalidraw]]
```

21. Seštej dve števili v dvojiškem komplementu: 0x71AC in 0x82.

```spoiler-markdown
![[Drawing 2025-11-16 17.39.23.excalidraw]]
```

22. Binarnim številom v dvojiškem komplementu 0xD in 0x5 spremeni predznak

```spoiler-markdown
![[Drawing 2025-11-16 17.54.44.excalidraw]]
```

23. Seštej števili 0x40300000 in 0x42400000, ki sta zapisani v 32-bitnem IEEE754 zapisu.

```spoiler-markdown
![[Drawing 2025-11-16 17.57.32.excalidraw]]
```

24. Seštej števili 0x40700000 in 0x407F0000, ki sta zapisani v 32-bitnem IEEE754 zapisu

```spoiler-markdown
![[Drawing 2025-11-16 17.57.32.excalidraw]]
```

25. Seštej števili 0x45B00000 in 0x4400000C, ki sta zapisani v 32-bitnem IEEE 754 zapisu.

```spoiler-markdown

```

# Assembly
1. Napiši program, ki sešteje dve števili.
```spoiler-markdown
.global _start
.text
.org 0x00000000

_start:

	ldr r0,=a
	ldr r1, [r0]
	ldr r0,=b
	ldr r2, [r0]
	
	add r3,r1,r2
	
	ldr r0,=rez
	str r3,[r0]
	
_end:
	B _end
	
.data
a:	.word 0x12
b:	.word 0x24
rez: .word 0x0
```

2. Za števila iz prejšnje naloge predpostavi, da so 8-bitna (.byte). Izračunaj vsoto STEV1 + STEV2 in jo shrani v pomnilniku na naslov REZ. Preveri zapise spremenljivk v pomnilniku in ugotovi na katerih naslovih se nahajajo.
```spoiler
.global _start
.text
.org 0x00000000

_start:

	ldr r0,=a
	ldrb r1, [r0]
	ldr r0,=b
	ldrb r2, [r0]
	
	add r3,r1,r2
	
	ldr r0,=rez
	strb r3,[r0]
	
_end:
	B _end
	
.data
a:	.word 0x12
b:	.word 0x24
rez: .word 0x0
```
3. Podani sta števili STEV1 = 183, STEV2 = - 97.
	- Pretvori števili v zapis v dvojiškem komplementu (32 bitov).
	- V programu ju podaj v šestnajstiškem zapisu in izračunaj vsoto REZ = STEV1 + STEV2.
	- V programu (CPUlator) preveri rezultate v registrih in v pomnilniku.
```spoiler
128+32+16+4+2+1 = 183
10110111 = B7

64+32+1 = 97
01100001 = 97
10011111 = FFFFFF9F

56 = 01010110
2+4+16+64 = 86

---

.global _start
.text
.org 0x00000000

_start:

	ldr r0,=a
	ldr r1, [r0]
	ldr r0,=b
	ldr r2, [r0]
	
	add r3,r1,r2
	
	ldr r0,=rez
	str r3,[r0]
	
_end:
	B _end
	
.data
a:	.word 0xB7
b:	.word 0xFFFFFF9F
rez: .word 0x0
```

---
- \#ime_spremenljivke
- \#0b01 = 1 (bitni zapis)
- \#0x0F = 15 (hexadecimalni zapis)
- \#(2) = 2 (direktna vrednost)
- \#(1<<5) = 0b00100000 =  32 (bit shift)

# UKAZI IN ARITMETIČNO LOGIČNE OPERACIJE
- MOV r0, r1 $\implies$ @ r0 $\leftarrow$ r1
- ADD r0, r1, #1 $\implies$ @ r0 $\leftarrow$ r1 + 1
- ADC r2, r2, #1 $\implies$ @ r2 $\leftarrow$ r2 + 1 + C (carry bit) - sešteva z bitom prenosa
- CMP r0, #8 $\implies$ (rezultat odštevanja je enak 0 (sta enaka)): N=0, Z=1, C=1 (operanda sta enaka), V=0
	C = 1, N=0, Z=0; če Rn $\ge$ Operand2
	C = 0, N=1, Z=0; če Rn < Operand2
	C = 0, N=0, Z=1; če Rn = Operand2
## Logične Operacije
- AND r0, r1, \#0x0F $\implies$ r0 $\leftarrow$ r1 AND \#0x0F
	Rezultat je 1, kjer sta istoležna bita **oba** 1, sicer je 0.
- ORR r0, r1, \#(02) $\implies$ r0 $\leftarrow$ r1 ORR \#(02)
	Rezultat je 0, kjer sta istoležna bita **oba** 0, sicer je 1.
- EOR r0, r1, \#0b00111100  r0 $\leftarrow$ r1 EOR \#0b00111100
	Rezultat je 1, kjer sta istoležna bita različna in je enak 0, kjer sta istoležna bita enaka.
- TST r0, #(1<<5) 
	Test, ki izvede operacijo AND in nastavi zastavice (rezultat se nikjer ne zapiše)
	- Z=1 $\Longleftrightarrow$ r0 AND #(1<<5) == 0
	- N = 1 $\Longleftrightarrow$ r0 AND #(1<<5) < 0
	Z pove ali je rezultat 0, N pa ali je negativen (najvišji bit je 1)
- MVN r0, #0 $\implies$ r0 = NOT(0x00000000) $\implies$ r0 = 0xFFFFFFFF
	Zamenja vse bite drugega operanda in rezultat zapiše v prvi operand.

# Floating point IEEE 754
32 bitna - 1 znak bit (1$\rightarrow$ -, 0$\rightarrow$ +), 8 bitov eksponent, 23 bitov mantisa.
Zapis števila: 1.mantisa x $2^{PraviEksponent}$
Eksponent: 127 + PraviEksponent

Primer: -1,9375 = 1,1111

Rezultat: 1(predznak) 01111111 (eksponent) 11110000000000000000000 (mantisa) = 0xBFF80000


1. Napišite zaporedje ukazov v zbirniku za arhitekturo ARMv7, ki zamenja vrednosti 32- bitnih spremenljivk STEV1 = -1.9375 in STEV2 = 35.6875. Števili najprej pretvorite v zapis s plavajočo vejico (IEEE754). Rezultat iz šestnajstiškega zapisa pretvorite v decimalno število.

-1.9375 = 1,1111 x $2^0$ = 1 01111111 11110000000000000000000 = 0xBFF80000
35,6875 = 100011,1011 = 1,000111011 $* 2^5$ = 0 10000100 00011101100000000000000 = 0x420EC000

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=a
ldr r1,=b

ldr r2, [r0]
ldr r3, [r1]

str r2, [r1]
str r3, [r0]

_end:
        B _end


        .data
a:  	.word  0xBFF80000
b:		.word  0x420EC000

```

2. Zapišite ukaz(e) v zbirniku za procesor ARM, ki v podan register naloži vrednost spremenljivke:
	- naloži 32-bitno vrednost 0x12345678 v register R1
	- naloži 8-bitno vrednost 128 v register R1.
	- naložimo 16-bitno vrednost 0xF123 v register R1.

```spoiler-markdown
ldr r1, =0x12345678
ldrb r1, #128
ldrh r1, =0xF123
```

3. Napišite program v ARM zbirniku, ki izračuna naslednji izraz: rez = (a + b) - (c - d), in shrani rezultat. Vse spremenljivke so 32 bitne in imajo naslednje vrednosti:
	- a = 32, b = 16, c= 12, d = 24
	- a = - 257, b = -16, c = -68, d = 34 
	V CPUlator vpišite spremenljivke v šestnajstiškem zapisu.

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=a1

ldr r1, [r0]
ldr r2, [r0,#4]
ldr r3, [r0,#8]
ldr r4, [r0,#12]

add r5,r1,r2
sub r6,r3,r4
sub r7,r5,r6

_end:
        B _end


        .data
a: 		.word 0x20
b:		.word 0x10
c: 		.word 0x0c
d:		.word 0x18

a1: 	.word 0xfffffeff
b1:		.word 0xfffffff0
c1: 	.word 0xffffffbc
d1:		.word 0x00000022
```

4. Napišite zaporedje ukazov v zbirniku za ARMv7, ki izračuna negativno vrednost števila a = 56 z dvojiškim komplementom in shrani rezultat v spremenljivko b. Namig: uporabite XOR operacijo.

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=a
ldr r1, [r0]
ldr r2, [r0,#4]

eor r3,r1,r2
add r3,r3,#1

_end:
        B _end


        .data
a: 		.word 0x00000038
full: 	.word 0xffffffff
```

5. Rezervirajte prostor za tabelo z oznako TABELA, v kateri bo zapisanih 5 8-bitnih vrednosti (bajtov). Nato napišite zaporedje ukazov v zbirniku za ARMv7, ki v vse bajte tabele zapiše vrednost 0xFF.

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=tabela
mov r1, #0xff

mov r2, #5

loop:
strb r1,[r0]
add r0,r0,#1
sub r2,r2,#1

cmp r2, #0
bne loop


_end:
        B _end


        .data
tabela: 	.space 5
```

6. Preverite delovanje ukazov CMP in TST za dva operanda (OP1, OP2), če uporabite desetiški števili 32 in 16. Izpišite rezultate zastavic N, Z, C, V iz registra CPSR (Current Program Status Register):
	- OP1 = OP2 (N = ; Z = ; C = ; V = )
	- OP1 > OP2 (N = ; Z = ; C = ; V = )
	- OP1 < OP2 (N = ; Z = ; C = ; V = )

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=a
ldr r1,[r0]
ldr r2,[r0,#4]

cmp r2,r1
mrs r3, CPSR

and r3,r3,#0xF0000000
str r3,[r0,#8]

tst r1,r2
mrs r3, CPSR

and r3,r3,#0xF0000000
str r3, [r0,#12]

_end:
        B _end


a:		.word 0x20
b:		.word 0x10
zastavice: .space 8
```

---

# Kviz 1

1. V spodnji ARMv7 kodi želimo prebrati vrednost spremenljivke `d` v register `r4`. Kakšen mora biti odmik (???) da bo ukaz `ldrb r4, [r3, ???]` pravilno bral iz spremenljivke `d`?

```asm
.global _start
.text
.org 0x00000000

_start:
    ldr r3, =a
    ldrb r4, [r3, ???]

_end:
    B _end

.data
a: .byte 0x01
b: .byte 0x02
empty: .space 4
c: .byte 0x03
d: .byte 0x04
e: .word 0xffffffff
```

- 0
- 8
- 7
- 4

```spoiler
7
```

2. Imam število `0x00000005` v 32-bitni plavajoči vejici po IEEE 754. Izberite pravilen odgovor:
	- Vrednost tega števila je 5
	- Število je pozitivno in denormalizirano
	- Število je negativno in normalizirano
	- Vrednost tega števila je -5

```spoiler
Število je pozitivno denormalizirano
```

3. Imamo dve binarni števili v dvojiškem komplementu: štiribitno `A=1010` in osembitno `B=11111010`. Izberi pravilno trditev:
	- A < B in imata obe števili enaki absolutni vrednosti
	- A > B in imata števili različni absolutni vrednosti
	- A < B in sta obe števili pozitivni
    - A = B

```spoiler
A=B
```

4. Imamo dve celi predznačeni binarni števili `A=1011` in `B=0101`, ki ju seštevemo. Izberi pravilno trditev:
	- rezultat je 1110 in pride do prenosa in preliva
	- rezultat je 0000 in pride do prenosa, ne pa do preliva
	- rezultat je 0000 in ne pride do preliva in prenosa
	- rezultat je 1111 in ne pride do prenosa

```spoiler-markdown
Rezultat je 0000, pride do prenosa, ne pa do preliva.
```

5. Predpostavite, da imamo v registru `r7` vrednost `-2` in v registru `r2` vrednost `0xfffffffe`. Kaj bo vrednost zastavic po izvedbi ukaza `CMP r2, r7`?
	- Zastavici C in N bosta nastavljeni (C=1, N=1), zastavica Z pa bo počiščena (Z=0)
    - Zastavici N in C bosta počiščeni, zastavica Z bo nastavljena (C=0, N=0, Z=1)
    - Zastavice C in Z bosta nastavljene (C=1, N=1, Z=1)
    - Zastavica N bo počiščena, zastavici C in Z bosta nastavljeni (C=1, N=0, Z=1)

```spoiler-markdown
Zastavici N in C bosta počiščeni, zastavica Z bo nastavljena (C=0, N=0, Z=1)
```

6. Predpostavite, da imamo v registru `r7` vrednost `12` in v registru `r2` vrednost `3`. Kaj bo vrednost zastavic po izvedbi ukaza `CMP r7, r2`?
	- Zastavica C bo nastavljena (C=1), zastavica N bo počiščena (C=1, N=0)
    - Zastavici C in N bosta nastavljeni (C=1, N=1)
    - Zastavici C in N bosta počiščeni (C=0, N=0)
    - Zastavica C bo počiščena (C=0), zastavica N bo nastavljena (C=0, N=1)

```spoiler-markdown
Zastavica C bo nastavljena (C=1), zastavica N bo počiščena (C=1, N=0)
```

7. Za spremenljivke
```
A: .word 0x1f2e3d4c  
B: .word 0xaabbccdd  
C: .word 0x55667788  
```
ki so v pomnilniku shranjene ena za drugo, izberi pravilen niz ukazov, da bo spremenljivka `C` shranjena na naslovu `A`.
	- ldr r0,=C; ldr r1,[r0,#0]; str r1,[r0,#8]
    - ldr r0,=A; ldr r1,[r0,#8]; str r1,[r0,#0]
    - ldr r0,=A; ldr r1,[r0,#0]; str r1,[r0,#4]
    - ldr r0,=A; ldr r1,[r0,#0]; str r1,[r0,#8]

```spoiler-markdown
ldr r0,=A; ldr r1,[r0,#8]; str r1,[r0,#0]
```

8. V spodnji ARMv7 kodi želimo prebrati vrednost spremenljivke `e` v register `r4`. Kakšen mora biti odmik (???) da bo ukaz `ldr r4, [r3, ???]` pravilno bral iz spremenljivke `e`?

```asm
.global _start
.text
.org 0x00000000

_start:
    ldr r3, =a
    ldr r4, [r3, ???]

.end:

.data
a: .byte 0x01
b: .byte 0x02
empty: .space 4
c: .byte 0x03
d: .byte 0x04
e: .word 0xffffffff
```

- 8
- 4
- 6
- 9

```spoiler-markdown
8
```

9. Kaj naredi ukaz `str r1, [r6, #8]`?
	- Prenese 8-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8
    - Prenese 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je shranjen v r6+8
    - Prenese 32-bitno spremenljivko iz r6 v pomnilniško besedo, katere naslov je r1+8
    - Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8

```spoiler-markdown
Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8
```

10. Kaj naredi ukaz `strb r1, [r5, #-16]`?
	- Shrani 8-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r5+16
    - Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r5-16
    - Shrani 8-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r5-16
    - Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r5+16

```spoiler-markdown
Shrani 8-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r5-16
```

11. Imamo dve binarni števili v 32-bitnem zapisu s plavajočo vejico: A = `01000100101010001110000000000011` B = `11000100011000011100000000001111` Izberi pravilno trditev:
	- A < B in sta obe števili negativni
    - A < B in sta različno predznačeni
    - A > B in sta obe števili pozitivni
    - A > B in sta različno predznačeni

```spoiler-markdown
A > B in sta različno predznačeni
```

12. Imamo dve binarni števili v dvojiškem komplementu: štiribitno `A=1001` in osembitno `B=11111000`. Izberi pravilno trditev:
	- A = B = 1
    - A = B = 0
    - A = 8, B = 248
    - A = B

```spoiler-markdown
Noben od odgovorov, B < A; B = -8, A = -7
```

13. Imamo dve celi predznačeni binarni števili `A=1000` in `B=1001`, ki ju seštejemo in zapišemo rezultat s 4 biti. Izberi pravilno trditev:
	- rezultat je 0001 in pride do preliva, ne pa do prenosa
    - rezultat je 1001 in pride do prenosa in preliva
    - rezultat je 0001 in ne pride do prenosa niti do preliva
    - rezultat je 0001 in pride do prenosa in preliva

```spoiler-markdown
rezultat je 0001 in pride do prenosa in preliva
```

14. Pri arhitekturi, ki uporablja 8 registrov in ima 3-operandne ukaze, koliko bitov potrebujemo za kodiranje registrov?
	- 9
    - 16
    - 32
    - 12

```spoiler-markdown
9
```

15. Predpostavite 32-bitno arhitekturo z 64 registri in 512 operacijskimi kodami. Kolikšen je lahko največji odmik v LOAD/STORE ukazih?
	- največ 14-bitni odmik
    - največ 16-bitni odmik
    - največ 18-bitni odmik
    - največ 11-bitni odmik

```spoiler-markdown
največ 11-bitni odmik
```

16. Predpostavite 32-bitno arhitekturo, kjer so ukazi 32-bitni, naslovi 32-bitni in pri kateri imamo za shranjevanje operandov v CPE 8 32-bitnih registrov. Arhitektura ima 128 različnih operacij ter za dostop do pomnilnika dovoljuje le bazno naslavljanje z odmikom. Zato bomo v ukazih LOAD/STORE lahko imeli:
	- največ 12 bitni odmik
    - največ 32 bitni odmik
    - največ 20 bitni odmik
    - največ 19 bitni odmik

```spoiler-markdown
največ 19 bitni odmik
```

17. Imamo dve binarni števili v dvojiškem komplementu: štiribitno `A=1010` in osembitno `B=11111010`. Izberi pravilno trditev:
	- A < B in sta obe števili pozitivni
    - A < B in imata obe števili enaki absolutni vrednosti
    - A > B in imata števili različni absolutni vrednosti
    - A = B

```spoiler-markdown
A=B
```

18. Pri arhitekturi, ki za shranjevanje operandov v CPE uporablja 8 registrov in ima 3-operandne ukaze, bomo v ukazih, ki izvedejo `reg1 <- (reg2 OP reg3)` potrebovali:
	- 16 bitov za kodiranje registrov
    - 32 bitov za kodiranje registrov
    - 12 bitov za kodiranje registrov
    - 9 bitov za kodiranje registrov

```spoiler-markdown
9 bitov za kodiranje registrov
```

19. Imam število `0x3F000000` v 32-bitni plavajoči vejici po IEEE 754. Izberite pravilen odgovor:
	- Vrednost tega števila je +0.3000000
    - Vrednost tega števila je -0.3000000
    - Vrednost tega števila je +0.3150000
    - Vrednost tega števila je +0.5000000

```spoiler-markdown
Vrednost tega števila je +0.5000000
```

20. Imamo dve binarni števili v IEEE 754 formatu enojne natančnosti: A = `0x80000000` B = `0x00000000` Izberi pravilno trditev:
	- A = B in sta števili normalizirani
    - A in B sta ničli
    - A < B in sta obe števili denormalizirani
    - A > B in sta obe števili denormalizirani

```spoiler-markdown
A in B sta ničli
```

21. Kaj naredi ukaz `str r1, [r6, #8]`?
	- Prenese 32-bitno spremenljivko iz r6 v pomnilniško besedo, katere naslov je r1+8. Pri tem uporabljamo bazno naslovljanje z odmikom.
    - Prenese 8-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8. Pri tem uporabljamo bazno naslovljanje z odmikom.
    - Prenese 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je shranjen v r6+8. Pri tem uporabljamo neposredno pomnilniško naslovljanje.
    - Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8. Pri tem uporabljamo bazno naslavljanje z odmikom.

```spoiler-markdown
Shrani 32-bitno spremenljivko iz r1 v pomnilniško besedo, katere naslov je r6+8. Pri tem uporabljamo bazno naslavljanje z odmikom.
```

22. Pri arhitekturi, ki za shranjevanje operandov v CPU uporablja registre in ima 3-operandne registrsko-registrske ukaze, imamo v ukazu 12 bitov za kodiranje registrov. Koliko splošnonamenskih registrov ima taka arhitektura?
	- 12
    - 9
    - 16
    - 32

```spoiler-markdown
16
```

---

# Skočni Ukazi

1. Za podane programe v zbirniku za procesor ARM izpišite zastavice N, Z, C, V in preverite kateri od naslednjih programov se vrti v zanki, če je podana 8-bitna spremenljivka a = 0x7F.

```asm
ZANKA A:
ldr r0, =a
ldrb r1, [r0]
cmp r1, #0
bne ZANKA

ZANKA B:
ldr r0, =a
ldrb r1, [r0]
tst r1, #0
beq ZANKA

ZANKA C:
ldr r0, =a
ldrb r1, [r0]
cmp r1, #0
ZANKA1:
mov r2, #0
tst r1, r2
bne ZANKA

ZANKA D:
ldr r0, =a
ldrb r1, [r0]
tst r1, #0
ZANKA1:
mov r2, #0
cmp r1, r2
beq ZANKA
```


```spoiler-markdown
|     | N   | Z   | C   | V   | Program se vrti v zanki |
| --- | --- | --- | --- | --- | ----------------------- |
| a)  | 0   | 0   | 1   | 0   | da                      |
| b)  | 0   | 1   | 0   | 0   | da                      |
| c)  | 0   | 0   | 1   | 0   |                         |
|     | 0   | 1   | 1   | 0   | ne                      |
| d)  | 0   | 1   | 0   | 0   |                         |
|     | 0   | 0   | 1   | 0   | ne                      |
```

2. Podana so tri 32-bitna števila vrednosti STEV 1 = 0xFFFFFEFD, STEV2 = 0x257A in STEV3 = 259. Napišite zaporedje ukazov v zbirniku za procesor ARM, ki preveri ali obstajata dve števili, ki imata enako absolutno vrednost in se razlikujeta po predznaku. Če obstajata takšni števili, potem v register R5 vpišite konstanto 2.

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=a
ldr r1,[r0]
ldr r2,[r0,#4]
ldr r3,[r0,#4]

add r4,r1,r2
cmp r4,#0
bne skip

mov r5,#2
skip:

add r4,r1,r3
cmp r4,#0
bne skip1

mov r5,#2
skip1:

add r4,r2,r3
cmp r4,#0
bne skip2

mov r5,#2
skip2:

_end:
        B _end


        .data
a:  	.word  0xfffffefd
b:		.word  0xFFFFEFDa
c:		.word  0x103

```

3. V pomnilniku je podanih sedem 8-bitnih vrednosti (bajtov):
	TABELA: 0x20, 0xF3, 0x2A, 0x4A, 0x48, 0x2C, 0x5F
	Napišite zaporedje ukazov v zbirniku za procesor ARM, ki preveri ali je v tabeli shranjena vrednost STEV=0x4A. Če jo najde, se izvajanje programa zaključi in v register R4 vpišite naslov na katerem se nahaja ta vrednost.

```spoiler-markdown
	    .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=tabela
mov r1, #0
ldrb r2, [r0,#7]

loop:

ldrb r3,[r0,r1]

cmp r3,r2
beq shrani

add r1,r1,#1
cmp r1,#7
beq _end
b loop


shrani:
add r4,r0,r1


_end:
        B _end


        .data
tabela: .byte 0x20, 0xF3, 0x2A, 0x4A, 0x48, 0x2C, 0x5F
stev: 	.byte 0x4a

```

---

1. Napišite zaporedje ukazov v zbirniku za processor ARM, ki izračuna izraz STEV1 = MAKS(STEV2, STEV3). Vse spremenljivke so 32-bitne in nepredznačene. Program preizkusite z vrednostmi STEV2 in STEV3:
	- STEV2 = 10, STEV3 = 25
	- STEV2 = 0xF0000002, STEV3 = 0xF0000000 
	Uporabite pogojni skok. Program naj bo naslednje oblike: 
	STEV1 = STEV2 
	IF STEV2 > STEV3 THEN GOTO DALJE 
	STEV1 = STEV3
	DALJE:

```spoiler-markdown
		.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=stev1
ldr r1, [r0,#4]
ldr r2, [r0,#8]

cmp r1,r2
bcs prvi

str r2,[r0]
b _end

prvi:
str r1,[r0]

_end:
		B _end


		.data
stev1:	.space 4
stev2:	.word	0xf0000002
stev3:	.word	0xf0000000
```

2. Imamo 32-bitno spremenljivko a. Glede na vrednost spremenljivke nastavite register R1 na naslednji način:
	- r1 = -1, če je a < 0
	- r1 = 0, če je a = 0
	- r1 = 1, če je a > 0
	Preizkusite za vrednosti a = 10, a = -18, a = 0 in a = 0xFFFFF3EC.

```spoiler-markdown
		.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=a
ldr r0,[r0]

cmp r0,#0
beq enako
bgt vecje

mov r1, #-1
b _end

enako:
mov r1,#0
b _end

vecje:
mov r1,#1
b _end

_end:
		B _end


		.data
a:	.word	0
```

3. Napišite program, ki preveri, ali je med odštevanjem dveh 32-bitnih spremenljivk a in b prišlo do prekoračitve (overflow). Če pride do overflowa, nastavite register R3 = 1, sicer R3 = 0.
	Poskusite za vrednosti:
	a = 0x7FFFFFFF, b = -1
	a=100, b=50

```spoiler-markdown
		.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=a
ldr r1,[r0]
ldr r2,[r0,#4]

cmp r1,r2
bvs overflow

mov r3,#0
b _end

overflow:
mov r3,#1

_end:
		B _end


		.data
a:	.word	0x7fffffff
b:	.word	-1
```

4. Zapišite ukaz(e) v zbirniku za procesor ARM, ki v register:
	- Nepredznačeno naloži 16-bitno vrednost 0xF123 v register R4.
	- Predznačeno naloži 16-bitno vrednost 0xF123 v register R5.
	Naložite 16-bitno spremenljivko iz pomnilnika kot dve 8-bitni spremenljivki

```spoiler-markdown
		.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=a
ldrb r4,[r0]
ldrb r5,[r0,#1]

lsl r5,r5,#24
asr r5,r5,#24

_end:
		B _end


		.data
a:	.hword	0xf123
```

5. Iz tabele 8-bitnih števil izračunaj število sodih vrednosti Dana je tabela 8-bitnih števil 2,7,12, 0xFF. Sestavi program, ki:
	- Prebere vsak element.
	- S pomočjo LSR #1 preveri, ali je originalno število sodo (LSB == 0).
	- Če je sodo, poveča števec.
	- Rezultat shrani v registru R0.

```spoiler-markdown
		.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=tabela
mov r1,#0
mov r2,#0

loop:
ldrb r3,[r0,r1]

mov r4,r3

lsr r3,r3,#1
lsl r3,r3,#1


cmp r3,r4
bne naprej

add r2,r2,#1

naprej:
cmp r1,#4
beq _end

add r1,r1,#1
b loop

_end:
		B _end


		.data
tabela: .byte 2,7,12,0xff
```

6. Dana je vhodna tabela A 32-bitnih predznačenih celih števil 32, -7, 0x55, 3, -2 in izhodna tabela B enake dolžine. Napiši ARMv7 program, ki iz vhodne tabele izračuna absolutne vrednosti in jih shrani v izhodno tabelo.
	- Preberi element iz vhodne tabele.
	- Uporabi ASR #31 za ekstrakcijo predznaka (ostane maska −1 ali 0).
	- Če je negativen, pretvori v pozitivnega (izračunaj eniški complement z uporabo XOR, potem seštej 1 za dvojiški komplement).
	- Rezultat shrani v izhodno tabelo.

```spoiler-markdown
.global _start

		.text
		.org 0x00000000
_start:

ldr r0,=a
ldr r8,=b
mov r1,#0

loop:
cmp r1,#16
beq _end

ldr r2,[r0,r1]
mov r3,r2
asr r3,r3,#31
cmp r3,#0
beq nadaljuj

eor r2,r2,r3
add r2,r2,#1

nadaljuj:
str r2,[r8,r1]

add r1,#4
b loop

_end:
		B _end


		.data
a:	.word -7,0x55,3,-2
b:	.space 16
	
	
```

---

1. V zbirniku napišite program za procesor ARM, ki izračuna vsoto 8-bitnih števil. Rezultat shranite v 32- bitno spremenljivko VSOTA. 
	Rešitev preverite s števili v dveh tabelah:
	-  TABELA1 = [20, -18, 19, -105]
	-  TABELA2 = [20, 90, -1, 50, 97]

```spoiler-markdown
        .global _start

        .text
        .org 0x00000000
_start:

ldr r0,=tabela1
mov r1,#0
mov r3,#0

loop:
ldrb r2,[r0,r3]

add r1,r1,r2


add r3,r3,#1
ldrb r4,[r0,r3]
cmp r4,#0
bne loop

lsl r5,r1,#24
asr r5,r5,#24

strb r1,[r0,r3]

_end:
        B _end


        .data
tabela1:  	.byte  20, 90, -1, 50, 97
vsota: 		.word
```

2. Podana je tabela 32-bitnih predznačenih števil (TABELA: .word 24, -3, 56, -201, 469).
	- Definirajte podprogram, ki vrne minimalno vrednost MIN (a,b). Vaš podprogram naj posnema naslednjo Python funkcijo:
		def abmin (a:int, b:int):
			return MIN(a, b)
	- Z uporabo podprograma zapišite program v zbirniku za procesor ARM tako, da poišče minimalno vrednost v tabeli in jo zapiše na konec tabele v spremenljivko STMIN.

```spoiler-markdown

```