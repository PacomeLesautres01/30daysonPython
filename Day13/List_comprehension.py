# JOUR 13 – LIST COMPREHENSION & LAMBDA

# ----------- Niveau 1 -----------

# 1. Itérer de 0 à 10 avec list comprehension
print("Exercice 1:")
print([i for i in range(11)])

# 2. Carrés de 0 à 10
print("\nExercice 2:")
print([i * i for i in range(11)])

# 3. Liste des tuples (nombre, carré)
print("\nExercice 3:")
print([(i, i**2) for i in range(11)])

# 4. Liste des nombres pairs entre 0 et 100
print("\nExercice 4:")
print([i for i in range(101) if i % 2 == 0])

# 5. Liste des nombres impairs entre 0 et 100
print("\nExercice 5:")
print([i for i in range(101) if i % 2 != 0])

# 6. Liste des entiers divisibles par 3
print("\nExercice 6:")
print([i for i in range(101) if i % 3 == 0])

# 7. Liste de tous les entiers entre 0 et 100 qui sont divisibles par 3 ou 5
print("\nExercice 7:")
print([i for i in range(101) if i % 3 == 0 or i % 5 == 0])

# 8. Extraire tous les mots d'une phrase en minuscules
print("\nExercice 8:")
sentence = 'I am enjoying learning python.'
print([word.lower() for word in sentence.split()])

# ----------- Niveau 2 -----------

# 1. Utiliser map pour créer une nouvelle liste avec la longueur de chaque mot
print("\nNiveau 2 - Exercice 1:")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
name_lengths = list(map(len, names))
print(name_lengths)

# 2. Utiliser filter pour filtrer les noms contenant plus de 6 lettres
print("\nNiveau 2 - Exercice 2:")
long_names = list(filter(lambda name: len(name) > 6, names))
print(long_names)

# 3. Utiliser lambda pour multiplier chaque élément de la liste par 2
print("\nNiveau 2 - Exercice 3:")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 4. Utiliser lambda pour filtrer les nombres pairs
print("\nNiveau 2 - Exercice 4:")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 5. Utiliser reduce pour calculer la somme
print("\nNiveau 2 - Exercice 5:")
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print("Somme des nombres:", total)

# 6. Combiner filter() et map() pour obtenir le carré des nombres impairs
print("\nNiveau 2 - Exercice 6:")
odd_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(odd_squares)

# ----------- Niveau 3 -----------

# 1. Créer une fonction anonyme qui renvoie True si un nombre est pair, False sinon
print("\nNiveau 3 - Exercice 1:")
is_even = lambda x: x % 2 == 0
print("4 est pair:", is_even(4))
print("7 est pair:", is_even(7))

# 2. Créer une fonction anonyme qui renvoie le carré d'un nombre
print("\nNiveau 3 - Exercice 2:")
square = lambda x: x ** 2
print("Carré de 5:", square(5))

# 3. Trier une liste de tuples par la deuxième valeur
print("\nNiveau 3 - Exercice 3:")
points = [(1, 2), (3, 1), (5, 0), (10, -1)]
sorted_points = sorted(points, key=lambda x: x[1])
print("Tri par deuxième valeur:", sorted_points)
