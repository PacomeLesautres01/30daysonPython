# Jour 4: 30 Days of Python Programming

#Exercices - Jour 4


# 1- Concaténer "trente", "jours", "de", "python"
chaine1 = ' '.join(['trente', 'jours', 'de', 'python'])
print(chaine1)  

# 2- Concaténer "codage", "pour", "all"
chaine2 = ' '.join(['codage', 'pour', 'all'])
print(chaine2)  

# 3- Déclarer la variable société
societe = "codage pour tous"
print(societe)                  # 4- Imprimer la variable société
print(len(societe))             # 5- Longueur de la variable société
print(societe.upper())          # 6- Tout en majuscules
print(societe.lower())          # 7- Tout en minuscules
print(societe.capitalize())     # Première lettre en majuscule
print(societe.title())          # Chaque mot en majuscule
print(societe.swapcase())       # Inverse maj/min

# 9. Couper le premier mot ("Coding For All")
chaine3 = "Coding For All"
print(chaine3[7:])  # "For All"

# 10. Vérifier si "Coding" est présent
print("Coding" in chaine3)  # True
print(chaine3.find("Coding"))  # 0

# 11- Remplacer "codage" par "Python"
print(societe.replace("codage", "Python"))

# 12- Remplacer "Python pour tout le monde" par "Python pour tous"
phrase = "Python pour tout le monde"
print(phrase.replace("tout le monde", "tous"))

# 13- Diviser "Coding For All"
print(chaine3.split())  

# 14. Diviser "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
chaine4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(chaine4.split(", "))

# 15- Caractère à l'index 0
print(chaine3[0])  

# 16- Dernier index
print(len(chaine3) - 1) 

# 17- Caractère à l’index 10 de "codage pour toutes"
chaine5 = "codage pour toutes"
print(chaine5[10])

# 18. Acronyme "Python pour tout le monde"
phrase2 = "Python pour tout le monde"
acronyme1 = ''.join([mot[0].upper() for mot in phrase2.split()])
print(acronyme1)  # PPTM

# 19. Acronyme "codage pour tous"
phrase3 = "codage pour tous"
acronyme2 = ''.join([mot[0].upper() for mot in phrase3.split()])
print(acronyme2)  # CPT

# 20. Première occurrence de "C"
print(chaine3.index("C"))

# 21. Première occurrence de "F"
print(chaine3.index("F"))

# 22. Dernière occurrence de "l" (dans "Coding For All People")
chaine6 = "Coding For All People"
print(chaine6.rfind("l"))

# 23- Première occurrence de "parce que"
texte = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print(texte.find("parce que"))

# 24- Dernière occurrence de "parce que"
print(texte.rindex("parce que"))

# 25. Trancher "parce que parce que parce que"
start = texte.find("parce que")
end = texte.rfind("parce que") + len("parce que")
print(texte[start:end])  # extrait

# 26. Première occurrence (même que 23)
print(texte.find("parce que"))

# 27. Trancher (même que 25)
print(texte[start:end])

# 28. Commence par "Coding" ?
print(chaine3.startswith("Coding"))

# 29. Se termine par "coding" ?
print(chaine3.endswith("coding"))

# 30. Retirer espaces autour
chaine7 = "  Codage pour tous  "
print(chaine7.strip())

# 31. isidentifier()
print("30daysofpython".isidentifier())        # False
print("Thirty_days_of_python".isidentifier()) # True

# 32. Joindre une liste avec "# "
libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(libs))

# 33. Nouvelle ligne
print("J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")

# 34. Tabulation
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. Aire d’un cercle
radius = 10
area = 3.14 * radius ** 2
print(f"La zone d'un cercle avec le rayon {radius} est de {int(area)} mètres carrés.")

# 36. Opérations mathématiques
a, b = 8, 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
