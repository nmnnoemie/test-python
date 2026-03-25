n=int(input("Entrer un nombre:"))
if n>0:
    print("Nombre valide")
else:
    print(f"Démarrage de{n} a 10:")
for i in range (0,11):
    print (n*i)