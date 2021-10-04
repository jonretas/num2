def NewtonSimple(x, f, Df, epsilon, maxit):
    import numpy as np
    # from numpy.linalg import norm, solve
    nit = 0
    fx = np.polyval(f, x)
    while (np.linalg.norm(fx) > epsilon) and (nit < maxit):
        nit += 1
        Dfx = np.polyval(Df, x)
        x = x - fx/Dfx
        fx = np.polyval(f, x)
    return [x, nit]
