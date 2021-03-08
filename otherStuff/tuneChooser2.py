# this programme picks 5 random sets of tunes for me to practice!
# Author: Caoimhin Vallely

import pandas as pd

df = pd.read_csv('tuneDatabase.csv')

tuneOfTheDay1 = df.sample(n=5)

print(tuneOfTheDay1)