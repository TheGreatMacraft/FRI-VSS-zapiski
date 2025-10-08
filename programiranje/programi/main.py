def paketov(teze,nosilnost):

    st_ladji = 0
    index = 0

    for ta_nosilnost in nosilnost:
        if index >= len(teze):
            break
        if ta_nosilnost < teze[index]:
            continue
        while index < len(teze) and ta_nosilnost - teze[index] >= 0:
            ta_nosilnost -= teze[index]
            index += 1
        st_ladji += 1

    return st_ladji

teze = [5,10,2,6,7,3,41,15,18,24,2,7,34]
nosilnost = [50,25,75,100,50,24]

print(paketov(teze,nosilnost))

