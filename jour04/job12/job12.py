def tri_croissant_liste(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

L = [7, 11, 42, 39, 2]

tri_croissant_liste(L)

print(L)