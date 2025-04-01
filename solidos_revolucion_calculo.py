import numpy as np #libreria para crear la matriz principal donde se va a graficar el solido
import matplotlib.pyplot as plt # para visualizar los solidos en 3d
from mpl_toolkits.mplot3d import Axes3D #generar los solidos en 3d

def f(x):
    return ((x+2.5)**5)+0.5 #funcion a usar


Y = np.linspace(-3.370550563, -1.149039961, 100)  # Intervalo en que se va a graficar, genera 100 valores entre los puntos escritos y los almacena en un arreglo llamado "y"
ang = np.linspace(0, 2*np.pi, 100)  # Intervalo del angulo de rotación, almacena los valores en un arreglo llamado "ang"

Y, T = np.meshgrid(Y, ang)  # plano en donde se va a graficar (hace una "malla" usando los valores de Y, asignando cada uno a los de ang)
X = f(Y)  # Función aplicada a Y (Toma los valores en Y, los pasa por la funcion y los almacena en un arreglo llamado X)
Z = Y * np.sin(T)  # Revolucion en z (convertimos los puntos a coordenadas cartesianas usando los valores en Y y del angulo generados)
Y = Y * np.cos(T)  # Revolucion en y

# Grafica del sólido (parámetros generales que saqué de internet)
fig = plt.figure(figsize=(5,5)) #ancho y alto de la figura en pulgadas 
ax = fig.add_subplot(111, projection='3d') #genera el plano (111 porque estamos en x,y,z y define el tipo de objeto a graficar)
ax.plot_surface(X, Y, Z, color='b', edgecolor='c', alpha=0.6) # lo que se va a graficar, color, color del borde y opacidad

# Nombres  etiquetas tanto del plano como del grafico
ax.set_title('Base Revolucionada')

plt.show() #abre el terminal en donde se va a mostrar el sólido