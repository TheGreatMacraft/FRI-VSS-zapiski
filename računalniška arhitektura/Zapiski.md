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
1. "*Računalnik naj deluje izključno na osnovi vsebine ukazov*. => *Naj ne spreminja svojega ožičenja.*" (CPE)
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

![[Drawing 2025-10-07 13.01.58.excalidraw|1000x400]]

# Pomnilnik
- pomnilnik je sestavljen iz zaporedja *pomnilniških besed (memory word)*
- **pomnilniška beseda** je najmanjša količina informacije, ki se prenaša med pomnilnikom in CPE
![[Drawing 2025-10-07 13.36.44.excalidraw]]
- v digitalni elektroniki, s katero implementiramo rač. sisteme se najmanjši količini informacije reče *bit*. Hrani se jo v obliki 0/1 (visoka ali nizka napetost => 3.3V ali 0V)
- Vsaka pomnilniška beseda ima svoj enoličen **naslov**, ki je informacija o poziciji besede v pomnilniku
- Tipična širina podatkovne besede je **8 bitov**, oziroma 1 bajt. 