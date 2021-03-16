# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

# doesn't seem to recognise pandas in VSC? Works fine in terminal?

# ref. for choosing from range of rows https://stackoverflow.com/questions/52152365/reading-just-range-of-rows-from-one-csv-file-in-python-using-pandas
import pandas as pd

df = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', nrows=32, index_col=0)

tunesOfTheDay = df.sample(n=5)

print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")

recentlyLearnedTunes = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', nrows=2, skiprows=30, index_col=0)
print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes)