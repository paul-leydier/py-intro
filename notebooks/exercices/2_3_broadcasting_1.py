def sigmoid(x):
    return 1 / 1 + np.exp(-x)  # application de la formule via broadcasting

sigmoid(np.random.rand(2, 4))