mot=str(input("Entrer un mot:"))
vowel=("aeiouy")
tion=("tion")
mca=str(mot.startswith(vowel))
mftion=str(mot.endswith(tion))
mv=mot.count(vowel)
mtion=mot.count(tion)
if str(mot.__contains__(tion)):
    print("présent")
elif str(mot.__contains__(vowel)):
    print("présent")
else :
    print("absent")