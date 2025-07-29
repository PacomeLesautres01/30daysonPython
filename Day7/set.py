# ===== Jour 7 - Exercices sur les Sets =====

# Données initiales
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("===== NIVEAU 1 =====")


print("1) Longueur de it_companies :", len(it_companies))   # 1- la longueur de it_companies

it_companies.add('Twitter')                                 # 2- Ajout de twitter
print("2) Après ajout de Twitter :", it_companies)

it_companies.update(['Netflix', 'Spotify', 'Tesla'])        # 3- Ajout de plusieurs entreprises
print("3) Après ajout de plusieurs entreprises :", it_companies)

it_companies.remove('Google')                               # 4- Suppression d'une entreprise
print("4) Après suppression de Google :", it_companies)

# 5. Différence entre remove et discard
print("5) remove() renvoie une erreur si l'élément n'existe pas, alors que discard() ne renvoie pas d'erreur.")
it_companies.discard('Yahoo')  # Ne fait rien si absent
print("   Exemple avec discard('Yahoo') (aucune erreur) :", it_companies)


print("\n===== NIVEAU 2 =====")


print("1) Union de A et B :", A.union(B))                  # 1. Union de A et B
print("2) Intersection de A et B :", A.intersection(B))    # 2. Intersection de A et B
print("3) A est un sous-ensemble de B :", A.issubset(B))   # 3. A est-il un sous-ensemble de B ?
print("4) A et B sont disjoints :", A.isdisjoint(B))       # 4. A et B sont-ils disjoints ?
print("5) A union B :", A.union(B))                        # 5. Joindre A avec B et B avec A
print("   B union A :", B.union(A))
print("6) Différence symétrique entre A et B :", A.symmetric_difference(B))    # 6. Différence symétrique entre A et B


del A                                                      # 7- Supprime l'ens A
del B                                                      # Supprime l'ens B
print("7) Les ensembles A et B ont été supprimés.")    


print("\n===== NIVEAU 3 =====")

# 1. Convertir la liste age en set et comparer les longueurs
age_set = set(age)
print("1) Longueur de la liste age :", len(age))
print("   Longueur du set age_set :", len(age_set))
if len(age) > len(age_set):
    print("   La liste est plus longue (elle contient des doublons).")
else:
    print("   Le set est plus grand ou égal (mais il n'a que des valeurs uniques).")

# 2. Différences entre string, list, tuple et set
print("\n2) Différences entre les types de données :")
print("- string : Séquence IMMUTABLE de caractères (ex: 'Python')")
print("- list   : Collection ORDONNÉE, MUTABLE, accepte doublons (ex: [1,2,2])")
print("- tuple  : Collection ORDONNÉE, IMMUTABLE, accepte doublons (ex: (1,2,2))")
print("- set    : Collection NON ordonnée, NON indexée, UNIQUEMENT des éléments uniques (ex: {1,2,3})")

# 3. Compter les mots uniques dans une phrase
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()      # Transformer en liste
unique_words = set(words)     # Conserver seulement les mots uniques
print("\n3) Mots uniques dans la phrase :", unique_words)
print("   Nombre de mots uniques :", len(unique_words))
