mdp=input("Entrer votre mot de passe:")
ndt=0
while mdp!="secret123":
     print ("mot de passe incorrect!",ndt+1)
     mdp=input("nouvelle tentative:")
     print ("tentative",ndt+1)
     for i in range(0,ndt):
        print("tentative",ndt+1)
        if mdp=="secret123":
            print("mot de passe correct!")
    
