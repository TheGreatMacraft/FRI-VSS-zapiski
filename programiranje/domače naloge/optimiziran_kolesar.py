import numpy as np
ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

vredu = np.arange(1,11,1)
finx = 0
finy = 0

for n in vredu:
    tmp = 10
    for el in ovire:
        if n in el[:-1] and tmp > el[-1]:
            tmp = el[-1]
    if tmp > finy and tmp != 10:
        finy = tmp
        finx = n

print(finx, finy)