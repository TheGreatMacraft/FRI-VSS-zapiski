def razporedi(teze, standardna_nosilnost):
    odgovor = []

    while len(teze) > 0:
        nosilnost = standardna_nosilnost
        teze_na_ladji = []

        for t in teze[:]:
            if nosilnost - t >= 0:
                nosilnost -= t
                teze_na_ladji.append(t)
                teze.remove(t)

        odgovor.append(teze_na_ladji)

    return odgovor

print(razporedi([5, 3, 8, 1, 2, 3, 5, 4, 2, 4], 9))