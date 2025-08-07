# Jour 16 - Exercices sur le module datetime

from datetime import datetime, date

# 1️. Obtenir le jour, mois, année, heure, minute et horodatage actuels
now = datetime.now()
print("Date et heure actuelles :", now)
print("Jour :", now.day)
print("Mois :", now.month)
print("Année :", now.year)
print("Heure :", now.hour)
print("Minute :", now.minute)
print("Horodatage (timestamp) :", now.timestamp())

print("-" * 50)

# 2️. Formater la date actuelle
date_formatee = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date formatée :", date_formatee)

print("-" * 50)

# 3️. Convertir "5 décembre 2019" en objet date
date_str = "5 December, 2019"  # Doit être en anglais pour strptime
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print("Objet date à partir de la chaîne :", date_obj)

print("-" * 50)

# 4️. Calculer le temps restant jusqu'à la nouvelle année
nouvel_an = datetime(year=now.year + 1, month=1, day=1)
temps_restant_nouvel_an = nouvel_an - now
print("Temps restant jusqu'au Nouvel An :", temps_restant_nouvel_an)

print("-" * 50)

# 5️. Calculer le temps écoulé depuis le 1er janvier 1970
epoch = datetime(year=1970, month=1, day=1)
temps_depuis_epoch = now - epoch
print("Temps écoulé depuis le 1er janvier 1970 :", temps_depuis_epoch)

print("-" * 50)

# 6️. Exemples d'utilisation du module datetime
print(" Exemples d'utilisation de datetime :")
print("- Analyse de séries chronologiques")
print("- Obtenir un horodatage des activités d'une application")
print("- Ajouter la date à un article de blog")
print("- Créer un système de rappel ou d'alarme")
print("- Calculer des échéances ou dates limites")
print("- Enregistrer des logs système")
