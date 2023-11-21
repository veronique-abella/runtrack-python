nom_produit = "téléphone portable"
prix_unitaire = 1000
quantite_stock = 100
nombre_achat_client = int(input("Entrer la quantité souhaitée : "))
quantite_stock_restant = (quantite_stock - nombre_achat_client)
inflation = 10
prix_unitaire_inflation = (prix_unitaire * inflation) / 100 + prix_unitaire

print(f"Nom du produit :{nom_produit}")
print(f"Prix unitaire :{prix_unitaire}")
print(f"Quantité du stock :{quantite_stock}")
print(f"Quantité du stock restant :{quantite_stock_restant}")
print(f"Prix unitaire après inflation :{prix_unitaire_inflation}")

