# Jour 5 - Exercices Listes

# === Niveau 1 ===


liste_vide = []
print("1: Liste vide =", liste_vide)     # 1. Liste vide

# 2. Déclarer une liste avec au moins 5 éléments
my_list = ['apple', 'banana', 'orange', 'mango', 'lemon']
print("2: Ma liste =", my_list)          # Affichage de ma liste
print("3: Longueur =", len(my_list))     # 3. Longueur de la liste

# 4. Premier, milieu et dernier élément
premier_element = my_list[0]
element_moyen = my_list[len(my_list)//2]
dernier_element = my_list[-1]
print("4:", premier_element, element_moyen, dernier_element) #Affichage des elements

# 5. Liste avec différents types de données
mixed_data_types = ['Pacôme', 20, 1.75, 'Célibataire', 'Togo']
print("5:", mixed_data_types)

# 6. Liste d'entreprises IT
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("6:", it_companies)                  # Affichage de la liste d'entreprises IT
print("7:", it_companies)                  # 7. Afficher la liste d'entreprises IT
print("8: Nombre =", len(it_companies))    # 8. Nombre d’entreprises

# 9. Première, milieu et dernière entreprise
first_c = it_companies[0]
middle_c = it_companies[len(it_companies)//2]
last_c = it_companies[-1]
print("9:", first_c, middle_c, last_c)     # Affichage de la premiere, moyenne et derniere entreprises

# 10. Modifier une entreprise
it_companies[1] = 'YouTube'                # Modification de Google en YouTube
print("10:", it_companies)                 # Affichage de la liste après modification

# 11. Ajouter une entreprise
it_companies.append('Twitter')             # Ajout de Twitter
print("11:", it_companies)                 # Affichage de la liste après ajout

# 12. Insérer au milieu
it_companies.insert(len(it_companies)//2, 'Netflix') # Insertion de Netflix au milieu
print("12:", it_companies)                           # Affichage de la liste après insertion

# 13. Mettre en majuscules un nom (sauf IBM)
it_companies[0] = it_companies[0].upper()  # Mettre Facebook en majuscules
print("13:", it_companies)                 # Affichage de la liste après mise en majuscules

# 14. Joindre les entreprises avec '#;  '
joined_companies = '#;  '.join(it_companies)
print("14: Entreprises jointes =", joined_companies)  # Affichage des entreprises jointes avec #;

# 15. Vérifier si une entreprise existe dans la liste it_companies
entreprise_a_verifier = 'Google'
print("15. Google existe-t-il dans la liste ?", entreprise_a_verifier in it_companies)  # Affiche True ou False

# 16. Trier la liste avec la méthode sort()
it_companies.sort()
print("16. Liste triée :", it_companies)    # Affichage de la liste triée

# 17. Inverser la liste dans l'ordre décroissant avec la méthode reverse()
it_companies.reverse()
print("17. Liste inversée :", it_companies)  # Affichage de la liste inversée

# 18. Extraire (slice) les 3 premières entreprises de la liste
premieres_trois = it_companies[:3]
print("18. Les 3 premières entreprises :", premieres_trois)

# 19. Extraire les 3 dernières entreprises de la liste
dernieres_trois = it_companies[-3:]
print("19. Les 3 dernières entreprises :", dernieres_trois)

# 20. Extraire l'entreprise ou les entreprises du milieu
index_milieu = len(it_companies) // 2
if len(it_companies) % 2 == 0:  # Si la liste a un nombre pair d'éléments
    milieu = it_companies[index_milieu-1:index_milieu+1]
else:  # Si la liste a un nombre impair d'éléments
    milieu = [it_companies[index_milieu]]
print("20. Entreprise(s) du milieu :", milieu)

# 21. Supprimer la première entreprise de la liste
it_companies.pop(0)
print("21. Après suppression de la première entreprise :", it_companies)

# 22. Supprimer l'entreprise ou les entreprises du milieu
index_milieu = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[index_milieu-1:index_milieu+1]
else:
    del it_companies[index_milieu]
print("22. Après suppression de l'entreprise/les entreprises du milieu :", it_companies)

# 23. Supprimer la dernière entreprise de la liste
it_companies.pop(-1)
print("23. Après suppression de la dernière entreprise :", it_companies)

# 24. Supprimer toutes les entreprises de la liste
it_companies.clear()
print("24. Après avoir vidé complètement la liste :", it_companies)

# 25. Détruire complètement la variable it_companies
del it_companies
# print(it_companies)  # Décommenter cette ligne provoquera une erreur car la liste n'existe plus

# 26. Joindre les deux listes front_end et back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
liste_complete = front_end + back_end
print("26. Liste fusionnée (front-end + back-end) :", liste_complete)

# 27. Copier la liste fusionnée et insérer Python et SQL après Redux
full_stack = liste_complete.copy()
position_redux = full_stack.index('Redux') + 1  # Position après Redux
full_stack.insert(position_redux, 'Python')
full_stack.insert(position_redux + 1, 'SQL')
print("27. Liste full_stack avec Python et SQL ajoutés :", full_stack)



# === Niveau 2 ===

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier
ages.sort()
print("\nNiveau 2")
print("1: Ages triés =", ages)

# Min et max
min_age, max_age = min(ages), max(ages)
print("2: Min =", min_age, "Max =", max_age)

# Ajouter min et max
ages.extend([min_age, max_age])
print("3: Ajout min/max =", ages)

# Médiane
ages.sort()
mid = len(ages)//2
if len(ages) % 2 == 0:
    median = (ages[mid-1] + ages[mid]) / 2
else:
    median = ages[mid]
print("4: Médiane =", median)

# Moyenne
average = sum(ages)/len(ages)
print("5: Moyenne =", round(average,2))

# Plage des âges
age_range = max(ages) - min(ages)
print("6: Plage des âges =", age_range)

# Pays
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid_country = countries[len(countries)//2]
print("\n7: Pays du milieu =", mid_country)

# Diviser en deux
first_half = countries[:(len(countries)+1)//2]
second_half = countries[(len(countries)+1)//2:]
print("8: Première moitié =", first_half)
print("   Deuxième moitié =", second_half)

# Séparer pays
first_three, scandic = countries[:3], countries[3:]
print("9: Trois premiers pays =", first_three)
print("   Pays nordiques =", scandic)

# Fusion des stacks
front_end = ['html', 'css', 'js', 'react', 'redux']
back_end = ['node', 'express', 'mongodb']
full_stack = front_end + back_end

# Insérer Python et SQL après Redux
index_redux = full_stack.index('redux') + 1
full_stack[index_redux:index_redux] = ['Python', 'SQL']
print("\n10: Full stack final =", full_stack)
