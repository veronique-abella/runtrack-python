def echanger_premier_et_dernier(liste):
    if len(liste) >= 1:
        print(liste)

        liste[0], liste[-1] = liste[-1], liste[0]

        print(liste)
    else:
        print()

ma_liste = [1, 2, 3, 4, 5]  
echanger_premier_et_dernier(ma_liste)