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

# 1ère méthode
# a = 5
# b = 7
# print(a,"et",b)
# a,b = b,a
# print(a,"et",b)

# 2ème méthode
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

# a = input("veuillez entrer un mot ")
# for i in range(3):
#     print(a)

# 35. Demande à l’utilisateur un texte et affiche "Ce texte contient ... 
# # voyelles et ... consonnes". 


# a = input("veuillez entrer un texte ")
# voyelle = int(0)
# consonne = int(0)
# for i in range(len(a)):
#     if(a[i]=="i" or a[i]=="u" or a[i]=="o" or a[i]=="a" or a[i]=="e" or a[i]=="y"):
#         voyelle = voyelle + 1
#     else:
#         consonne = consonne + 1
# print("Ce texte contient",voyelle,"voyelles et",consonne,"consonnes")


# 36. Écris un programme qui prend une durée en secondes et la convertit en 
# heures, minutes et secondes. 

# duree = int(input("Veuillez entrer une durée en secondes"))
# reste = int(0)
# heure = int(0)
# minute = int(0)
# seconde = int(0)
# if(duree == 3600):
#     print(duree,"secondes= 1h")
#     # je peux tout aussi enlevé le if(duree == 3600) et commencé à la 2eme 
#     # condition en mettant supperieur ou égal au lieu de suppérieur seulement
#     # ou aussi le faire faire en partant des seconde puis des minutes et enfin les heures
# elif (duree > 3600 ):
#     heure = duree//3600
#     reste = duree%3600
#     if(reste > 60):
#         minute = reste//60
#         seconde = reste%60
#     print(heure,"h",minute,"min",seconde,"s")
# elif(duree >= 60):
#     minute = duree//60
#     seconde = duree%60
#     print(minute,"min",seconde,"s")

   




# 37. Demande à l’utilisateur son salaire mensuel et affiche son salaire annuel. 

# a = int(input("veuillez entrer votre salaire mensuel "))
# print("Si votre salaire mesuel est de",a,"alors le salaire annuel sera",a*12)



# 38. Demande à l’utilisateur deux nombres et affiche "Le premier est plus 
# grand", "Le deuxième est plus grand" ou "Ils sont égaux". 


# a = int(input("veuillez entrer deux nombres "))
# b = int(input("veuillez entrer deux nombres "))
# if(a==b):
#     print(a,"est égal à",b)
# elif(a>b):
#     print(a,"est suppérieur à",b)
# else:
#     print(a,"est inférieur à",b)



# 39. Demande un nombre et affiche "Ce nombre est un multiple de 5" si c’est 
# vrai.

# a = int(input("veuillez entrer un nombre  "))
# if(a%5==0):
#     print(a," est un multiple de 5")
# else:
#     print(a,"n'est pas un multiple de 5")


# 40. Demande à l’utilisateur un mot et affiche "Ce mot commence par une 
# voyelle" si c’est vrai.

# a= input("veuillez entrer un texte ")
# if(a[0]=="i" or a[0]=="I" or a[0]=="u" or a[0]=="U" or a[0]=="o" or a[0]=="O" or a[0]=="a" or a[0]=="A" or a[0]=="e" or a[0]=="E" or a[0]=="y" or a[0]=="Y"):
#     print(a,"commmence par une voyelle")
# else:
#         print(a,"ne commmence pas par une voyelle")




# 41. Demande à l’utilisateur un nombre et affiche "Ce nombre est un carré 
# parfait" si c'est vrai.

# nbr = int(input("Veuillez saisir un nombre : "))
# for i in range((nbr//2)+1):
#     if(i**2==nbr):
#         print(nbr,"est un carré parfait car",nbr,"=",i,"²")
#         break



# 42. Demande à l'utilisateur un mot et vérifie s'il commence et finit par la même 
# lettre. 

# a= input("veuillez entrer un mot ")
# if(a[0]==a[-1]):
#     print("c'est vrai",a,"commence par",a[0],"et se termine par",a[0])
# else:
#     print("C'est faux",a,"commence par",a[0],"mais se termine par",a[-1])


# 43. Demande à l’utilisateur un texte et affiche le nombre de mots qu’il contient. 

# celui-ci est un peu incomplet
# a = input("veuillez entrer un texte ")
# cpt = int(1)
# for i in range(len(a)):
#     if(a[i]==" "):
#         cpt = cpt + 1
# print("Ce texte contient",cpt,"mots")


