def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")
    else:
        print("Entrez un nombre entier et positif.")

resultat_1 = verifier_pair_impair(7)
print(resultat_1)

resultat_2 = verifier_pair_impair(12)
print(resultat_2)

resultat_3 = verifier_pair_impair(0)
print(resultat_3)

resultat_4 = verifier_pair_impair(3.5)
print(resultat_4)

resultat_5 = verifier_pair_impair(-8)
print(resultat_5)
