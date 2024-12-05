import numpy as np


def nm_step(f, vertices, alpha, gamma, phi, sigma):
    """
    @param alpha: 0 < alpha
    @param beta: 0 < beta
    @param phi: 0 < phi <= 0.5
    @param sigma: 0 < sigma <= 0.5
    """
    vertices = sorted(vertices, key=lambda i: f(i))

    x0 = sum(vertices[:-1]) / (len(vertices) - 1)
    xr = x0 + alpha * (x0 - vertices[-1])
    # reflection
    if f(vertices[0]) <= f(xr) < f(vertices[-2]):
        vertices[-1] = xr
        return vertices
    if f(xr) < f(vertices[0]):
        xe = x0 + gamma * (xr - x0)
        if f(xe) < f(xr):
            vertices[-1] = xe
        else:
            vertices[-1] = xr
        return vertices
    # f(xr >= f(vertices[-2])
    if f(xr) < f(vertices[-1]):
        xc = x0 + phi * (xr - x0)
        if f(xc) < f(xr):
            vertices[-1] = xc
            return vertices
    else:
        xc = x0 + phi * (vertices[-1] - x0)
        if f(xc) < f(vertices[-1]):
            vertices[-1] = xc
            return vertices

    for i in range(1, len(vertices)):
        vertices[i] = vertices[0] + sigma * (vertices[i] - vertices[0])

    return vertices


a = 1
b = 100


def rosenbrock(x, y):
    return (a - x) ** 2 + b * (y - x**2) ** 2


global_min = (a, a**2)


vertices = [
    np.array([1000, 100]),
    np.array([2000, 200]),
    np.array([1000, 200]),
]
for _ in range(150):
    vertices = nm_step(lambda p: rosenbrock(p[0], p[1]), vertices, 1, 2, 0.5, 0.5)
    print(vertices[0], np.linalg.norm(vertices[0] - global_min))
