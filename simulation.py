import math
import numpy as np

# Simulates a gaussian distribution using the uniform distribution
def simul_gaussian(N):
    X_distrib = []
    # X is assigned the first values to verify U^2+V^2 <= 1
    # i.e. the values of U and V that are on the unity disk
    for _ in range(N):
        U = 1
        V = 1
        while U**2 + V**2 > 1:
            U = np.random.uniform(-1.0, 1.0)
            V = np.random.uniform(-1.0, 1.0)
        R = math.sqrt(U**2 + V**2)
        X = U * math.sqrt(-2 * math.log(R**2) / R**2)
        X_distrib.append(X)
    return X_distrib


# Simulates a brownian motion using the gaussian distribution
def simul_brownian(N, T):
    brownian_motion = [0]
    timestep = T/N
    gaussian = simul_gaussian(N+1)
    # Wt+1 = Wt + √(ti+1 - ti) * Xt
    # X ~ N(0,1)
    for i in range(1, N+1):
        actual_brownian = brownian_motion[i-1]
        brownian_motion.append(actual_brownian + math.sqrt(timestep) * gaussian[i])
    return brownian_motion
