nombre = input("Entrez un nombre: ")

print(nombre)

if int(nombre) < 10 :

    print("Ce nombre est trop petit")
    
# Transforme un texte en majuscule
"Bonjour".upper() 

# Transforme un texte en miniscule
"Bonjour".lower() 

# Met la première lettre de la phrase ou du mot en minuscule
"boujour".capitalize()

# Met une majuscule à la première lettre de chaque mots
"boujour".title()

# Remplace le partie du mot choisi en une autre
print("Bonjour".replace("jour", "soir").replace("Bon", "Mauvais"))

# Enleve les éspaces au début et à la fin
"Bonjour".strip()
# rstrip() et lstrip() verifie seulement le coté assigné à la fonction

