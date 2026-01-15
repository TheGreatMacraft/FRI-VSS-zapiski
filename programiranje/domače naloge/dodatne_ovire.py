def odstrani_odvecne(obstojece, nove):
    obstojece [:] = [ob for ob in obstojece if not any(max(ob[0],nv[0]) <= min(ob[1],nv[1]) for nv in nove)]

def zlite_ovire(obstojece, dodatne):
    tmp = list(obstojece)
    odstrani_odvecne(tmp, dodatne)
    vse = tmp + dodatne
    vse.sort()

    rez = []
    current_start, current_end = vse[0]

    for start, end in vse[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            rez.append((current_start, current_end))
            current_start, current_end = start, end

    rez.append((current_start, current_end))
    return rez

obstojece = [(3, 5), (9, 10), (13, 15), (19, 24), (26, 27), (33, 35), (37, 38), (45, 47), (49, 50), (53, 55),
                 (60, 60), (62, 62), (64, 66), (69, 69), (71, 71), (73, 73), (76, 77)]

nove = [(7, 9), (15, 16), (20, 20), (24, 25), (30, 33), (36, 36), (41, 42), (48, 48), (59, 65), (69, 72), (79, 81)]

print(zlite_ovire(obstojece,nove))