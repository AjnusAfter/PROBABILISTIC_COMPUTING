# A

import matplotlib.pyplot as plt

a = 39373
c = 0
M = 2 ^ 31-1
n_samples = 10000


def LCG(seed, a, c, M, n_samples):
    x = seed
    u = []

    for i in range(n_samples):
        nx = (a*x + c) % M
        u.append(float(nx) / float(M))
        x = nx
    return u


U = LCG(4, a, c, M, n_samples)
print(len(U))
plt.hist(U, facecolor="purple")
plt.show()


# B

def DADO(U):
    n = len(U)
    dado = []

    for i in range(n):
        if (U[i] < 1.0/6.0):
            dado.append(1)
        elif (U[i] < 2.0/6.0):
            dado.append(2)
        elif (U[i] < 3.0/6.0):
            dado.append(3)
        elif (U[i] < 4.0/6.0):
            dado.append(4)
        elif (U[i] < 5.0/6.0):
            dado.append(5)
        else:
            dado.append(6)
            
    return dado

U = LCG(3, a, c, M, 6000000)
dado = DADO(U)
plt.hist(dado, 6, facecolor = 'green')
plt.show()