# Jour 3: 30 Days of Python Programming

#Exercices - Jour 3
# 1- Déclaration de âge comme variable entière
age = 20  # 
print("Âge :", age)

# 2- Déclaration de taille comme variable flottante
taille = 1.75  
print("Taille :", taille)

# 3- Variable qui stocke un numéro complexe
numero_complexe = 3 + 4j  
print("Numéro complexe :", numero_complexe)

# 4- Calcul de la zone d'un triangle
# Formule : zone = 0.5 * base * hauteur
base = float(input("Entrez la base du triangle: "))
hauteur = float(input("Entrez la hauteur du triangle: "))
zone_triangle = 0.5 * base * hauteur
print("La zone du triangle est de", zone_triangle)

# 5- Calcul du périmètre d'un triangle
# Formule : périmètre = a + b + c
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre_triangle = a + b + c
print("Le périmètre du triangle est", perimetre_triangle)

# 6- Calcul de la surface et du périmètre d'un rectangle
# Formule : surface = longueur * largeur, périmètre = 2 * (longueur + largeur)
longueur = float(input("Entrez la longueur du rectangle: "))
largeur = float(input("Entrez la largeur du rectangle: "))
surface_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("Surface du rectangle :", surface_rectangle)
print("Périmètre du rectangle :", perimetre_rectangle)

# 7- Calcul de la surface et de la circonférence d'un cercle
# Formule : surface = π * r^2, circonférence = 2 *
r = float(input("Entrez le rayon du cercle: "))
pi = 3.14
surface_cercle = pi * r * r
circonference_cercle = 2 * pi * r
print("Surface du cercle :", surface_cercle)
print("Circonférence du cercle :", circonference_cercle)

# -------- Exercice 8 --------
# y = 2x - 2 -> pente m = 2
m = 2
x_intercept = 1  # Résoudre 0 = 2x - 2 => x = 1
y_intercept = -2  # quand x = 0
print("Pente :", m, "Ordonnée à l'origine (y) :", y_intercept, "Abscisse (x) :", x_intercept)

# -------- Exercice 9 --------
# Points (2, 2) et (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pente_2pts = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Pente (deux points) :", pente_2pts)
print("Distance euclidienne :", distance)

# -------- Exercice 10 --------
print("Comparaison des pentes :", m == pente_2pts)

# -------- Exercice 11 --------
# y = x^2 + 6x + 9 -> (x+3)^2, y = 0 quand x = -3
for x in [-5, -3, 0, 2]:
    y = x**2 + 6*x + 9
    print(f"Pour x={x}, y={y}")
print("y = 0 pour x = -3")

# 12- Comparaison de la longueur de python et dragon
len_python = len("Python")
len_dragon = len("Dragon")
print("Longueurs:", len_python, len_dragon)
print("Comparaison falsy:", len_python > len_dragon and len_dragon > len_python)

# -------- Exercice 13 --------
print("'on' dans python et dragon ? :", ("on" in "python") and ("on" in "dragon"))

# -------- Exercice 14 --------
phrase = "I hope this course is not full of jargon."
print("'jargon' dans la phrase ?", "jargon" in phrase)

# -------- Exercice 15 --------
print("Pas de 'on' dans Dragon et Python ?", not ("on" in "Dragon" and "on" in "Python"))

# -------- Exercice 16 --------
python_len = len("python")
python_float = float(python_len)
python_str = str(python_len)
print("Longueur:", python_len, "Float:", python_float, "String:", python_str)

# -------- Exercice 17 --------
nombre = int(input("Entrez un nombre pour vérifier s'il est pair : "))
if nombre % 2 == 0:
    print(nombre, "est pair")
else:
    print(nombre, "est impair")

# -------- Exercice 18 --------
print("7 // 3 == int(2.7) ?", 7 // 3 == int(2.7))

# -------- Exercice 19 --------
print("Type de '10' == type de 10 ?", type("10") == type(10))

# 20- Comparaison 
print("Vérification de int('9,8') == 10 ?", int(9.8) == 10)

# 21- Saisie des heures travaillées et du taux horaire
heures = float(input("Entrez les heures travaillées: "))
taux_horaire = int(input("Entrez le taux par heure: "))
gain = heures * taux_horaire
print("Votre gain hebdomadaire est de", gain , "FCFA.")

# 22- Conversion d'années en secondes
# 1 an = 365 jours, 1 jour = 24 heures, 1 heure = 60 minutes, 1 minute = 60 secondes
annees = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = annees * 365 * 24 * 60 * 60
print(f"Vous avez vécu environ {secondes} secondes.")

# 23-  Script Python qui affiche le tableau
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
