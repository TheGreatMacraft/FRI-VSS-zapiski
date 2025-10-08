1. Nariši resničnostno tabelo izjavnega izraza $(p \implies q) \vee (\neg q \implies p)$.
Pomoč: [[diskretne strukture/Zapiski#Resničnostna tabela|Resničnostna tabela]]

Rešitev:
```spoiler-markdown
![[Drawing 2025-10-08 15.39.24.excalidraw|1500]]
```

2. Preveri ali je izjavni izraz $p \implies (q \implies p)$ tavtologija.
Pomoč: [[diskretne strukture/Zapiski#Resničnostna tabela|Resničnostna tabela]]

Rešitev:
```spoiler-markdown
![[Drawing 2025-10-08 16.41.50.excalidraw|1500]]
```

3. Poišči izjavni izraz s predpisano resničnostno tabelo:

$\begin{array}{c|c} p & q & r & A \\ \hline 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 1 \end{array}$

Pomoč: [[diskretne strukture/Zapiski#Disjunktivna normalna oblika|Disjunktivna normalna oblika]], [[diskretne strukture/Zapiski#Konjunktivna normalna oblika|Konjunktivna normalna oblika]]
```spoiler-markdown
Preverimo, kje je A resničen in v oklepajih zapišemo stanje spremenljivk na teh točkah, ki jih povežemo s konjunkcijo (in). Oklepaje nato med seboj povežemo z disjunkcijo (ali). S tem zapišemo [[diskretne strukture/Zapiski#Disjunktivna normalna oblika|Disjunktivno normalno obliko]].

$A_{DNO} = (\neg p \land \neg q \land r) \vee (\neg p \land q \land r) \vee (p \land \neg q \land \neg r) \vee (p \land \neg q \land r) \vee (p \land q \land r)$

Isto nalogo lahko rešimo s pomočjo [[diskretne strukture/Zapiski#Konjunktivna normalna oblika|Konjunktivne normalne oblike]], tako da preverimo kje A ni resničen in v oklepajih zapišemo stanja spremenljivk na teh točkah, povezana z disjunkcijo (ali), te oklepaje pa nato povežemo s konjunkcijo (in):

$A_{KNO} = (p \vee q \vee r) \land (p \vee \neg q \vee r) \land (\neg p \vee \neg q \vee r)$

```

4. Skrajšaj $(p \vee q \vee r) \land (p \vee \neg q \vee r) \land (\neg p \vee \neg q \vee r)$
Pomoč: [[diskretne strukture/Zapiski#Zakoni izjavnega računa|Zakoni izjavnega računa]]

```spoiler-markdown
![[Drawing 2025-10-08 18.25.33.excalidraw|2500]]
```

5. 