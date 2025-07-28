# ----------------------------
# jour 6 - Tuples 
# ----------------------------

# ----------------------------
# Level 1
# ----------------------------

# 1. Creation d'un tuple vide
tuple_vide = ()
print("Tuple vide :", tuple_vide)

# 2. Création d'un tuple avec noms de sœurs et frères
sisters = ('Alice', 'Emma', 'Sophie')
brothers = ('Paul', 'Lucas', 'Hugo')
print("Sœurs :", sisters)
print("Frères :", brothers)

siblings = brothers + sisters                                 # 3- Combinaison des tuples frères et sœurs
print("Frères et sœurs :", siblings)                          # Affichage du tuple combiné
print("Nombre total de frères et sœurs :", len(siblings))     # 4- Affichage du nombre total de frères et sœurs

family_members = siblings + ('Papa', 'Maman')                 # 5- Ajout des parents au tuple
print("Membres de la famille :", family_members)              # Affichage du tuple complet de la famille

# ----------------------------
# Level 2
# ----------------------------

# 1. Déballer siblings et parents depuis family_members
*siblings_only, father, mother = family_members
print("Siblings :", siblings_only)
print("Père :", father)
print("Mère :", mother)



fruits = ('Banane', 'Orange', 'Pomme')                          # 2- Création de tuples pour les fruits
vegetables = ('Carotte', 'Tomate', 'Chou')                      # Création de tuples pour les légumes
animal_products = ('Lait', 'Fromage', 'Œufs')                   # Création de tuples pour les produits animaux
food_stuff_tp = fruits + vegetables + animal_products
print("Nourriture (tuple) :", food_stuff_tp)                    # Affichage du tuple de nourriture


food_stuff_lt = list(food_stuff_tp)                             # 3- Conversion du tuple en liste
print("Nourriture (liste) :", food_stuff_lt)                    # Affichage de la liste de nourriture

# 4. Extraire l'élément ou les éléments du milieu
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("Élément(s) du milieu :", middle_items)

# 5. Extraire les 3 premiers et 3 derniers éléments
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("3 premiers éléments :", first_three)
print("3 derniers éléments :", last_three)

# 6. Supprimer le tuple food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Ceci causerait une erreur car le tuple est supprimé

# 7. Vérifier si un élément existe dans nordic_countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia est un pays nordique ?", 'Estonia' in nordic_countries)
print("Iceland est un pays nordique ?", 'Iceland' in nordic_countries)
