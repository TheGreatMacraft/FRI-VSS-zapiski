def rekurzija(a):
    if(a == 0):
        return
    print(a)
    return rekurzija(a-1)

rekurzija(100)