# Dans cette fonction, nous demandons a l'utilisateur s'il souhaite continuer
# et renvoyons un booleen en fonction de sa reponse
# Si nous ne comprenons pas la reponse, nous reponsons la question
def ask_if_keep_going():
    answer = input()
    if answer == 'O':
        return True
    elif answer == 'N':
        return False
    else:
        print("Je n'ai pas compris. Utilisez 'O' or 'N'")
        return ask_if_keep_going()  # On appelle ceci une fonction recursive. Dans certains cas, elle peut s'appeler elle-meme

print("Bienvenue sur la calculatrice Python!")
keep_going = True
# Boucle principale, durant laquelle nous effectuons un calcul, 
# puis demandons a l'utilisateur s'il veut continuer
while keep_going:
    # Recuperation du calcul a effectuer
    print("Entrez votre premier nombre :")
    first_number = int(input())
    print("Entrez votre second nombre :")
    second_number = int(input())
    print("Entrez l'opération à effectuer (acceptés : '+', '-', '*', '/') :")
    operation = input()
    
    # On effectue l'operation demandee
    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "*":
        print(first_number * second_number)
    elif operation == "/":
        print(first_number / second_number)
    else:
        print("Opérateur invalide.")

    # Une fois le calcul termine, nous demandons a l'utilisateur s'il veut continuer
    print("Voulez-vous continuer ? (O/N)")
    keep_going = ask_if_keep_going()
print("Au revoir.")