# Chaque etudiant a ses propres informations
etudiants = {
 "Alice": {"age": 20, "note": 16},
 "Bob": {"age": 22, "note": 11},
}
# Acceder a une donnee imbriquee
# D'abord on prend Alice, puis on prend son age
print(etudiants["Alice"]["age"]) # 20
print(etudiants["Bob"]["note"]) # 11
# Parcourir tous les etudiants
for prenom, infos in etudiants.items():
 print(f"{prenom} : {infos['note']}/20")