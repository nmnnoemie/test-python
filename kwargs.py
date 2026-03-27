def afficher_produit(nom, **details):
 print(f"Produit : {nom}")
 for cle, valeur in details.items():
  print(f"{cle} {valeur}")
afficher_produit("Laptop", prix=999, marque="Dell", stock=5)