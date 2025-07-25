# Jour 2: 30 Days of Python Programming

#Exercices - Jour 2
#Niveau 1
first_name = "Pacôme"
last_name = "NYABO"
full_name = "Pacôme NYABO"
country = "Togo"
city = "Lomé"
age = 30
year = 2025
is_married = False
is_true = True
is_light_on = True

# Déclaration de la variable multiple sur une seule ligne
animal, couleur, fruit, temperature, nombre, est_ouvert, est_actif, note, ville, pays = "chat", "bleu", "banane", 22.5, 7, True, False, 15.5,



#Niveau 2
#1- Afficher le type de chaque variable
print(type(first_name))  # Affiche le type de la variable first_name
print(type(last_name))   # Affiche le type de la variable last_name
print(type(full_name))   # Affiche le type de la variable full_name
print(type(country))     # Affiche le type de la variable country
print(type(city))        # Affiche le type de la variable city
print(type(age))         # Affiche le type de la variable age
print(type(year))        # Affiche le type de la variable year
print(type(is_married))  # Affiche le type de la variable is_married
print(type(is_true))     # Affiche le type de la variable is_true
print(type(is_light_on)) # Affiche le type de la variable is_light_on

#2- Longueur prenom grace à la fonction len()
print(len(first_name))  # Affiche la longueur de la variable first_name

#3- Comparaison de la longueur du prénom et du nom de famille
print(len(first_name) > len(last_name))  


num_one = 5
num_two = 4
# Addition de num_one et num_two
total = num_one + num_two
# Soustraction de num_one et num_two
diff = num_one - num_two
# Multiplication de num_one et num_two
product = num_one * num_two
# Division de num_one et num_two
division = num_one / num_two
# Modulo de num_one et num_two
remainder = num_one % num_two
#Exponentiation de num_one et num_two
exp = num_one ** num_two
# Division entière de num_one et num_two
floor_division = num_one // num_two

# Affichage des résultats des opérations
print("Total:", total)
print("Différence:", diff)
print("Produit:", product)
print("Division:", division)
print("Reste de la division:", remainder)
print("Exponentiation:", exp)
print("Division entière:", floor_division)



#12 
# la valeur de pi
pi = 3.1416
# Rayon donné
rayon = 30

# i. Calcul de l'aire du cercle
area_of_circle = pi * (rayon ** 2)
print("Aire du cercle :", area_of_circle, "m²")

# ii. Calcul de la circonférence du cercle
circum_of_circle = 2 * pi * rayon
print("Circonférence du cercle :", circum_of_circle, "m")

# iii. Demander un rayon à l'utilisateur et calculer l'aire
user_radius = float(input("Entrez le rayon du cercle : "))
user_area = pi * (user_radius ** 2)
print("Aire du cercle avec le rayon donné :", user_area, "m²")



#13- Saisie des informations utilisateur
first_name = input("Entrez votre prénom : ")
last_name = input("Entrez votre nom de famille : ")
country = input("Entrez votre pays : ")
age = int(input("Entrez votre âge : "))


'''>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>>'''