#Question 5
import numpy as np
import matplotlib.pyplot as plt
delta = 1
gamma = 4
beta = 1
alpha = 2

def H(x1, x2):
    return delta*x1 - gamma*np.log(x1) + beta*x2 - alpha*np.log(x2)

x1 = np.linspace(0.1,10,1001)
x2 = np.linspace(0.1,10,1001)
X1, X2 = np.meshgrid(x1, x2) #Champ des positions
Z=H(X1, X2)
plt.figure(figsize = (6,6))
graphe = plt.contour(X1, X2, Z, np.linspace(-2, 7, 20))
plt.title("Courbes de niveau de H")
plt.scatter(gamma/delta, alpha/beta, label="Point d'équilibre")
plt.grid()
plt.legend()
plt.show()