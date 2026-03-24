capital=float (input("entrer le capital emprunté:"))
tauxannuel=float(input("entrer votre taux annuel:"))
duréenenmois =float(input("entrée votre durée en mois:"))
interets= (capital*tauxannuel)/100/12*duréenenmois
print("le montant de l'emprunt est de:",interets)