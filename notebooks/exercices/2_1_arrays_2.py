a = np.full((5, 5), 1)  # Declare un array 5x5 rempli de 1
a[1:-1, 1:-1] = 0  # Selectionne la slice au milieu de l'array, puis lui applique la valeur 0
print(a)