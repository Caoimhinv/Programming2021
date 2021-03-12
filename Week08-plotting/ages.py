# from Andrew Beatty GMIT lab
# Write a program that plots a histogram of salaries from numpyStuff.py

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) # this is so that the "random" numbers are the same
                  # each time to make it easier to debug
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size= numberOfEntries) # I don't like this. Prefer to have absolute values at top

plt.scatter(ages, salaries, label = "salaries") # this will be random

# adding a normal ditribution curve I think!
x = np.random.normal(size=80000)
plt.hist(x)

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
plt.show()
