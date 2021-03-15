# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

# doesn't seem to recognise pandas in VSC? Works fine in terminal?

# ref. for choosing from range of rows https://stackoverflow.com/questions/52152365/reading-just-range-of-rows-from-one-csv-file-in-python-using-pandas
import pandas as pd
import csv

df = pd.read_csv('tuneDatabase.csv', nrows=32)

tunesOfTheDay = df.sample(n=5)

print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay)

recentlyLearnedTunes = pd.read_csv('tuneDatabase.csv', nrows=2, skiprows=30)
print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes)