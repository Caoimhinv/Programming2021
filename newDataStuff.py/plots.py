# ref for pie chart from csv file https://www.w3resource.com/graphics/matplotlib/piechart/matplotlib-piechart-exercise-4.php



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df =  pd.read_csv('tuneFrequency.csv')
tuneType = df["TuneType"]
frequency = df["Frequency"] 
plt.pie(frequency,labels = tuneType)
plt.show()

# Work in progress!
# bins=np.arange(min(tuneType), max(tuneType) + 1, 1)

# print(df['TuneType'].count())
# plt.hist(df['TuneType'], bins)

# plt.show()