solde=float(input("Entrer votre solde:"))
montant = float(input("Entrer le montant à retirer:"))
if montant>solde:
    print("Solde insuffisant")
else:
    print("Retrait effectué")