ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]
x = 6
blizu_ovira = []

for el in ovire:
    if x in el[:-1] and (not blizu_ovira or el[-1] < blizu_ovira[-1]):
        blizu_ovira = el

print(f"Prva ovira, na katero bo kolesar naletel, v vrstici {x}, je ovira({blizu_ovira})")

