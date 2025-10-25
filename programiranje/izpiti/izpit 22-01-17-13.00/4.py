def skladiscniki(marsovec,hierarhija):
    if(not hierarhija[marsovec]):
        return 1
    podHierarhija = hierarhija[marsovec]
    st = 0
    for el in podHierarhija:
        st += skladiscniki(el,hierarhija)
    return st

hierarhija = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Matjaž": ["Viljem"],
    "Viljem": ["Tadeja"],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Ludvik": [],
    "Franc": [],
    "Jurij": ["Jožef"],
    "Jožef": ["Petra", "Aleksander", "Alenka"],
    "Barbara": [],
    "Hans": ["Herman", "Erik"],
    "Herman": ["Margareta"],
    "Erik": [],
    "Margareta": [],
    "Aleksander": [],
    "Petra": [],
    "Alenka": [],
    "Tadeja": []
}

print(skladiscniki("Adam",hierarhija))