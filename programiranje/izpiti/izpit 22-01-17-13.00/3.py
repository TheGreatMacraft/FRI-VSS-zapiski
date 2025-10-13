def marsovci():
    ime_datoteke = input("Vnesi ime datoteke: ") + ".txt"
    text = open(ime_datoteke, encoding="utf-8")
    slovar = {}
    for line in text:
        if line.split(":")[1].split(" ")[1] != "paradižnik":
            continue
        kraj = line.split(":")[0]
        if kraj in slovar:
            slovar[kraj] + int(line.split(" ")[len(line.split(" ")) - 1])
        else:
            slovar[kraj] = int(line.split(" ")[len(line.split(" ")) - 1])

    return slovar

print(marsovci())