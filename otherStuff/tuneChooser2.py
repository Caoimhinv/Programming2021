# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

# ref. for choosing from range of rows https://stackoverflow.com/questions/52152365/reading-just-range-of-rows-from-one-csv-file-in-python-using-pandas
import pandas as pd
import csv

df = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', nrows=33, index_col=0, header=None)
tunesOfTheDay = df.sample(n=5)
print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")
recentlyLearnedTunes = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', nrows=3, skiprows=31, index_col=0, header=None)
print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes, "\n")
todaysNewTune = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', nrows=1, skiprows=34, index_col=0, header=None)
print("NEW TUNE FOR TODAY:\n ", todaysNewTune, "\n")