def max_palindrom():
    max = 0
    for i in range(100,1000):
        seznam = [int(d) for d in str(i)]
        for j in range(len(seznam)):
            if seznam[j] != seznam[-1-j]:
                break