def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if longueur_du_mot(mot) > longueur_minimale]
    return ' '.join(mots_filtres)

def longueur_du_mot(mot):
    count = 0
    for _ in mot:
        count += 1
    return count

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

print("Output :", resultat)