# 44.Écris un programme qui demande la distance et la vitesse, puis calcule le 
# temps de trajet.

# dist = float(input("veuillez entrer la distance (en mètre) "))
# vit = float(input("veuillez entrer la vitesse (en mètre par seconde) "))
# print("Le temps du trajet sera :",dist/vit,"s")


# 45.Demande à l’utilisateur un nombre entier et affiche la somme des chiffres qui 
# le composent.

# somme = int(0)
# nombre = (input("veuillez entrer un nombre "))
# for i in range(len(nombre)):
#     somme = somme+ int(nombre[i])
#     print(nombre[i])
# print("la SOMME DES CHIFFRES QUI LE COMPOSE EST ",somme)


# 46. Demande trois nombres et affiche le plus grand.


# a = float(input("veuillez entrer trois nombres"))
# b = float(input())
# c = float(input())

# if(a>b and a>c):
#     print(a,"est le plus grand nombre")
# elif(b>a and b>c):
#     print(b,"est le plus grand nombre")
# elif(c>a and c>b):
#     print(c,"est le plus grand nombre")
# else:
#     print("y'en a qui sont égaux")

# 47. Demande à l’utilisateur un nombre et affiche "Ce nombre est premier" s’il 
# l’est. 

# nbr = int(input("Veuillez saisir un nombre : "))
# cpt = int(0)
# for i in range(nbr):
#     if(nbr%(i+1)==0):
#         cpt = cpt +1
# print(cpt)
# if(cpt==2):
#     print("Ce nombre est premier")
# else:
#     print(nbr,"n'est pas premier")


# 48.Écris un programme qui demande à l’utilisateur deux nombres et échange 
# leurs valeurs. 

# nbr1 = int(input("Veuillez saisir deux nombres : "))
# nbr2 = int(input())
# print("nombre 1 =",nbr1,"et nombre 2 =",nbr2)
# ech = nbr1
# nbr1 =nbr2
# nbr2 = ech
# print("nombre 1 est devenu",nbr1,"et nombre 2 est devenu",nbr2)



# 49. Demande une phrase et affiche "Ce texte est un palindrome" si c’est vrai. 

# mot = input("Veuillez saisir un mot : ")
# demi = len(mot)//2
# verife = False
# for i in range(demi):
#     if(mot[i]==mot[-(i+1)]):
#         verife= True
#     else:
#         verife=False
#     print(mot[i]," et ",mot[-(i+1)])

# if(verife==False):
#     print(mot,"n'est pas un palindrome")
# else:
#     print(mot,"est un palindrome")



# 50. Demande à l’utilisateur un texte et affiche "Ce texte est en majuscules", 
# "Ce texte est en minuscules", ou "Ce texte est mixte". 

# texte = input("Entrez votre texte : ")

# if(texte.lower() == texte):
#     print("Ce texte est en minuscule")
# elif(texte.upper()==texte):
#     print("Ce texte est en majuscule")
# else:
#     print("Ce texte est mixte")



# les exos sur du cours
# 
# Exercice 1  
# Un magasin de reprographie facture 2 F les dix premières photocopies, 1.50 F les vingt suivantes et 
# # 1 F au-delà. Ecrivez un programme qui demande à l’utilisateur le nombre de photocopies 
# # effectuées puis affiche le montant correspondant. 

# nbr = int(input("Entrer le nombre de photocopies "))
# reste= int(0)
# prix = float(0)
# if(nbr>10):
#     reste = nbr-10
#     prix += 2*10
#     if(reste>20):
#         nbr = reste-20
#         prix += 1.5*20 + nbr 
#     else:
#          prix += 1.5*reste
#     print("le montant est de la facture est de",prix)

# else:
#     print("le montant est de la facture est de",2*nbr)





# Exercice 2 
# Ecrire un programme permettant d’afficher le nom du jour en introduisant le numéro du jour.  
# En utilisant une alternative. 
# # En utilisant l’instruction match.

# choix = int(input("Entrer le numéro du jour de la semaine"))

# match choix:
#     case 1:
#         print("Lundi")
#     case 2:
#         print("Mardi")
#     case 3:
#         print("Mercredi")
#     case 4:
#         print("Jeudi")
#     case 5:
#         print("Vendredi")
#     case 6:
#         print("Samedi")
#     case 7:
#         print("Dimanche")

    # ou utiliser les conditions