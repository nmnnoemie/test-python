premiercoté=float(input("Entrer le premier coté:"))
deuxièmecoté=float(input("Entrer le deuxième coté:"))
troisièmecoté=float(input("Entrer le troisième coté:"))
if premiercoté>deuxièmecoté+troisièmecoté:
    print("triangle invalide")
elif deuxièmecoté>premiercoté+troisièmecoté:
    print("triangle invalide")
elif troisièmecoté>premiercoté+deuxièmecoté:
    print ("trianngle invalide")
else:
    print("triangle valide")
