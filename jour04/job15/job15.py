def tri_a_bulles(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

def arrondir_liste(liste):
    liste_arrondie = []
    for nombre in liste:
        nombre_arrondi = int(nombre + 0.5)
        liste_arrondie.append(nombre_arrondi)
    return liste_arrondie

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

L_arrondie = arrondir_liste(L)

tri_a_bulles(L_arrondie)

print(L_arrondie)