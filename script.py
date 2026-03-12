mot_de_passe = "python"
Entre = None
essais = 3
changé = None
while essais > 0:

       Entre = input("Entre le mot de passe : ")

       if Entre ==mot_de_passe:
            print("Accès autorisé")
            changé = input("Veux-tu changer le mot de passe ? oui/non : ")
       if changé == "oui":
            mot_de_passe = input("Nouveau mot de passe : ")
            print("Mot de passe changé !")
            print("Accès autorisé")
            break 
       if changé == "non": 
          print("Accès autorisé")
          break    
       elif essais ==0:
            print("Accès bloqué")
       else :
            essais = essais - 1
            print("code incorrect")
            print("il reste", essais ,"essai")
print("fin du programme")
