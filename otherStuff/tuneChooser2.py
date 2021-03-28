# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

import pandas as pd

df = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', index_col=0)
status = 34

x = input("Will we move on (or stay put)? y/n :")
if x == 'y':
    current = status + 1
    df1 = df[0:current]
    tunesOfTheDay = df1.sample(n=5)
    print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")
    recentlyLearnedTunes = df1[current-3:current]
    print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes, "\n")
    todaysNewTune = str(df.iloc[current])
    print("NEW TUNE FOR TODAY:\n ", todaysNewTune, "\n")
else:
    df1 = df[0:status]
    tunesOfTheDay = df1.sample(n=5)
    print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")
    recentlyLearnedTunes = df1[status-4:status-1]
    print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes, "\n")
    last_learnt_tune = str(df.iloc[status-1])
    print("LAST LEARNT TUNE TO REVISE:\n ", last_learnt_tune)


