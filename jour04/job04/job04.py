def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "mangue")
    return fruits

liste_de_fruits_avec_mangue = ajouter_mangue()

print(liste_de_fruits_avec_mangue)