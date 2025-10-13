def paketov(teze, nosilnost):
    tmp = nosilnost
    st_paketov = 0
    for paket in teze:
        if tmp - paket >= 0:
            tmp -= paket
            st_paketov += 1
        else:
            break
    return st_paketov

print(paketov([5, 3, 8, 1, 2, 3, 5, 4, 2, 4], 9))