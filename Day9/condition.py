# -----------------------------
# JOUR 9 - EXERCICES : CONDITIONNELS
# -----------------------------

# ----------- Niveau 1 -----------

# 1. Âge et conduite
age = int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes assez vieux pour apprendre à conduire.")
else:
    print(f"Vous avez besoin de {18 - age} an{'s' if (18 - age) > 1 else ''} de plus pour apprendre à conduire.")

# 2. Comparaison d'âges
mon_age = 25
votre_age = int(input("Entrez votre âge: "))
if votre_age > mon_age:
    diff = votre_age - mon_age
    print(f"Vous avez {diff} an{'s' if diff > 1 else ''} de plus que moi.")
elif votre_age < mon_age:
    diff = mon_age - votre_age
    print(f"J'ai {diff} an{'s' if diff > 1 else ''} de plus que vous.")
else:
    print("Nous avons le même âge.")

# 3. Comparaison de deux nombres
a = int(input("Entrez le numéro un: "))
b = int(input("Entrez le numéro deux: "))
if a > b:
    print(f"{a} est supérieur à {b}")
elif a < b:
    print(f"{a} est inférieur à {b}")
else:
    print(f"{a} est égal à {b}")

# ----------- Niveau 2 -----------

# 1. Notation selon score
score = int(input("Entrez votre score: "))
if 80 <= score <= 100:
    print("Note : A")
elif 70 <= score <= 79:
    print("Note : B")
elif 60 <= score <= 69:
    print("Note : C")
elif 50 <= score <= 59:
    print("Note : D")
elif 0 <= score <= 49:
    print("Note : F")
else:
    print("Score invalide")

# 2. Détection de la saison
mois = input("Entrez le mois: ").capitalize()
if mois in ["Septembre", "Octobre", "Novembre"]:
    print("La saison est l'automne.")
elif mois in ["Décembre", "Janvier", "Février"]:
    print("La saison est l'hiver.")
elif mois in ["Mars", "Avril", "Mai"]:
    print("La saison est le printemps.")
elif mois in ["Juin", "Juillet", "Août"]:
    print("La saison est l'été.")
else:
    print("Mois invalide.")

# 3. Vérification et ajout de fruit
fruits = ['banana', 'orange', 'mango', 'lemon']
nouveau_fruit = input("Entrez un fruit: ").lower()
if nouveau_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(nouveau_fruit)
    print("Liste mise à jour des fruits:", fruits)

# ----------- Niveau 3 -----------

# Dictionnaire de la personne
personne = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Vérifie et affiche la compétence du milieu
if 'skills' in personne:
    competences = personne['skills']
    milieu = len(competences) // 2
    print("Compétence du milieu:", competences[milieu])

# 2. Vérifie si 'Python' est présent
if 'skills' in personne:
    print("Possède la compétence Python :", 'Python' in personne['skills'])

# 3. Déterminer le type de développeur
if 'skills' in personne:
    comp = set(personne['skills'])
    if comp == {'JavaScript', 'React'}:
        print("Il est un développeur frontal.")
    elif {'Node', 'Python', 'MongoDB'}.issubset(comp):
        print("Il est un développeur backend.")
    elif {'React', 'Node', 'MongoDB'}.issubset(comp):
        print("Il est un développeur fullstack.")
    else:
        print("Titre inconnu.")

# 4. Vérifie si la personne est mariée et vit en Finlande
if personne.get('is_marred') and personne.get('country') == 'Finland':
    print(f"{personne['first_name']} {personne['last_name']} vit en Finlande. Il est marié.")
