#a
import matplotlib.pyplot as plt

a = 39373
c = 0
M = 2^31-1
n_samples = 10000

def LCG(seed, a, c, M, n_samples):
    x = seed
    u = []
    
    for i  in range(n_samples):
        nx = (a*x + c) % M
        u.append(float(nx) / float(M))
        x = nx
    return u

U = LCG(4, a, c, M, n_samples)
print(len(U))                 
plt.hist(U, facecolor= "purple")
plt.show()
        