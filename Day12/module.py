# Jour 12: Module


# On utilise des modules comme random et string pour faire les exercices
import random
import string

# ----------------------------------------
# EXERCICES NIVEAU 1
# ----------------------------------------

# 1. Fonction qui génère un ID aléatoire de 6 caractères
def random_user_id():
    caracteres = string.ascii_letters + string.digits               # lettres + chiffres
    user_id = ''
    for i in range(6):
        user_id += random.choice(caracteres)                        # choisir un caractère au hasard
    return user_id

print("ID aléatoire (6 caractères) :", random_user_id())


# 2. Fonction qui génère plusieurs IDs avec taille et quantité données par l'utilisateur
def user_id_gen_by_user():
    nombre_caractere = int(input("Combien de caractères par ID ? "))
    nombre_ids = int(input("Combien d'IDs veux-tu ? "))

    characters = string.ascii_letters + string.digits

    for i in range(nombre_ids):
        user_id = ''
        for j in range(nombre_caractere):
            user_id += random.choice(characters)
        print(user_id)

print("Génération d'IDs aléatoires :")
# Pour exécuter cette fonction, décommentez la ligne suivante :
# user_id_gen_by_user()


# 3. Fonction qui génère une couleur RGB (3 nombres entre 0 et 255)
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("Couleur RGB aléatoire :", rgb_color_gen())

# ----------------------------------------
# EXERCICES NIVEAU 2
# ----------------------------------------

# 1. Fonction qui génère une liste de couleurs hexadécimales
def list_of_hexa_colors(n):
    for i in range(n):
        color = '#'
        for j in range(6):                              # chaque code hexa contient 6 caractères
            color += random.choice('0123456789abcdef')
        print(color)

print("Liste de 3 couleurs HEXA :")
list_of_hexa_colors(3)


# 2. Fonction qui génère une liste de couleurs RGB
def list_of_rgb_colors(n):
    for i in range(n):
        print(rgb_color_gen())

print("Liste de 3 couleurs RGB :")
list_of_rgb_colors(3)


# 3. Fonction qui génère soit des couleurs HEXA soit RGB selon le choix
def generate_colors(type, n):
    if type == 'hexa':
        list_of_hexa_colors(n)
    elif type == 'rgb':
        list_of_rgb_colors(n)
    else:
        print("Type inconnu. Tape 'hexa' ou 'rgb'.")

print("Couleurs générées automatiquement :")
generate_colors('hexa', 2)
generate_colors('rgb', 2)

# ----------------------------------------
# EXERCICES NIVEAU 3
# ----------------------------------------

# 1. Fonction qui mélange une liste
def shuffle_list(ma_liste):
    random.shuffle(ma_liste)                                   # mélange directement la liste
    return ma_liste

print("Liste mélangée :", shuffle_list([1, 2, 3, 4, 5]))


# 2. Générer 7 chiffres uniques entre 0 et 9
def unique_random_numbers():
    numbers = []
    while len(numbers) < 7:
        number = random.randint(0, 9)
        if number not in numbers:
            numbers.append(number)
    return numbers

print("7 chiffres uniques entre 0 et 9 :", unique_random_numbers())
