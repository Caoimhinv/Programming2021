# from Andrew Beatty lab GMIT
# Write a program that plots the function y = x2

import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()