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

a = int(input("veuillez entrer deux nombres  "))
b = int(input())
print(" a = ",a," et b = ",b)
# pour celui-ci j'ai un peu gambergé
a = a+b
b = a-b
a = a-b
print("Maintenant a = ",a," et b = ",b)