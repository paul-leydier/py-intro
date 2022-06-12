def reverse(string):
    new_string = ""
    # On parcourt string a l'envers, et on ajoute les lettres une 
    # par une a new_string
    for c in range(len(string)-1, -1, -1):
        new_string = new_string + string[c]
    # solution avancee : new_string = string[::-1]
    return new_string

# Solution avancee :
# def reverse(string):
#     return string[::-1]

reverse("Hello World!")