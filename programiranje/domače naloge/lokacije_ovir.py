zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

def ovire(zemljevid):
    rezultat = []
    for i in range(len(zemljevid)):
        j = 0
        while j < len(zemljevid[i]):
            if zemljevid[i][j] == '#':
                ovire = [j+1]
                for k in range(j, len(zemljevid[i])):
                    if zemljevid[i][k] == '.':
                        ovire.extend([k, i+1])
                        rezultat.append(ovire)
                        j = k
                        break
                else:
                    ovire.extend([len(zemljevid[i]), i+1])
                    rezultat.append(ovire)
                    j = len(zemljevid[i])
            j += 1
    return rezultat

print(ovire(zemljevid))
