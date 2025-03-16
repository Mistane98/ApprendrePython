# Déclare une variable nom contenant ton prénom et affiche-la avec print().

# nom = "Ton prénom"
# print(nom)
# print(nom)


# Crée une variable age, attribue-lui un nombre et affiche "J'ai X ans" en 
# remplaçant X par la valeur de age.

# age = 67
# print("j'ai",age,"ans")


# Déclare une variable ville contenant le nom de ta ville et affiche "J'habite 
# à ...".

# ville = "Conakry"
# print("J'habite",ville)


#  Déclare deux variables a = 5 et b = 3, puis affiche leur somme. 

# a = 5
# b = 3
# somme = a + b
# print("La somme de a et b est ",somme)


# Déclare trois variables x = 10, y = 2.5, et z = "Python", puis affiche-les 
# toutes sur une seule ligne. 

# x = 10
# y = 2.5
# z = "python"
# print(x,y,z, sep="  ")


# Écris un programme qui demande le prénom de l'utilisateur et l'affiche avec 
# "Bonjour ...". 

# prenom = input("Quel est votre prénom ?")
# print("Bonjour ", prenom)


# Demande à l'utilisateur son âge et affiche "Tu as ... ans". 

# age = int(input("Quel est votre âge ?  "))
# print("Tu as ", age," ans")


#  Écris un programme qui demande deux nombres et affiche leur addition.

# a = int(input("veuillez entrer deux nombres  "))
# b = int(input())
# print("la somme de ",a," et ",b," est ", a+b)


# Demande à l'utilisateur son nom et son âge, puis affiche "Tu t’appelles 
# ... et tu as ... ans".

# prenom = input("Quel est votre prénom ?")
# age = int(input("Quel est votre âge ?  "))
# print("Tu t’appelles ",prenom," et tu as ",age," ans")


# Crée trois variables de différents types (int, float, str), puis affiche leur 
# type avec type(). 

# x = 10
# y = 2.5
# z = "python"
# print(x," est de type",type(x))
# print(y," est de type",type(y))
# print(z," est de type",type(z))


#  Demande à l'utilisateur de saisir un nombre et affiche son double. 

# nombre = int(input("veuillez entrer un nombre  "))
# print("le double de ",nombre," est ", nombre * 2)


# Demande à l'utilisateur un nombre, convertis-le en entier et affiche son carré. 

# nombre = int(input("veuillez entrer un nombre  "))
# print("le carré de ",nombre," est ", nombre * nombre)



#  Crée une variable contenant une phrase et affiche son premier caractère. 

# a = input("veuillez entrer une phrase  ")
# print("Le premier caractère de cette phrase est ",a[0])



#  Demande à l'utilisateur deux nombres, effectue la multiplication et affiche le 
# résultat. 

# a = int(input("veuillez entrer deux nombres  "))
# b = int(input())
# print("le produit de ",a," et ",b," est ", a*b)


# Demande à l'utilisateur une température en Celsius et convertis-la en 
# Fahrenheit (F = C * 9/5 + 32). 

# F = 0
# C = float(input("veuillez entrer la température en dégré celsius  "))
# F = C * 9/5 + 32
# print(C,"°C est égale à ",F,"°F")

#  Écris un programme qui demande le prix d'un article et la TVA (en %), puis 
# affiche le prix TTC. 

# prix = float(input("veuillez entrer le prix   "))
# tva = float(input("veuillez entrer la TVA EN POURCENTAGE   "))
# print("le prix hors taxe est ",prix + (prix*tva/100) )


# Demande à l'utilisateur un nombre et affiche "Pair" s'il est pair, sinon 
# "Impair". 

# a = int(input("veuillez entrer un nombre  "))
# if(a%2==0):
#     print(a," est un nombre pair")
# else:
#     print(a," est un nombre impair")


# Demande à l'utilisateur un mot et affiche "Ce mot contient X lettres" (en 
# remplaçant X par la longueur du mot).

# a = input("veuillez entrer un MOT  ")
# print(a," Ce mot contient ",len(a)," lettres ")


#  Demande le prénom et l’âge de l’utilisateur et affiche "Dans 10 ans, tu 
# auras X ans". 

# prenom = input("Quel est votre prénom ?  ")
# age = int(input("Quel est votre âge ?  "))
# print("Dans 10 ans ",prenom," aura ",age + 10," ans")


# Écris un programme qui échange les valeurs de deux variables a et b sans 
# créer de troisième variable. 

