def remplacer_element(liste):
    if len(liste) >= 5:
        print(liste[1])

        if len(liste) >= 5:
            liste[3] = liste[2] + liste[4]
            print(liste)

        print(liste[-1])
    else:
        print()

L = [1, 2, 3, 4, 5]  

print(L)

remplacer_element(L)