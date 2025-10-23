ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]
x = 6
min = None

for el in ovire:
    if el[2] == y and (min == None or el[1] < min):
        min = el[1]

print(f"Prva ovira, na katero bo kolesar naletel, v vrstici {x}, je ovira({x},{min})")
