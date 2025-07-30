# 1. Créez un dictionnaire vide appelé chien
chien = {}

# 2. Ajouter le nom, la couleur, la race, les jambes, l'âge
chien['nom'] = 'Rex'
chien['couleur'] = 'noir'
chien['race'] = 'Labrador'
chien['jambes'] = 4
chien['âge'] = 5

# 3. Créez un dictionnaire étudiant avec les clés demandées
étudiant = {
    'first_name': 'Pacôme',
    'last_name': 'Nyabo',
    'gender': 'masculin',
    'age': 20,
    'marital_status': 'célibataire',
    'skills': ['Python', 'HTML'],
    'country': 'Côte d\'Ivoire',
    'city': 'Abidjan',
    'address': 'Cocody, Riviera'
}

# 4. Obtenez la longueur du dictionnaire étudiant
print("Longueur du dictionnaire étudiant :", len(étudiant))

# 5. Obtenez la valeur de 'skills' et vérifiez le type de données
print("Compétences :", étudiant['skills'])
print("Type de 'skills' :", type(étudiant['skills']))

# 6. Modifier la liste 'skills' en ajoutant une ou deux compétences
étudiant['skills'].append('CSS')
étudiant['skills'].append('Git')
print("Compétences mises à jour :", étudiant['skills'])

# 7. Obtenez les clés du dictionnaire comme une liste
cles = list(étudiant.keys())
print("Clés du dictionnaire étudiant :", cles)

# 8. Obtenez les valeurs du dictionnaire comme une liste
valeurs = list(étudiant.values())
print("Valeurs du dictionnaire étudiant :", valeurs)

# 9. Convertir le dictionnaire en liste de tuples avec items()
liste_tuples = list(étudiant.items())
print("Dictionnaire en liste de tuples :", liste_tuples)

# 10. Supprimer un élément du dictionnaire (ex. 'marital_status')
del étudiant['marital_status']
print("Dictionnaire après suppression d'un élément :", étudiant)

# 11. Supprimer complètement le dictionnaire 'chien'
del chien
# print(chien)  # Cette ligne générera une erreur si décommentée, car 'chien' est supprimé
