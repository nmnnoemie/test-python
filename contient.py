texte=str(input("Entrer un texte:"))
mot=str(input("Entrer un mot à chercher:"))
mf=texte.find(mot)
mc=texte.count(mot)
ti=texte.index(mot)
abs="pas trouvé"
if texte.__contains__(mot):
    print("présent",mc,ti)
else:
    print(abs)

