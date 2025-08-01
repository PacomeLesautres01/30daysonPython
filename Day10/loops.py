###########################
# Jours 10: les boucles
###########################

#Exercices: niveau 1

# 1. Iteration de 0 a 10 avec la boucle for
for i in range(11):             #La fonction range génère une séquence de nombres de 0 à 11 exclus
    print(i)

# Iteration de 0 a 10 avec la boucle while
i = 0
while i <= 10:
    print(i)
    i += 1


# 2. Iteration de 10 a 0 avec la boucle for
for i in range(10, -1, -1):      #Le troisième argument -1 indique que nous voulons décrémenter
    print(i)


# Iteration de 10 a 0 avec la boucle while
i = 10      
while i >= 0:
    print(i)
    i -= 1


# 3.  une boucle qui fait sept appels à imprimer ()
for i in range(1, 8):
    print('#' * i)           


# 4.  Utilisation des boucles imbriquées 
for i in range(7):                     # Boucle externe pour les lignes
    for j in range(13):                # Boucle interne pour les colonnes
        print('#', end=' ')
    print()                            # Pour passer à la ligne suivante après chaque ligne de la boucle externe

# 5. Carrés parfaits
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Parcours d’une liste
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech_list:
    print(item)

# 7. Nombres pairs de 0 à 100
for i in range(101):
    if i % 2 == 0:
        print(i)


# 8. Nombres impairs de 0 à 100
for i in range(101):
    if i % 2 != 0:
        print(i)



#Exercices: niveau 2

# 1. Calcul de la somme avec une boucle for
somme = 0
for i in range(101):
    somme += i
print("La somme de tous les nombres est", somme)

# 2. Somme des pairs et des impairs
even_sum = sum(i for i in range(101) if i % 2 == 0)
odd_sum = sum(i for i in range(101) if i % 2 != 0)
print("La somme de tous les pairs est", even_sum)
print("La somme de tous les impairs est", odd_sum)



# Je n'ai pas pu faire l'exercice 3 car j'ai pas vite commencé et je rsique de ne pas envoyé mon code à temps.