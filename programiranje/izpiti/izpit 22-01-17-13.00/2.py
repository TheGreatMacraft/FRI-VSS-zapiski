def razporedi(teze, standardna_nosilnost):
    odgovor = []

    while len(teze) > 0:
        nosilnost = standardna_nosilnost
        teze_na_ladji = []

        for i in teze[:]:
            if nosilnost - i > 0:
                nosilnost -= i
                teze_na_ladji.append(i)
                teze.remove(i)

        odgovor.append(teze_na_ladji)

    return odgovor

print(razporedi([5, 3, 8, 1, 2, 3, 5, 4, 2, 4], 9))