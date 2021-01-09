import numpy as np
import matplotlib.pyplot as plt

x0 = np.array([1])
x02 = np.array([0.5, 0.3])
dt = 0.000001
t0 = 0
tf = 10

def f(x, t):
    return x

def F(x, t):
    #Fonction qui retourne la dérivée de la position pour Lotka - Volterra
    alpha = 2
    beta = 1
    gamma = 4
    delta = 1
    x1, x2 = x[0], x[1]
    return np.array([x1*(alpha - beta*x2), -x2*(gamma - delta*x1)])

def solve_euler_explicit(f, x0, dt, t0, tf):
    ''' Approche dx/dt = f(t, x) par méthode d'Euler
    Parametres
    ----------
    f : fonction RxR^n -> R^n 
    x0 : condition initiale 1D Numpy array
    t : pas de temps
    t0 : temps initial
    tf : temps final
    Retours
    -------
    t : vecteur des temps : 1D numpy array
    x : vecteur de la solution : nD numpy array
    '''

    t = np.arange(start=t0, stop=tf, step=dt)
    x = np.zeros( (len(t), len(x0)) )
    x[0] = x0
    for n in range(0,len(t)-1):
        x[n+1] = x[n] + f(x[n],t[n])*(t[n+1] - t[n]) #à remplacer par *dt ?
    return t, x

t, x = solve_euler_explicit(F, x02, dt, t0, tf)
x=x.transpose()
plt.plot(x[0], x[1])
plt.show()







'''
Pour visualiser

t, x = solve_euler_explicit(f, x0, dt, t0, tf)
y = np.array(np.exp(t))
plt.plot(t, np.exp(t), label='solution explicite')
plt.legend
plt.plot(t, x, label='Euler')
plt.legend()
plt.show()
'''

""" temps = []
delt=[]
dts = np.linspace(10**-5, 10**-2, 200)
for dt in dts:
    t, x = solve_euler_explicit(f, x0, dt, t0, tf)
    #y = np.array(np.exp(t))
    #diff = abs(x - y)
    #delta = np.max(diff)
    delta = np.abs(x[-1] - np.exp(1))
    temps.append(dt)
    delt.append(delta[0])

fit=np.polyfit(np.log(temps), np.log(delt), 1)
print("L'ordre de convergence est : ", fit[0])

fig=plt.figure(figsize = (18,9))
ax1=plt.subplot(121)
ax1.set_title("Ecart en fonction de dt")
ax1.plot(temps, delt)

ax2=plt.subplot(122)
ax2.set_title("Graphe log - log")
ax2.loglog(temps, delt)
ax2.loglog(temps, np.power(temps, fit[0])*np.exp(fit[1]))

plt.grid()
plt.show() """
