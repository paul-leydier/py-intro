def standardize(array):
    means = np.mean(array, axis=0)  # moyennes des colonnes
    stds = np.std(array, axis=0)  # ecart-type des colonnes
    
    return (array - means) / stds  # application de la formule via broadcasting

standardize(test_array)  # application de la fonction a notre array de test