# a = int(input("veuillez entrer deux nombres  "))
# b = int(input())
# print(" a = ",a," et b = ",b)
# # pour celui-ci j'ai un peu gambergé
# a = a+b
# b = a-b
# a = a-b
# print("Maintenant a = ",a," et b = ",b)


# Demande à l'utilisateur son prénom et affiche-le en majuscules et en 
# minuscules.

# prenom = input("Quel est votre prénom ?  ")
# print("Prénom en majiscule ",prenom.upper())
# print("Prénom en miniscule ",prenom.lower())


# Demande à l'utilisateur deux nombres et affiche leur quotient en division 
# entière et leur reste.

# a = int(input("veuillez entrer deux nombres  "))
# b = int(input())
# print("le quotien de ",a," et ",b," est ",a//b," leur reste est ", a%b)


#  Demande trois nombres à l'utilisateur et affiche leur moyenne. 


# a = int(input("veuillez entrer deux nombres  "))
# b = int(input())
# c = int(input())
# moy = (a+b+c)/3
# print("la moyenne de ",a ,b," et ",c," est ",moy)


#  Écris un programme qui convertit une longueur en mètres vers des 
# kilomètres. 

# lon = int(input("veuillez entrer une longueur en mètres  "))
# print(lon," mètres =",lon/1000,"kilomètres")


# Demande une phrase à l’utilisateur et affiche-la 5 fois sur des lignes 
# différentes. 

# a = input("veuillez entrer une phrase  ")
# for x in range(5):
#     print(a)
# ou
# print(a)
# print(a)
# print(a)
# print(a)
# print(a)



#  Écris un programme qui demande une année et affiche si elle est bissextile 
# (année % 4 == 0). 

# annee = int(input("veuillez entrer une année  "))
# if(annee % 4 == 0):
    # print(annee,"est une année bissextile")



# Demande le prix d'un produit et le pourcentage de réduction, puis affiche le 
# prix final. 

# prix = float(input("veuillez entrer le prix   "))
# tva = float(input("veuillez entrer le  POURCENTAGE de la réduction "))
# print("le prix après réduction est ",prix - (prix*tva/100) )


# Demande à l’utilisateur son prénom et affiche "Bonjour ..." en ajoutant 
# une ligne vide avant. 


# prenom = input("veuillez entrer votre prénom  ")
# print("")
# print("Bonjour",prenom)


# Demande à l’utilisateur une phrase et affiche la première et la dernière lettre. 

# a = input("veuillez entrer une phrase  ")
# print("Le premier caractère de cette phrase est ",a[0])
# print("Le dernier caractère de cette phrase est ",a[-1])
# 

#  Demande à l’utilisateur son année de naissance et affiche son âge actuel. 

# annee = int(input("veuillez entrer votre année de naissance "))
# print("actuellement vous devez avoir DANS LES ENVIRONS DE",2025-annee)


# # Écris un programme qui demande la taille et le poids d'une personne et 
# # calcule son IMC (poids / taille²). 
                 

# taille = float(input("veuillez entrer votre taille   "))
# poids = float(input("veuillez entrer  votre poids "))
# print("Votre IMC EST de",poids/taille**2,"kg/m²")



# Demande un nombre à l’utilisateur et affiche "Positif" s'il est positif, 
# "Négatif" sinon. 

# nombre = int(input("veuillez entrer un nombre "))
# if(nombre >= 0):
#     print(nombre,"est un nombre positif")
# else:
#     print(nombre,"est un nombre négatif")


# 33. Écris un programme qui affiche "Python est génial" sans utiliser 
# directement cette phrase.

# a = "python" 
# b = "est"
# c = "génial"
# print(a,b,c)


# 34. Demande à l’utilisateur un mot et affiche-le en le dupliquant 3 fois. 

a = input("veuillez entrer un mot ")
for i in range(3):
    print(a)

# 35. Demande à l’utilisateur un texte et affiche "Ce texte contient ... 
# voyelles et ... consonnes". 
# 36. Écris un programme qui prend une durée en secondes et la convertit en 
# heures, minutes et secondes. 
# 37. Demande à l’utilisateur son salaire mensuel et affiche son salaire annuel. 
# 38. Demande à l’utilisateur deux nombres et affiche "Le premier est plus 
# grand", "Le deuxième est plus grand" ou "Ils sont égaux". 
# 39. Demande un nombre et affiche "Ce nombre est un multiple de 5" si c’est 
# vrai. 
# 40. Demande à l’utilisateur un mot et affiche "Ce mot commence par une 
# voyelle" si c’est vrai.