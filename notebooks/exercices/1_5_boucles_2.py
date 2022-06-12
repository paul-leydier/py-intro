# On itere normalement
for i in range(1, 5):
    for j in range(i):
        print("* ", end='')
    print("")  # Retour a la ligne

# On itere a l'envers
for i in range(5, 0, -1):
    for j in range(i):
        print("* ", end='')
    print("")  # Retour a la ligne