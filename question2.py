#Affiche un champ de dérivées de positions avec quiver ou streamplot

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0,20,21)
x2 = np.linspace(0,20,21)
X1, X2 = np.meshgrid(x1, x2) #Champ des positions

def F(X1, X2):
    #Fonction qui retourne la dérivée de la position pour Lotka - Volterra
    alpha = 2
    beta = 1
    gamma = 4
    delta = 1
    return X1*(alpha - beta*X2), -X2*(gamma - delta*X1)

U, V = F(X1, X2) #champ des dérivées

fig = plt.figure(figsize = (12,6))

ax1 = plt.subplot(121)
ax1.quiver(X1, X2, U, V)

ax2 = plt.subplot(122)
ax2.streamplot(X1, X2, U, V, density=1)
plt.show()