# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Caoimhin Vallely

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 4))
ypoints = xpoints
plt.plot(xpoints, ypoints, color = 'blue', label = "f(x)=x")

# add x squared
xpoints = np.array(range(0, 4))
ypoints = xpoints **2
plt.plot(xpoints, ypoints, color = 'red', label = "g(x)=x^2")

# add x cubed
xpoints = np.array(range(0, 4))
ypoints = xpoints **3

plt.plot(xpoints, ypoints, color = 'green', label = "h(x)=x^3")

plt.title("Plottask")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()