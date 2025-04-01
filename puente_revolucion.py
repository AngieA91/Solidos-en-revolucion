import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

def f(x):
    return ((-x/2)**2) 
Y = np.linspace(-2, 0, 100) 
ang = np.linspace(0, 2*np.pi, 100)  
Y, T = np.meshgrid(Y, ang) 
X = f(Y)  
Z = Y * np.sin(T)  
Y = Y * np.cos(T)  
fig = plt.figure(figsize=(5,5)) 
ax = fig.add_subplot(111, projection='3d') 
ax.plot_surface(X, Y, Z, color='b', edgecolor='c', alpha=0.6) 
ax.set_title('Cuello Revolucionado')
plt.show() 