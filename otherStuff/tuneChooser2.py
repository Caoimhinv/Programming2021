# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

# doesn't seem to recognise pandas in VSC? Works fine in terminal?

# ref. for choosing from range of rows https://stackoverflow.com/questions/52152365/reading-just-range-of-rows-from-one-csv-file-in-python-using-pandas
import pandas as pd

df = pd.read_csv('tuneDatabase.csv', nrows=31)

tuneOfTheDay1 = df.sample(n=5)

print(tuneOfTheDay1)