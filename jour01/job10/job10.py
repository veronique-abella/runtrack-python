montant_initial_investissement = 10000
taux_rendement_annuel = 3
gain_annuel = (montant_initial_investissement * taux_rendement_annuel) / 100 
nouveau_montant_apres_un_an = montant_initial_investissement + gain_annuel
nouveau_montant_investissement = nouveau_montant_apres_un_an + 5000
nouveau_taux_rendement = taux_rendement_annuel + 2
nouveau_gain_annuel = (nouveau_montant_investissement * nouveau_taux_rendement) / 100 
nouveau_montant_apres_deux_ans = nouveau_montant_investissement + nouveau_gain_annuel
retrait_investisseur = nouveau_montant_apres_deux_ans * 0.10 

diminution_rendement = nouveau_taux_rendement - 1
nouveau_montant_apres_retrait = nouveau_montant_apres_deux_ans - retrait_investisseur
nouveau_gain_apres_retrait = (nouveau_montant_apres_retrait * diminution_rendement) / 100
nouveau_montant_apres_trois_ans = nouveau_gain_apres_retrait + nouveau_montant_apres_retrait


print(f"Gain annuel en fonction du taux de rendement :{gain_annuel}")
print(f"Gain annuel après deux ans :{nouveau_gain_annuel}")
print(f"Gain après diminution rendement :{retrait_investisseur}")
print(f"Gain annuel après trois ans :{nouveau_gain_apres_retrait}")
print(f"Montant final :{nouveau_montant_apres_trois_ans}")

