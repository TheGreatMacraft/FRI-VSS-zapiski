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