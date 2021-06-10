# défini une liste vide pour stocker les lignes uniques

ld= []
ls=[]


# ouvrir le fichier en lecture seule
with open('results.txt', 'r') as file:
    # lire le fichier ligne par ligne
    for line in file:
        ld.append(line)
        if line not in ls:
            ls.append(line)
            ld.remove(line)
      

# réouvrir le fichier mais en mode écriture (ce qui effacera le contenu existant) et écrire les lignes de la liste
with open('result2.txt', 'w') as file:
    for line in ld:
      file.write(line)