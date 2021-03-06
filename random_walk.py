import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import rc

#Cristian Borja Ejercicio 25

rc("text", usetex = True)
resultados = np.loadtxt("random_walks.txt")
fig, ax = matplotlib.pyplot.subplots()
ax.hist(resultados, normed = 1, bins = 100)
ax.set_xlabel(r"Posici\'on final")
ax.set_ylabel(r"Probabilidad")
ax.set_title(r"Caminata aleatoria")
fig.savefig("rand.png")

