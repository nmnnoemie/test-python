montant= float(input("Entrer votre montant :"))
pourcentage_de_pourboire=float(input("Entrer votre pourcentage de pourboire :"))
pourcentage_de_pourboire=montant*(pourcentage_de_pourboire/100)
total =montant+pourcentage_de_pourboire
print ("Votre addition est de :",total)
