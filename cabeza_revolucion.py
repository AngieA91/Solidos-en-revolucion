import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(a):
    return np.sqrt((1.5**2) - (a**2))

z_val = np.linspace(-1.5, 1.5, 50)
ang = np.linspace(0, 2*np.pi, 100)
Z, T = np.meshgrid(z_val, ang)

X = f(Z)
X_R = X* np.cos(T)
Y_R = X *np.sin(T)

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_R, Y_R, Z, color='b', edgecolor='c', alpha=0.6)
ax.set_title('Cabeza Revolucionada')
plt.show()