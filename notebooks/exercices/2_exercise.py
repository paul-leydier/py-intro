def estimate_pi(n):
    random_points = np.random.rand(n, 2)  # n random points with x and y between 0 and 1
    is_in_circle = np.sum(random_points ** 2, axis=1) <= 1  # booleans (true if point is in the circle)
    n_in_circle = np.sum(is_in_circle)  # number of points in the circle
    return (n_in_circle / n) * 4

estimate_pi(10000000)